"""Smart query service - dispatches to module-specific query handlers."""
import traceback
from typing import Any, Dict
from app.services.db_service import get_connection
from app.services.queries import exam_queries, hostel_queries, trainee_queries

# Aggregate all templates from module files
QUERY_TEMPLATES = (
    exam_queries.TEMPLATES +
    hostel_queries.TEMPLATES +
    trainee_queries.TEMPLATES
)

# Ordered list of module handlers to try
_MODULE_HANDLERS = [exam_queries, hostel_queries, trainee_queries]


def get_relevant_templates(question: str) -> list:
    """Filter templates based on keywords to avoid exceeding LLM context limits."""
    text = question.lower()
    exam_words = {"exam", "marks", "mark", "result", "pass", "fail", "score", "grade", "subject", "percentage", "top", "bottom", "lowest", "highest", "performers"}
    hostel_words = {"hostel", "room", "bed", "building", "warden", "allocation", "checkin", "checkout", "occupancy", "vacant", "complaint", "feedback"}
    trainee_words = {"trainee", "student", "attendance", "present", "absent", "leave", "course", "department", "designation", "calendar", "batch", "nominee", "linen", "field"}
    
    active_templates = []
    if any(w in text for w in exam_words):
        active_templates.extend(exam_queries.TEMPLATES)
    if any(w in text for w in hostel_words):
        active_templates.extend(hostel_queries.TEMPLATES)
    if any(w in text for w in trainee_words):
        active_templates.extend(trainee_queries.TEMPLATES)
        
    if not active_templates:
        return QUERY_TEMPLATES
        
    return active_templates


def execute_smart_query(query_id: str, params: Dict[str, Any], office_id: int) -> str:
    conn = get_connection()
    try:
        cur = conn.cursor()
        # Try each module handler in order
        for module in _MODULE_HANDLERS:
            result = module.execute(query_id, params or {}, cur, office_id)
            if result is not None:
                return result
        return None
    except Exception as e:
        print(f"Error executing smart query {query_id}: {traceback.format_exc()}")
        return f"Error processing request: {str(e)}"
    finally:
        conn.close()
