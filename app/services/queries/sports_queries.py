"""Sports module query templates."""

TEMPLATES = [
    
    {
        "id": "SPORTS_UPCOMING",
        "module": "sports",
        "description": "Upcoming sports",
        "example_questions": ["Upcoming sports?", "Future sports events?"],
        "required_params": [],
        "optional_params": ["office_id", "limit"],
        "allowed_roles": ["principal", "admin", "staff", "trainee"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SPORTS_COMPLETED",
        "module": "sports",
        "description": "Completed sports",
        "example_questions": ["Completed sports?", "Past sports events?"],
        "required_params": [],
        "optional_params": ["office_id", "from_date"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SPORTS_TEAMS",
        "module": "sports",
        "description": "Sports teams",
        "example_questions": ["Sports teams?", "How many teams?"],
        "required_params": [],
        "optional_params": ["program_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff", "sports_coordinator"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SPORTS_PARTICIPANTS_COUNT",
        "module": "sports",
        "description": "Participants count",
        "example_questions": ["Sports participants?", "How many participants?"],
        "required_params": [],
        "optional_params": ["program_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "SPORTS_ITEM_LIST",
        "module": "sports",
        "description": "Sport item list",
        "example_questions": ["Sports items?", "Equipment list?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff", "sports_coordinator"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SPORTS_ITEM_ISSUED",
        "module": "sports",
        "description": "Issued sport items",
        "example_questions": ["Issued items?", "Equipment issued?"],
        "required_params": [],
        "optional_params": ["office_id", "user_id"],
        "allowed_roles": ["principal", "admin", "staff", "sports_coordinator"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SPORTS_MATERIAL_PURCHASE",
        "module": "sports",
        "description": "Sport material purchase",
        "example_questions": ["Material purchases?", "Sports items bought?"],
        "required_params": [],
        "optional_params": ["office_id", "from_date", "to_date"],
        "allowed_roles": ["principal", "admin", "sports_coordinator"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SPORTS_PHOTOS",
        "module": "sports",
        "description": "Sports photos",
        "example_questions": ["Sports photos?", "Event pictures?"],
        "required_params": [],
        "optional_params": ["sport_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff", "trainee"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SPORTS_TEAM_SUMMARY",
        "module": "sports",
        "description": "Sport team summary",
        "example_questions": ["Team summary?", "Team-wise stats?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "SPORTS_ITEM_STOCK",
        "module": "sports",
        "description": "Sport item stock",
        "example_questions": ["Item stock?", "Equipment available?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "sports_coordinator"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "SPORTS_PAYMENT",
        "module": "sports",
        "description": "Sport payment/receipt",
        "example_questions": ["Sports payments?", "Sports receipts?"],
        "required_params": [],
        "optional_params": ["office_id", "from_date", "to_date"],
        "allowed_roles": ["principal", "admin", "sports_coordinator"],
        "result_type": "summary",
        "security_level": "medium"
    },
    {
        "id": "SPORTS_BY_DATE",
        "module": "sports",
        "description": "Sports by date",
        "example_questions": ["Sports on date?", "Date-wise sports?"],
        "required_params": [],
        "optional_params": ["date", "from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SPORTS_BY_COORDINATOR",
        "module": "sports",
        "description": "Coordinator-wise sports",
        "example_questions": ["Sports by coordinator?", "Coordinator events?"],
        "required_params": [],
        "optional_params": ["coordinator_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SPORTS_TEAM_PARTICIPANTS",
        "module": "sports",
        "description": "Team-wise participants",
        "example_questions": ["Team participants?", "Participants by team?"],
        "required_params": [],
        "optional_params": ["team_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SPORTS_MATERIAL_COST",
        "module": "sports",
        "description": "Material cost summary",
        "example_questions": ["Material costs?", "Sports expenditure?"],
        "required_params": [],
        "optional_params": ["office_id", "from_date", "to_date"],
        "allowed_roles": ["principal", "admin", "sports_coordinator"],
        "result_type": "summary",
        "security_level": "medium"
    },
    {
        "id": "SPORTS_ISSUE_FINE",
        "module": "sports",
        "description": "Sports issue fine",
        "example_questions": ["Sports fines?", "Equipment fines?"],
        "required_params": [],
        "optional_params": ["office_id", "user_id"],
        "allowed_roles": ["principal", "admin", "sports_coordinator"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "SPORTS_BY_COURSE",
        "module": "sports",
        "description": "Sports by course",
        "example_questions": ["Sports by course?", "Course-wise sports?"],
        "required_params": [],
        "optional_params": ["course_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "SPORTS_STATUS_SUMMARY",
        "module": "sports",
        "description": "Sports status summary",
        "example_questions": ["Sports status?", "Event status?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "SPORTS_MODULE_SUMMARY",
        "module": "sports",
        "description": "Sports module summary",
        "example_questions": ["Sports summary?", "Sports module overview?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "summary",
        "security_level": "low"
    }
]


def execute(query_id, params, cur, office_id):
    """Execute sports queries."""
    p = params or {}
    
    if query_id == "SPORTS_TOTAL_PROGRAMS":
        cur.execute("SELECT COUNT(*) AS total FROM sport s JOIN users u ON u.id = s.team WHERE u.office_id = %s", (office_id,))
        r = cur.fetchone()
        return f"Total sports programs: {r['total'] if r else 0}"
    
    return None
