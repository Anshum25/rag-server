"""Pass and EQ module query templates."""

TEMPLATES = [
    {
        "id": "PASS_EQ_TOTAL_PASS",
        "module": "pass_eq",
        "description": "Total pass requests",
        "example_questions": ["Total pass requests?", "How many pass applications?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "PASS_EQ_PENDING",
        "module": "pass_eq",
        "description": "Pending pass",
        "example_questions": ["Pending pass?", "Awaiting approval?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "medium"
    },
    {
        "id": "PASS_EQ_APPROVED",
        "module": "pass_eq",
        "description": "Approved pass",
        "example_questions": ["Approved pass?", "Granted passes?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "PASS_EQ_BY_USER",
        "module": "pass_eq",
        "description": "Pass by user",
        "example_questions": ["Pass by user?", "User's pass history?"],
        "required_params": [],
        "optional_params": ["user_id", "user_name", "office_id"],
        "allowed_roles": ["principal", "admin", "staff", "trainee"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "PASS_EQ_BY_YEAR",
        "module": "pass_eq",
        "description": "Pass by year",
        "example_questions": ["Pass by year?", "Year-wise pass?"],
        "required_params": [],
        "optional_params": ["year", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "PASS_EQ_TYPE_SUMMARY",
        "module": "pass_eq",
        "description": "Pass type summary",
        "example_questions": ["Pass type summary?", "By pass type?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "PASS_EQ_TOTAL_EQ",
        "module": "pass_eq",
        "description": "EQ requests",
        "example_questions": ["Total EQ?", "How many EQ requests?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "PASS_EQ_BY_JOURNEY_DATE",
        "module": "pass_eq",
        "description": "EQ by journey date",
        "example_questions": ["EQ by journey date?", "Journey-wise EQ?"],
        "required_params": [],
        "optional_params": ["journey_date", "from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "PASS_EQ_TICKET_STATUS",
        "module": "pass_eq",
        "description": "EQ ticket status",
        "example_questions": ["EQ ticket status?", "Ticket confirmed?"],
        "required_params": [],
        "optional_params": ["eq_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff", "trainee"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "PASS_EQ_TRAIN_CLASS_SUMMARY",
        "module": "pass_eq",
        "description": "Train class summary",
        "example_questions": ["Train class summary?", "Class-wise pass?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "PASS_EQ_STATION_SUMMARY",
        "module": "pass_eq",
        "description": "Station/from-to summary",
        "example_questions": ["Station summary?", "Route-wise pass?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "PASS_EQ_PNR_SEARCH",
        "module": "pass_eq",
        "description": "PNR search",
        "example_questions": ["Search PNR?", "Find by PNR?"],
        "required_params": [],
        "optional_params": ["pnr_number", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "medium"
    },
    {
        "id": "PASS_EQ_PASSENGER_LIST",
        "module": "pass_eq",
        "description": "Passenger list",
        "example_questions": ["Passenger list?", "Who is traveling?"],
        "required_params": [],
        "optional_params": ["pass_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "PASS_EQ_ISSUE_DATE_SUMMARY",
        "module": "pass_eq",
        "description": "Pass issue date summary",
        "example_questions": ["Issue date summary?", "When issued?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "PASS_EQ_STATUS_SUMMARY",
        "module": "pass_eq",
        "description": "Pass status summary",
        "example_questions": ["Pass status?", "Approval status?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "PASS_EQ_EQ_STATUS_SUMMARY",
        "module": "pass_eq",
        "description": "EQ status summary",
        "example_questions": ["EQ status?", "EQ approval status?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "PASS_EQ_REMARKS",
        "module": "pass_eq",
        "description": "Pass remarks",
        "example_questions": ["Pass remarks?", "Comments on pass?"],
        "required_params": [],
        "optional_params": ["pass_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "PASS_EQ_RETURN_ROUTE",
        "module": "pass_eq",
        "description": "Pass return route",
        "example_questions": ["Return route?", "Return journey?"],
        "required_params": [],
        "optional_params": ["pass_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "PASS_EQ_BY_COURSE",
        "module": "pass_eq",
        "description": "Pass/EQ by course",
        "example_questions": ["Pass by course?", "Course-wise EQ?"],
        "required_params": [],
        "optional_params": ["course_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "PASS_EQ_MODULE_SUMMARY",
        "module": "pass_eq",
        "description": "Pass/EQ module summary",
        "example_questions": ["Pass/EQ summary?", "Pass EQ module overview?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "summary",
        "security_level": "low"
    }
]


def execute(query_id, params, cur, office_id):
    """Execute pass EQ queries."""
    p = params or {}
    
    if query_id == "PASS_EQ_TOTAL_PASS":
        cur.execute("SELECT COUNT(*) AS total FROM pass p JOIN users u ON u.id = p.user_id WHERE u.office_id = %s", (office_id,))
        r = cur.fetchone()
        return f"Total pass requests: {r['total'] if r else 0}"
    
    return None
