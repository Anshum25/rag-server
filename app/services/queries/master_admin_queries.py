"""Master Admin module query templates."""

TEMPLATES = [
    {
        "id": "MASTER_TOTAL_USERS",
        "module": "master_admin",
        "description": "Total users",
        "example_questions": ["Total users?", "How many users?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "super_admin"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "MASTER_TOTAL_ROLES",
        "module": "master_admin",
        "description": "Total roles",
        "example_questions": ["Total roles?", "How many roles?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "super_admin"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "MASTER_ROLE_WISE_USERS",
        "module": "master_admin",
        "description": "Role-wise users",
        "example_questions": ["Role-wise users?", "Users by role?"],
        "required_params": [],
        "optional_params": ["role_id", "office_id"],
        "allowed_roles": ["principal", "admin", "super_admin"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MASTER_PERMISSION_LIST",
        "module": "master_admin",
        "description": "Permission list",
        "example_questions": ["List permissions?", "What permissions?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "super_admin"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MASTER_USER_ACCESS_LIST",
        "module": "master_admin",
        "description": "User access list",
        "example_questions": ["User access?", "Who has access?"],
        "required_params": [],
        "optional_params": ["user_id", "office_id"],
        "allowed_roles": ["principal", "admin", "super_admin"],
        "result_type": "list",
        "security_level": "medium"
    },
    {
        "id": "MASTER_DEPARTMENTS_LIST",
        "module": "master_admin",
        "description": "Departments list",
        "example_questions": ["List departments?", "What departments?"],
        "required_params": [],
        "optional_params": ["office_id", "service_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MASTER_DESIGNATIONS_LIST",
        "module": "master_admin",
        "description": "Designations list",
        "example_questions": ["List designations?", "What designations?"],
        "required_params": [],
        "optional_params": ["office_id", "grade_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MASTER_GRADES_LIST",
        "module": "master_admin",
        "description": "Grades list",
        "example_questions": ["List grades?", "What grades?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MASTER_SERVICES_LIST",
        "module": "master_admin",
        "description": "Services list",
        "example_questions": ["List services?", "What services?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MASTER_ZONES_LIST",
        "module": "master_admin",
        "description": "Zones list",
        "example_questions": ["List zones?", "What zones?"],
        "required_params": [],
        "optional_params": [],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MASTER_DIVISIONS_LIST",
        "module": "master_admin",
        "description": "Divisions list",
        "example_questions": ["List divisions?", "What divisions?"],
        "required_params": [],
        "optional_params": ["zone_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MASTER_DEPOTS_LIST",
        "module": "master_admin",
        "description": "Depots list",
        "example_questions": ["List depots?", "What depots?"],
        "required_params": [],
        "optional_params": ["division_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MASTER_RAIL_STATIONS_LIST",
        "module": "master_admin",
        "description": "Rail stations list",
        "example_questions": ["List stations?", "Rail stations?"],
        "required_params": [],
        "optional_params": [],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MASTER_HOLIDAYS_LIST",
        "module": "master_admin",
        "description": "Holidays list",
        "example_questions": ["List holidays?", "What holidays?"],
        "required_params": [],
        "optional_params": ["office_id", "year"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MASTER_BANKS_LIST",
        "module": "master_admin",
        "description": "Banks list",
        "example_questions": ["List banks?", "What banks?"],
        "required_params": [],
        "optional_params": [],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MASTER_COMPANIES_LIST",
        "module": "master_admin",
        "description": "Companies list",
        "example_questions": ["List companies?", "What companies?"],
        "required_params": [],
        "optional_params": [],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MASTER_PLACES_LIST",
        "module": "master_admin",
        "description": "Places list",
        "example_questions": ["List places?", "What places?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MASTER_ACTIVE_USERS",
        "module": "master_admin",
        "description": "Active users",
        "example_questions": ["Active users?", "How many active?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "super_admin"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "MASTER_INACTIVE_USERS",
        "module": "master_admin",
        "description": "Inactive users",
        "example_questions": ["Inactive users?", "How many inactive?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "super_admin"],
        "result_type": "count",
        "security_level": "medium"
    },
    {
        "id": "MASTER_MODULE_SUMMARY",
        "module": "master_admin",
        "description": "Master admin summary",
        "example_questions": ["Master admin summary?", "Master overview?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "super_admin"],
        "result_type": "summary",
        "security_level": "low"
    }
]


def execute(query_id, params, cur, office_id):
    """Execute master admin queries."""
    p = params or {}
    
    if query_id == "MASTER_TOTAL_USERS":
        cur.execute("SELECT COUNT(*) AS total FROM users WHERE office_id = %s", (office_id,))
        r = cur.fetchone()
        return f"Total users: {r['total'] if r else 0}"
    
    return None
