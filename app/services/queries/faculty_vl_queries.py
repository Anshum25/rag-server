"""Faculty and Visiting Lecturer module query templates."""

TEMPLATES = [
    {
        "id": "FACULTY_VL_TOTAL",
        "module": "faculty_vl",
        "description": "Total visiting lecturers",
        "example_questions": ["Total visiting lecturers?", "How many VLs?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "FACULTY_VL_BY_DATE",
        "module": "faculty_vl",
        "description": "VL by date",
        "example_questions": ["VL on date?", "Visiting lecturer schedule?"],
        "required_params": [],
        "optional_params": ["date", "from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FACULTY_VL_BY_SUBJECT",
        "module": "faculty_vl",
        "description": "VL by subject",
        "example_questions": ["VL by subject?", "Subject-wise VL?"],
        "required_params": [],
        "optional_params": ["subject_name", "subject_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FACULTY_VL_BY_COURSE",
        "module": "faculty_vl",
        "description": "VL by course",
        "example_questions": ["VL by course?", "Course-wise visiting lecturers?"],
        "required_params": [],
        "optional_params": ["course_id", "course_name", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FACULTY_VL_LECTURE_COUNT",
        "module": "faculty_vl",
        "description": "VL lecture count",
        "example_questions": ["VL lecture count?", "How many VL lectures?"],
        "required_params": [],
        "optional_params": ["vl_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "FACULTY_VL_PAYMENT",
        "module": "faculty_vl",
        "description": "VL payment/price summary",
        "example_questions": ["VL payments?", "Visiting lecturer fees?"],
        "required_params": [],
        "optional_params": ["vl_id", "from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "summary",
        "security_level": "medium"
    },
    {
        "id": "FACULTY_LECTURE_SCHEDULE",
        "module": "faculty_vl",
        "description": "Faculty lecture schedule",
        "example_questions": ["Faculty schedule?", "Lecture schedule?"],
        "required_params": [],
        "optional_params": ["faculty_id", "from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FACULTY_BY_DEPARTMENT",
        "module": "faculty_vl",
        "description": "Faculty by department",
        "example_questions": ["Faculty by department?", "Dept-wise faculty?"],
        "required_params": [],
        "optional_params": ["department_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FACULTY_BY_DESIGNATION",
        "module": "faculty_vl",
        "description": "Faculty by designation",
        "example_questions": ["Faculty by designation?", "Designation-wise faculty?"],
        "required_params": [],
        "optional_params": ["designation_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FACULTY_ASSIGNED_COURSE",
        "module": "faculty_vl",
        "description": "Faculty assigned to course",
        "example_questions": ["Faculty assigned to course?", "Course faculty?"],
        "required_params": [],
        "optional_params": ["course_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FACULTY_VL_TOP",
        "module": "faculty_vl",
        "description": "Top VL by lectures",
        "example_questions": ["Top visiting lecturers?", "Most active VL?"],
        "required_params": [],
        "optional_params": ["office_id", "limit"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "ranking",
        "security_level": "low"
    },
    {
        "id": "FACULTY_VL_FEEDBACK",
        "module": "faculty_vl",
        "description": "VL feedback summary",
        "example_questions": ["VL feedback?", "Visiting lecturer ratings?"],
        "required_params": [],
        "optional_params": ["vl_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "FACULTY_VL_DATE_RANGE",
        "module": "faculty_vl",
        "description": "VL date range",
        "example_questions": ["VL in date range?", "Visiting lecturers between dates?"],
        "required_params": [],
        "optional_params": ["from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FACULTY_VL_SUBJECT_SUMMARY",
        "module": "faculty_vl",
        "description": "VL subject-wise summary",
        "example_questions": ["VL subject summary?", "Subject-wise VL count?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "FACULTY_VL_COURSE_SUMMARY",
        "module": "faculty_vl",
        "description": "VL course-wise summary",
        "example_questions": ["VL course summary?", "Course-wise VL count?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "FACULTY_AVAILABILITY",
        "module": "faculty_vl",
        "description": "Faculty availability",
        "example_questions": ["Faculty availability?", "When is faculty free?"],
        "required_params": [],
        "optional_params": ["faculty_id", "date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FACULTY_VL_DAILY",
        "module": "faculty_vl",
        "description": "Daily VL schedule",
        "example_questions": ["Daily VL schedule?", "Today's VL?"],
        "required_params": [],
        "optional_params": ["date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FACULTY_VL_UPCOMING",
        "module": "faculty_vl",
        "description": "Upcoming VL lectures",
        "example_questions": ["Upcoming VL?", "Next VL sessions?"],
        "required_params": [],
        "optional_params": ["office_id", "limit"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FACULTY_VL_COMPLETED",
        "module": "faculty_vl",
        "description": "Completed VL lectures",
        "example_questions": ["Completed VL?", "Past VL sessions?"],
        "required_params": [],
        "optional_params": ["office_id", "from_date"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FACULTY_VL_MODULE_SUMMARY",
        "module": "faculty_vl",
        "description": "Faculty/VL module summary",
        "example_questions": ["Faculty summary?", "VL module overview?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "summary",
        "security_level": "low"
    }
]


def execute(query_id, params, cur, office_id):
    """Execute faculty VL queries."""
    p = params or {}
    
    if query_id == "FACULTY_VL_TOTAL":
        cur.execute("SELECT COUNT(*) AS total FROM vl_management WHERE office_id = %s", (office_id,))
        r = cur.fetchone()
        return f"Total visiting lecturers: {r['total'] if r else 0}"
    
    return None
