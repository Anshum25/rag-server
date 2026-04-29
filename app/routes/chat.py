import re

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.access_policy import (
    describe_access,
    describe_restricted_access,
    has_module_access,
    is_module_implemented,
    normalize_role,
)
from app.services.intent import detect_intent
from app.services.embedder import get_embedding
from app.services.exam_service import get_marks_by_trainee
from app.services.qdrant_service import search_data_filtered
from app.services.groq_service import generate_answer

router = APIRouter()

EXAM_ACCESS_ROLES = {"principal", "admin", "exam_staff"}
EXAM_KEYWORDS = {
    "exam",
    "marks",
    "mark",
    "result",
    "score",
    "scores",
    "subject",
    "grade",
    "grades",
}

AGGREGATE_KEYWORDS = {
    "highest",
    "lowest",
    "average",
    "total",
    "sum",
    "all",
    "every",
    "top",
    "best",
    "first",
}
HOSTEL_KEYWORDS = {"hostel", "room", "warden", "bed", "allocation"}
ATTENDANCE_KEYWORDS = {"attendance", "present", "absent", "leave"}
ACCESS_KEYWORDS = {"access", "permission", "permissions", "allowed", "role"}


class ChatRequest(BaseModel):
    message: str
    role: str = "principal"
    office_id: int = 1


def is_exam_question(message: str) -> bool:
    text = message.lower()
    return any(keyword in text for keyword in EXAM_KEYWORDS)


def is_hostel_question(message: str) -> bool:
    text = message.lower()
    return any(keyword in text for keyword in HOSTEL_KEYWORDS)


def is_attendance_question(message: str) -> bool:
    text = message.lower()
    return any(keyword in text for keyword in ATTENDANCE_KEYWORDS)


def is_access_question(message: str) -> bool:
    text = message.lower()
    return any(keyword in text for keyword in ACCESS_KEYWORDS)


def extract_search_name(message: str) -> str:
    text = message.lower().strip()
    
    # Pattern: "highest marks of [name]" or "marks of [name]" - extract name after "of"
    if " of " in text:
        parts = text.split(" of ")
        if len(parts) > 1:
            # Take the part after "of", clean it
            name_part = parts[1]
            # Remove trailing punctuation/keywords
            for keyword in EXAM_KEYWORDS.union({"show", "tell", "me", "for", "please", "trainee", "trainees", "student", "students", "?", ".", "!"}):
                name_part = name_part.replace(keyword, " ")
            name = " ".join(name_part.split())
            if name and len(name) > 2:
                return name
    
    # Pattern: "[name] marks" - name comes before keywords
    cleaned = text
    for keyword in EXAM_KEYWORDS.union(AGGREGATE_KEYWORDS).union({"show", "tell", "me", "of", "for", "please", "trainee", "trainees", "student", "students", "?", ".", "!"}):
        cleaned = cleaned.replace(keyword, " ")
    
    normalized = " ".join(cleaned.split())
    return normalized or message.strip()


def has_specific_name(message: str) -> bool:
    """Check if query contains a specific name pattern (not just aggregate words)"""
    text = message.lower()
    # If "of [something]" pattern exists, likely has a name
    if " of " in text:
        parts = text.split(" of ")
        if len(parts) > 1:
            after_of = parts[1].strip()
            # Check if after "of" has actual content (not just empty or punctuation)
            name_candidate = after_of.split()[0] if after_of.split() else ""
            if name_candidate and len(name_candidate) > 2 and name_candidate not in AGGREGATE_KEYWORDS:
                return True
    return False


def is_aggregate_query(message: str) -> bool:
    """Check if user is asking for aggregate data (highest, lowest, all, etc.)"""
    text = message.lower()
    return any(word in text for word in AGGREGATE_KEYWORDS)


def parse_marks_from_text(text: str) -> int:
    """Extract numeric marks from chunk text like 'Marks: 85' or 'marks: 60'"""
    # Look for patterns like "Marks: 85" or "marks: 60" or "Score: 75"
    match = re.search(r'[Mm]arks?:\s*(\d+)', text)
    if match:
        return int(match.group(1))
    # Try other patterns
    match = re.search(r'[Ss]core:\s*(\d+)', text)
    if match:
        return int(match.group(1))
    return 0


def get_sorted_exam_records(vector, office_id, user_role, sort_order="desc", limit=50):
    """
    Get exam records and sort by actual marks value.
    sort_order: 'desc' for highest first, 'asc' for lowest first
    """
    # Get large number of records (500) to find true top/bottom
    results = search_data_filtered(
        vector=vector,
        office_id=office_id,
        user_role=user_role,
        module="exam",
        limit=500,
    )
    
    if not results:
        return []
    
    # Parse marks from each result and sort
    records_with_marks = []
    for result in results:
        if result.payload:
            text = result.payload.get("text", "")
            marks = parse_marks_from_text(text)
            records_with_marks.append({
                "text": text,
                "marks": marks,
                "payload": result.payload
            })
    
    # Sort by marks value (not similarity!)
    reverse = (sort_order == "desc")
    records_with_marks.sort(key=lambda x: x["marks"], reverse=reverse)
    
    # Return top N
    return records_with_marks[:limit]


def build_exam_context(rows: list[dict]) -> str:
    return "\n".join(
        [
            (
                f"Trainee: {row['trainee_name']}\n"
                f"Course: {row['course_name']}\n"
                f"Subject: {row['subject_name']}\n"
                f"Marks: {row['marks_text']}\n"
                f"Result: {row['result']}"
            )
            for row in rows
        ]
    )


@router.post("/chat")
def chat(request: ChatRequest):
    try:
        user_message = request.message.strip()
        user_role = normalize_role(request.role)
        office_id = request.office_id
        intent = detect_intent(user_message)

        if intent == "text":
            if is_access_question(user_message):
                lowered = user_message.lower()
                if "not access" in lowered or "cannot access" in lowered or "can't access" in lowered:
                    return {
                        "type": "text",
                        "message": describe_restricted_access(user_role),
                    }

                return {
                    "type": "text",
                    "message": describe_access(user_role),
                }

            if is_exam_question(user_message):
                if not has_module_access(user_role, "exam"):
                    return {
                        "type": "text",
                        "message": "You do not have permission to access exam data.",
                    }

                # DETECT: Schedule/time queries - use vector search, NOT name lookup
                msg_lower = user_message.lower()
                schedule_keywords = ["schedule", "next week", "upcoming", "when", "date", "time", "exam date", "timetable"]
                if any(kw in msg_lower for kw in schedule_keywords):
                    vector = get_embedding(user_message)
                    results = search_data_filtered(
                        vector=vector,
                        office_id=office_id,
                        user_role=user_role,
                        module="exam",
                        limit=10,
                    )
                    if results:
                        context = "\n".join([r.payload.get("text", "") for r in results if r.payload])
                        answer = generate_answer(question=user_message, context=context)
                        return {"type": "text", "message": answer}
                    return {"type": "text", "message": "No exam schedule data found."}

                # Check if user mentioned a specific name (e.g., "highest marks of Ashwini")
                if has_specific_name(user_message):
                    search_name = extract_search_name(user_message)
                    marks_rows = get_marks_by_trainee(
                        search_name=search_name,
                        office_id=office_id,
                    )

                    if marks_rows:
                        answer = generate_answer(
                            question=user_message,
                            context=build_exam_context(marks_rows),
                        )
                        return {
                            "type": "text",
                            "message": answer,
                        }
                    # Don't return error - fallback to vector search

                # SPECIAL: Average marks calculation
                if "average" in user_message.lower() and ("mark" in user_message.lower() or "score" in user_message.lower()):
                    vector = get_embedding("all exam marks")
                    results = search_data_filtered(
                        vector=vector,
                        office_id=office_id,
                        user_role=user_role,
                        module="exam",
                        limit=50,
                    )
                    if results:
                        marks = []
                        for r in results:
                            text = r.payload.get("text", "")
                            # Extract marks from text like "Marks: 85 out of 100"
                            match = re.search(r'Marks:\s*(\d+)', text)
                            if match:
                                marks.append(int(match.group(1)))
                        if marks:
                            avg = sum(marks) / len(marks)
                            return {"type": "text", "message": f"Average marks: {avg:.1f} out of {len(marks)} records"}
                    return {"type": "text", "message": "No marks data found to calculate average."}

                # Handle aggregate queries (highest, lowest, average, all trainees)
                if is_aggregate_query(user_message):
                    vector = get_embedding(user_message)
                    
                    # Detect if user wants highest or lowest
                    msg_lower = user_message.lower()
                    wants_lowest = any(word in msg_lower for word in ["lowest", "least", "minimum", "min", "bottom", "worst"])
                    wants_highest = any(word in msg_lower for word in ["highest", "most", "maximum", "max", "top", "best"])
                    
                    # Determine sort order
                    if wants_lowest:
                        sort_order = "asc"  # Lowest first
                    else:
                        sort_order = "desc"  # Highest first (default)
                    
                    # Get records sorted by actual marks value
                    sorted_records = get_sorted_exam_records(
                        vector=vector,
                        office_id=office_id,
                        user_role=user_role,
                        sort_order=sort_order,
                        limit=50,
                    )

                    if sorted_records:
                        # Build context from sorted records (now properly ordered by marks!)
                        context = "\n\n".join(
                            [f"Marks: {r['marks']}\n{r['text']}" for r in sorted_records]
                        )
                        answer = generate_answer(
                            question=user_message,
                            context=context,
                        )
                        return {
                            "type": "text",
                            "message": answer,
                        }
                    return {
                        "type": "text",
                        "message": "I could not find exam data for your query.",
                    }

                # Handle generic exam queries - use vector search
                vector = get_embedding(user_message)
                results = search_data_filtered(
                    vector=vector,
                    office_id=office_id,
                    user_role=user_role,
                    module="exam",
                    limit=100,
                )

                if results:
                    context = "\n".join([r.payload.get("text", "") for r in results if r.payload])
                    answer = generate_answer(question=user_message, context=context)
                    return {"type": "text", "message": answer}
                
                return {"type": "text", "message": "No exam data found for your query."}

            if is_hostel_question(user_message):
                if not has_module_access(user_role, "hostel"):
                    return {
                        "type": "text",
                        "message": "You do not have permission to access hostel data.",
                    }

                msg_lower = user_message.lower()

                # SPECIAL: How many wards/buildings
                if any(kw in msg_lower for kw in ["how many ward", "number of ward", "total ward", "count ward"]):
                    vector = get_embedding("hostel buildings")
                    results = search_data_filtered(
                        vector=vector,
                        office_id=office_id,
                        user_role=user_role,
                        module="hostel",
                        limit=20,
                    )
                    if results:
                        # Count unique buildings
                        buildings = set()
                        for r in results:
                            text = r.payload.get("text", "")
                            if "HOSTEL BUILDING" in text or "Building:" in text:
                                # Extract building name
                                match = re.search(r'Building(?:\s*ID)?:\s*(\d+|\w+)', text)
                                if match:
                                    buildings.add(match.group(1))
                        return {"type": "text", "message": f"Total hostel wards/buildings: {len(buildings)}"}
                    return {"type": "text", "message": "No building data found."}

                # SPECIAL: Most occupied room
                if any(kw in msg_lower for kw in ["most occupied", "highest occupancy", "fullest room"]):
                    vector = get_embedding("hostel rooms occupied beds")
                    results = search_data_filtered(
                        vector=vector,
                        office_id=office_id,
                        user_role=user_role,
                        module="hostel",
                        limit=50,
                    )
                    if results:
                        max_occupied = 0
                        max_room = None
                        for r in results:
                            text = r.payload.get("text", "")
                            # Look for "Occupied: X" pattern
                            occ_match = re.search(r'Occupied:\s*(\d+)', text)
                            room_match = re.search(r'Room Name/Number:\s*(\S+)', text)
                            if occ_match and room_match:
                                occ = int(occ_match.group(1))
                                if occ > max_occupied:
                                    max_occupied = occ
                                    max_room = room_match.group(1)
                        if max_room:
                            return {"type": "text", "message": f"Most occupied room: {max_room} with {max_occupied} occupants"}
                    return {"type": "text", "message": "No occupancy data found."}

                # Search specifically in hostel module
                vector = get_embedding(user_message)
                results = search_data_filtered(
                    vector=vector,
                    office_id=office_id,
                    user_role=user_role,
                    module="hostel",
                    limit=20,
                )

                if results:
                    context = "\n".join(
                        [result.payload.get("text", "") for result in results if result.payload]
                    )
                    answer = generate_answer(
                        question=user_message,
                        context=context,
                    )
                    return {
                        "type": "text",
                        "message": answer,
                    }

                return {
                    "type": "text",
                    "message": "I could not find hostel data for your query.",
                }

            if is_attendance_question(user_message):
                if not has_module_access(user_role, "attendance"):
                    return {
                        "type": "text",
                        "message": "You do not have permission to access attendance data.",
                    }

                # Search specifically in attendance module
                vector = get_embedding(user_message)
                results = search_data_filtered(
                    vector=vector,
                    office_id=office_id,
                    user_role=user_role,
                    module="attendance",
                    limit=100,
                )

                if results:
                    context = "\n".join(
                        [result.payload.get("text", "") for result in results if result.payload]
                    )
                    answer = generate_answer(
                        question=user_message,
                        context=context,
                    )
                    return {
                        "type": "text",
                        "message": answer,
                    }

                return {
                    "type": "text",
                    "message": "I could not find attendance data for your query.",
                }

            vector = get_embedding(user_message)
            results = search_data_filtered(
                vector=vector,
                office_id=office_id,
                user_role=user_role,
                limit=100,
            )

            if results:
                context = "\n".join(
                    [result.payload.get("text", "") for result in results if result.payload]
                )
                answer = generate_answer(
                    question=user_message,
                    context=context,
                )
                return {
                    "type": "text",
                    "message": answer,
                }

            if not (
                is_exam_question(user_message)
                or is_hostel_question(user_message)
                or is_attendance_question(user_message)
            ):
                answer = generate_answer(question=user_message, context="")
                return {
                    "type": "text",
                    "message": answer,
                }

            return {
                "type": "text",
                "message": "I could not find permitted data for your role.",
            }

        # CHART AND DASHBOARD DISABLED - forcing text responses
        # if intent == "dashboard":
        #     return {"type": "dashboard", "message": "Dashboard request detected"}
        # if intent == "chart":
        #     return {"type": "chart", "message": "Chart request detected"}

        return {
            "type": "text",
            "message": "I could not understand the request.",
        }
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Chat processing failed: {exc}")