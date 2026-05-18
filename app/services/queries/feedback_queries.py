"""Feedback module query templates."""

TEMPLATES = [
    {
        "id": "FEEDBACK_TOTAL",
        "module": "feedback",
        "description": "Total feedback responses",
        "example_questions": ["Total feedback?", "How many feedback responses?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "FEEDBACK_BY_COURSE",
        "module": "feedback",
        "description": "Feedback by course",
        "example_questions": ["Feedback by course?", "Course-wise feedback?"],
        "required_params": [],
        "optional_params": ["course_id", "course_name", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FEEDBACK_BY_TRAINEE",
        "module": "feedback",
        "description": "Feedback by trainee/user",
        "example_questions": ["Feedback by trainee?", "User's feedback?"],
        "required_params": [],
        "optional_params": ["user_id", "user_name", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FEEDBACK_QUESTION_WISE",
        "module": "feedback",
        "description": "Question-wise feedback",
        "example_questions": ["Question-wise feedback?", "Feedback by question?"],
        "required_params": [],
        "optional_params": ["fq_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FEEDBACK_SECTION_WISE",
        "module": "feedback",
        "description": "Section-wise feedback",
        "example_questions": ["Section-wise feedback?", "Feedback by section?"],
        "required_params": [],
        "optional_params": ["fs_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FEEDBACK_AVERAGE_RATING",
        "module": "feedback",
        "description": "Average rating",
        "example_questions": ["Average rating?", "Overall feedback rating?"],
        "required_params": [],
        "optional_params": ["course_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "FEEDBACK_POSITIVE_NEGATIVE",
        "module": "feedback",
        "description": "Positive/negative feedback",
        "example_questions": ["Positive feedback?", "Negative feedback?"],
        "required_params": [],
        "optional_params": ["sentiment", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "FEEDBACK_PENDING_USERS",
        "module": "feedback",
        "description": "Feedback pending users",
        "example_questions": ["Who hasn't given feedback?", "Pending feedback users?"],
        "required_params": [],
        "optional_params": ["course_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FEEDBACK_SUBMITTED_USERS",
        "module": "feedback",
        "description": "Feedback submitted users",
        "example_questions": ["Who submitted feedback?", "Feedback submitted list?"],
        "required_params": [],
        "optional_params": ["course_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FEEDBACK_COURSE_CONTENT",
        "module": "feedback",
        "description": "Course content feedback",
        "example_questions": ["Course content feedback?", "Content rating?"],
        "required_params": [],
        "optional_params": ["course_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "FEEDBACK_FACILITY",
        "module": "feedback",
        "description": "Facility feedback",
        "example_questions": ["Facility feedback?", "Infrastructure feedback?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "FEEDBACK_VL",
        "module": "feedback",
        "description": "VL feedback",
        "example_questions": ["VL feedback?", "Visiting lecturer feedback?"],
        "required_params": [],
        "optional_params": ["vl_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "FEEDBACK_BY_YEAR",
        "module": "feedback",
        "description": "Feedback by year",
        "example_questions": ["Feedback by year?", "Annual feedback?"],
        "required_params": [],
        "optional_params": ["year", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "FEEDBACK_BY_MONTH",
        "module": "feedback",
        "description": "Feedback by month",
        "example_questions": ["Feedback by month?", "Monthly feedback?"],
        "required_params": [],
        "optional_params": ["month", "year", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "FEEDBACK_COMMENTS",
        "module": "feedback",
        "description": "Feedback comments/list",
        "example_questions": ["Feedback comments?", "Show feedback text?"],
        "required_params": [],
        "optional_params": ["course_id", "office_id", "limit"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FEEDBACK_TOP_RATED",
        "module": "feedback",
        "description": "Top rated course",
        "example_questions": ["Top rated course?", "Best rated course?"],
        "required_params": [],
        "optional_params": ["office_id", "limit"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "ranking",
        "security_level": "low"
    },
    {
        "id": "FEEDBACK_LOW_RATED",
        "module": "feedback",
        "description": "Low rated course",
        "example_questions": ["Low rated course?", "Worst rated course?"],
        "required_params": [],
        "optional_params": ["office_id", "limit"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "ranking",
        "security_level": "low"
    },
    {
        "id": "FEEDBACK_RESPONSE_COUNT",
        "module": "feedback",
        "description": "Feedback response count",
        "example_questions": ["Feedback response count?", "Total responses?"],
        "required_params": [],
        "optional_params": ["course_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "FEEDBACK_SUMMARY_BY_QUESTION",
        "module": "feedback",
        "description": "Feedback summary by question",
        "example_questions": ["Question summary?", "Feedback stats by question?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "FEEDBACK_MODULE_SUMMARY",
        "module": "feedback",
        "description": "Feedback module summary",
        "example_questions": ["Feedback summary?", "Feedback module overview?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "summary",
        "security_level": "low"
    }
]


def execute(query_id, params, cur, office_id):
    """Execute feedback queries."""
    p = params or {}
    
    if query_id == "FEEDBACK_TOTAL":
        cur.execute("SELECT COUNT(*) AS total FROM feed_master fm JOIN users u ON u.id = fm.user_id WHERE u.office_id = %s", (office_id,))
        r = cur.fetchone()
        return f"Total feedback responses: {r['total'] if r else 0}"
    
    return None
