"""Timetable module query templates."""

TEMPLATES = [
    {
        "id": "TIMETABLE_TODAY",
        "module": "timetable",
        "description": "Today's timetable",
        "example_questions": ["Today's timetable?", "What lectures today?"],
        "required_params": [],
        "optional_params": ["office_id", "course_id"],
        "allowed_roles": ["principal", "admin", "staff", "trainee"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "TIMETABLE_TOMORROW",
        "module": "timetable",
        "description": "Tomorrow's timetable",
        "example_questions": ["Tomorrow's timetable?", "What lectures tomorrow?"],
        "required_params": [],
        "optional_params": ["office_id", "course_id"],
        "allowed_roles": ["principal", "admin", "staff", "trainee"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "TIMETABLE_WEEKLY",
        "module": "timetable",
        "description": "Weekly timetable",
        "example_questions": ["Weekly timetable?", "This week lectures?"],
        "required_params": [],
        "optional_params": ["office_id", "course_id", "week_start"],
        "allowed_roles": ["principal", "admin", "staff", "trainee"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "TIMETABLE_COURSE",
        "module": "timetable",
        "description": "Course timetable",
        "example_questions": ["Course timetable?", "Batch timetable?"],
        "required_params": [],
        "optional_params": ["course_id", "course_name", "office_id"],
        "allowed_roles": ["principal", "admin", "staff", "trainee"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "TIMETABLE_BATCH",
        "module": "timetable",
        "description": "Batch timetable",
        "example_questions": ["Batch timetable?", "Specific batch schedule?"],
        "required_params": [],
        "optional_params": ["batch_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff", "trainee"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "TIMETABLE_SUBJECT_WISE",
        "module": "timetable",
        "description": "Subject-wise timetable",
        "example_questions": ["Subject-wise timetable?", "Lectures for subject?"],
        "required_params": [],
        "optional_params": ["subject_id", "subject_name", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "TIMETABLE_FACULTY_WISE",
        "module": "timetable",
        "description": "Faculty-wise timetable",
        "example_questions": ["Faculty timetable?", "Teacher's schedule?"],
        "required_params": [],
        "optional_params": ["faculty_id", "faculty_name", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "TIMETABLE_CLASSROOM",
        "module": "timetable",
        "description": "Classroom timetable",
        "example_questions": ["Classroom schedule?", "Room booking?"],
        "required_params": [],
        "optional_params": ["classroom_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "TIMETABLE_SESSION",
        "module": "timetable",
        "description": "Session-wise timetable",
        "example_questions": ["Session timetable?", "Period schedule?"],
        "required_params": [],
        "optional_params": ["session_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "TIMETABLE_TOPIC",
        "module": "timetable",
        "description": "Topic-wise timetable",
        "example_questions": ["Topic schedule?", "When is topic covered?"],
        "required_params": [],
        "optional_params": ["topic_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "TIMETABLE_BY_DATE",
        "module": "timetable",
        "description": "Timetable by date",
        "example_questions": ["Timetable on date?", "Schedule for date?"],
        "required_params": [],
        "optional_params": ["date", "office_id", "course_id"],
        "allowed_roles": ["principal", "admin", "staff", "trainee"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "TIMETABLE_UPCOMING",
        "module": "timetable",
        "description": "Upcoming lectures",
        "example_questions": ["Upcoming lectures?", "Next lectures?"],
        "required_params": [],
        "optional_params": ["office_id", "course_id", "limit"],
        "allowed_roles": ["principal", "admin", "staff", "trainee"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "TIMETABLE_COMPLETED",
        "module": "timetable",
        "description": "Completed lectures",
        "example_questions": ["Completed lectures?", "Past lectures?"],
        "required_params": [],
        "optional_params": ["office_id", "course_id", "from_date"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "TIMETABLE_VL",
        "module": "timetable",
        "description": "VL lectures",
        "example_questions": ["VL lectures?", "Visiting lecturer schedule?"],
        "required_params": [],
        "optional_params": ["vl_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "TIMETABLE_DEPT_WISE",
        "module": "timetable",
        "description": "Department-wise timetable",
        "example_questions": ["Department timetable?", "Dept schedule?"],
        "required_params": [],
        "optional_params": ["department_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "TIMETABLE_COUNT",
        "module": "timetable",
        "description": "Timetable count",
        "example_questions": ["Total timetable entries?", "How many lectures?"],
        "required_params": [],
        "optional_params": ["office_id", "course_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "TIMETABLE_HOURS_SUMMARY",
        "module": "timetable",
        "description": "Timetable hours summary",
        "example_questions": ["Total lecture hours?", "Hours per subject?"],
        "required_params": [],
        "optional_params": ["office_id", "course_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "TIMETABLE_COURSE_PLAN",
        "module": "timetable",
        "description": "Course lecture plan",
        "example_questions": ["Course plan?", "Lecture plan?"],
        "required_params": [],
        "optional_params": ["course_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "TIMETABLE_MODULE_SUMMARY",
        "module": "timetable",
        "description": "Timetable module summary",
        "example_questions": ["Timetable summary?", "Timetable overview?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "summary",
        "security_level": "low"
    }
]


def execute(query_id, params, cur, office_id):
    """Execute timetable queries."""
    p = params or {}
    
    if query_id == "TIMETABLE_TODAY":
        cur.execute("""
            SELECT tt.*, c.course_name 
            FROM tt_designs tt 
            JOIN training_calendars tc ON tc.id = tt.course_id 
            JOIN courses c ON c.id = tc.ct_id 
            WHERE tc.office_id = %s 
            LIMIT 50
        """, (office_id,))
        rows = cur.fetchall()
        if not rows:
            return "No timetable entries found for today."
        lines = [f"- {r.get('course_name', 'Unknown')}" for r in rows[:10]]
        return f"Timetable entries found:\n" + "\n".join(lines)
    
    return None
