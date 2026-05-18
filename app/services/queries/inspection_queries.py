"""Inspection module query templates."""

TEMPLATES = [
    {
        "id": "INSPECTION_TOTAL",
        "module": "inspection",
        "description": "Total inspection notes",
        "example_questions": ["Total inspections?", "How many inspections?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "INSPECTION_BY_DATE",
        "module": "inspection",
        "description": "Inspection by date",
        "example_questions": ["Inspections on date?", "Date-wise inspections?"],
        "required_params": [],
        "optional_params": ["date", "from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "INSPECTION_DESCRIPTIONS",
        "module": "inspection",
        "description": "Inspection descriptions",
        "example_questions": ["Inspection descriptions?", "Inspection details?"],
        "required_params": [],
        "optional_params": ["inspection_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "INSPECTION_BY_FACULTY",
        "module": "inspection",
        "description": "Inspection by faculty/user",
        "example_questions": ["Inspections by faculty?", "Faculty inspections?"],
        "required_params": [],
        "optional_params": ["faculty_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "INSPECTION_STATUS_SUMMARY",
        "module": "inspection",
        "description": "Inspection status summary",
        "example_questions": ["Inspection status?", "Status summary?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "INSPECTION_PENDING",
        "module": "inspection",
        "description": "Pending inspections",
        "example_questions": ["Pending inspections?", "Awaiting inspection?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "INSPECTION_COMPLETED",
        "module": "inspection",
        "description": "Completed inspections",
        "example_questions": ["Completed inspections?", "Done inspections?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "INSPECTION_REMARKS",
        "module": "inspection",
        "description": "Inspection remarks",
        "example_questions": ["Inspection remarks?", "Comments on inspection?"],
        "required_params": [],
        "optional_params": ["inspection_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "INSPECTION_BY_OFFICE",
        "module": "inspection",
        "description": "Inspection by office",
        "example_questions": ["Office inspections?", "Office-wise inspections?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "INSPECTION_FILES",
        "module": "inspection",
        "description": "Inspection file uploads",
        "example_questions": ["Inspection files?", "Uploaded documents?"],
        "required_params": [],
        "optional_params": ["inspection_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "INSPECTION_BY_TYPE",
        "module": "inspection",
        "description": "Inspection by type",
        "example_questions": ["Inspections by type?", "Type-wise inspections?"],
        "required_params": [],
        "optional_params": ["type_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "INSPECTION_ACTION_NOTES",
        "module": "inspection",
        "description": "Inspection action notes",
        "example_questions": ["Action notes?", "Inspection actions?"],
        "required_params": [],
        "optional_params": ["inspection_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "INSPECTION_DATE_RANGE",
        "module": "inspection",
        "description": "Inspection date range",
        "example_questions": ["Inspections in range?", "Date range inspections?"],
        "required_params": [],
        "optional_params": ["from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "INSPECTION_MONTHLY_COUNT",
        "module": "inspection",
        "description": "Monthly inspection count",
        "example_questions": ["Monthly inspections?", "Inspections this month?"],
        "required_params": [],
        "optional_params": ["month", "year", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "INSPECTION_TITLE_SEARCH",
        "module": "inspection",
        "description": "Inspection title search",
        "example_questions": ["Find inspection by title?", "Search inspection?"],
        "required_params": [],
        "optional_params": ["title", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "INSPECTION_DESC_SEARCH",
        "module": "inspection",
        "description": "Inspection description search",
        "example_questions": ["Search inspection description?", "Find in inspection?"],
        "required_params": [],
        "optional_params": ["keyword", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "INSPECTION_COPY_TO_SUMMARY",
        "module": "inspection",
        "description": "Inspection copy_to summary",
        "example_questions": ["Inspection copies?", "Shared with whom?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "INSPECTION_DEPT_SUMMARY",
        "module": "inspection",
        "description": "Inspection department summary",
        "example_questions": ["Dept-wise inspections?", "Inspection by department?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "INSPECTION_LATEST",
        "module": "inspection",
        "description": "Inspection latest notes",
        "example_questions": ["Latest inspections?", "Recent inspections?"],
        "required_params": [],
        "optional_params": ["office_id", "limit"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "INSPECTION_MODULE_SUMMARY",
        "module": "inspection",
        "description": "Inspection module summary",
        "example_questions": ["Inspection summary?", "Inspection module overview?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "summary",
        "security_level": "low"
    }
]


def execute(query_id, params, cur, office_id):
    """Execute inspection queries."""
    p = params or {}
    
    if query_id == "INSPECTION_TOTAL":
        cur.execute("SELECT COUNT(*) AS total FROM inspection_notes WHERE office_id = %s", (office_id,))
        r = cur.fetchone()
        return f"Total inspection notes: {r['total'] if r else 0}"
    
    return None
