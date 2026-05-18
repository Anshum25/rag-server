"""Seminar module query templates."""

TEMPLATES = [
    {
        "id": "SEMINAR_TOTAL",
        "module": "seminar",
        "description": "Total seminars",
        "example_questions": ["Total seminars?", "How many seminars?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "SEMINAR_UPCOMING",
        "module": "seminar",
        "description": "Upcoming seminars",
        "example_questions": ["Upcoming seminars?", "Future seminars?"],
        "required_params": [],
        "optional_params": ["office_id", "limit"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SEMINAR_COMPLETED",
        "module": "seminar",
        "description": "Completed seminars",
        "example_questions": ["Completed seminars?", "Past seminars?"],
        "required_params": [],
        "optional_params": ["office_id", "from_date"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SEMINAR_BY_DATE",
        "module": "seminar",
        "description": "Seminar by date",
        "example_questions": ["Seminars on date?", "Date-wise seminars?"],
        "required_params": [],
        "optional_params": ["date", "from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SEMINAR_BY_TOPIC",
        "module": "seminar",
        "description": "Seminar by topic",
        "example_questions": ["Seminars by topic?", "Topic-wise seminars?"],
        "required_params": [],
        "optional_params": ["topic_id", "topic_name", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SEMINAR_BY_SPEAKER",
        "module": "seminar",
        "description": "Seminar by main speaker",
        "example_questions": ["Seminars by speaker?", "Speaker-wise seminars?"],
        "required_params": [],
        "optional_params": ["speaker_id", "speaker_name", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SEMINAR_BY_JUDGE",
        "module": "seminar",
        "description": "Seminar by judge",
        "example_questions": ["Seminars by judge?", "Judge-wise seminars?"],
        "required_params": [],
        "optional_params": ["judge_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SEMINAR_TOPIC_LIST",
        "module": "seminar",
        "description": "Seminar topic list",
        "example_questions": ["Seminar topics?", "List topics?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SEMINAR_DURATION",
        "module": "seminar",
        "description": "Seminar duration",
        "example_questions": ["Seminar duration?", "How long was seminar?"],
        "required_params": [],
        "optional_params": ["seminar_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "SEMINAR_BY_TYPE",
        "module": "seminar",
        "description": "Seminar by type",
        "example_questions": ["Seminars by type?", "Type-wise seminars?"],
        "required_params": [],
        "optional_params": ["type_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SEMINAR_BY_VL",
        "module": "seminar",
        "description": "Seminar by VL",
        "example_questions": ["VL seminars?", "Seminars by visiting lecturer?"],
        "required_params": [],
        "optional_params": ["vl_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SEMINAR_MONTHLY_COUNT",
        "module": "seminar",
        "description": "Monthly seminar count",
        "example_questions": ["Monthly seminars?", "Seminars this month?"],
        "required_params": [],
        "optional_params": ["month", "year", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "SEMINAR_ATTENDANCE",
        "module": "seminar",
        "description": "Seminar attendance",
        "example_questions": ["Seminar attendance?", "Who attended seminar?"],
        "required_params": [],
        "optional_params": ["seminar_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SEMINAR_REMARKS",
        "module": "seminar",
        "description": "Seminar remarks",
        "example_questions": ["Seminar remarks?", "Feedback on seminar?"],
        "required_params": [],
        "optional_params": ["seminar_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SEMINAR_STATUS_SUMMARY",
        "module": "seminar",
        "description": "Seminar status summary",
        "example_questions": ["Seminar status?", "Status summary?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "SEMINAR_SUBJECT_SUMMARY",
        "module": "seminar",
        "description": "Seminar subject summary",
        "example_questions": ["Subject-wise seminar?", "Seminar by subject?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "SEMINAR_TOPIC_SUMMARY",
        "module": "seminar",
        "description": "Seminar topic summary",
        "example_questions": ["Topic-wise seminar?", "Seminar topics count?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "SEMINAR_OFFICE_SUMMARY",
        "module": "seminar",
        "description": "Seminar office summary",
        "example_questions": ["Office seminar summary?", "Office-wise seminars?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "SEMINAR_DATE_RANGE",
        "module": "seminar",
        "description": "Seminar date range",
        "example_questions": ["Seminars in range?", "Date range seminars?"],
        "required_params": [],
        "optional_params": ["from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SEMINAR_MODULE_SUMMARY",
        "module": "seminar",
        "description": "Seminar module summary",
        "example_questions": ["Seminar summary?", "Seminar module overview?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "summary",
        "security_level": "low"
    }
]


def execute(query_id, params, cur, office_id):
    """Execute seminar queries."""
    p = params or {}
    
    if query_id == "SEMINAR_TOTAL":
        cur.execute("SELECT COUNT(*) AS total FROM seminars s JOIN users u ON u.id = s.type_id WHERE u.office_id = %s", (office_id,))
        r = cur.fetchone()
        return f"Total seminars: {r['total'] if r else 0}"
    
    return None
