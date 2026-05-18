"""Complaint module query templates."""

TEMPLATES = [
    {
        "id": "COMPLAINT_TOTAL",
        "module": "complaint",
        "description": "Total complaints",
        "example_questions": ["Total complaints?", "How many complaints?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "COMPLAINT_PENDING",
        "module": "complaint",
        "description": "Pending complaints",
        "example_questions": ["Pending complaints?", "Unsolved complaints?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "medium"
    },
    {
        "id": "COMPLAINT_COMPLETED",
        "module": "complaint",
        "description": "Completed/closed complaints",
        "example_questions": ["Completed complaints?", "Resolved complaints?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "COMPLAINT_BY_STATUS",
        "module": "complaint",
        "description": "Complaint by status",
        "example_questions": ["Complaints by status?", "Status-wise complaints?"],
        "required_params": [],
        "optional_params": ["status", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "COMPLAINT_BY_CATEGORY",
        "module": "complaint",
        "description": "Complaint by category",
        "example_questions": ["Complaints by category?", "Category-wise complaints?"],
        "required_params": [],
        "optional_params": ["category_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "COMPLAINT_BY_SUBCATEGORY",
        "module": "complaint",
        "description": "Complaint by subcategory",
        "example_questions": ["Complaints by subcategory?", "Subcategory-wise complaints?"],
        "required_params": [],
        "optional_params": ["subcategory_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "COMPLAINT_BY_USER",
        "module": "complaint",
        "description": "Complaint by user",
        "example_questions": ["Complaints by user?", "User's complaints?"],
        "required_params": [],
        "optional_params": ["user_id", "user_name", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "medium"
    },
    {
        "id": "COMPLAINT_BY_BUILDING",
        "module": "complaint",
        "description": "Complaint by building/hostel",
        "example_questions": ["Hostel complaints?", "Building-wise complaints?"],
        "required_params": [],
        "optional_params": ["building_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "COMPLAINT_BY_DATE",
        "module": "complaint",
        "description": "Complaint by date",
        "example_questions": ["Complaints on date?", "Today's complaints?"],
        "required_params": [],
        "optional_params": ["date", "from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "COMPLAINT_MONTHLY",
        "module": "complaint",
        "description": "Monthly complaints",
        "example_questions": ["Monthly complaints?", "This month complaints?"],
        "required_params": [],
        "optional_params": ["month", "year", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "COMPLAINT_RATING",
        "module": "complaint",
        "description": "Complaint rating/review",
        "example_questions": ["Complaint ratings?", "Complaint reviews?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "COMPLAINT_FORWARDED",
        "module": "complaint",
        "description": "Forwarded complaints",
        "example_questions": ["Forwarded complaints?", "Escalated complaints?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "COMPLAINT_ATTACHMENTS",
        "module": "complaint",
        "description": "Complaint attachments",
        "example_questions": ["Complaint attachments?", "Files attached to complaints?"],
        "required_params": [],
        "optional_params": ["complaint_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "COMPLAINT_URGENT",
        "module": "complaint",
        "description": "Urgent complaints",
        "example_questions": ["Urgent complaints?", "High priority complaints?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "medium"
    },
    {
        "id": "COMPLAINT_RESOLVED_COUNT",
        "module": "complaint",
        "description": "Resolved count",
        "example_questions": ["Resolved complaints count?", "How many complaints resolved?"],
        "required_params": [],
        "optional_params": ["office_id", "from_date", "to_date"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "COMPLAINT_UNRESOLVED_COUNT",
        "module": "complaint",
        "description": "Unresolved count",
        "example_questions": ["Unresolved complaints count?", "How many complaints pending?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "COMPLAINT_OFFICE_SUMMARY",
        "module": "complaint",
        "description": "Complaint office summary",
        "example_questions": ["Office complaint summary?", "Complaint statistics?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "COMPLAINT_CATEGORY_SUMMARY",
        "module": "complaint",
        "description": "Complaint category summary",
        "example_questions": ["Category summary?", "Complaints by category count?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "COMPLAINT_DETAILED_LIST",
        "module": "complaint",
        "description": "Detailed complaint list",
        "example_questions": ["Show complaint details?", "Detailed complaints?"],
        "required_params": [],
        "optional_params": ["office_id", "status", "limit"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "medium"
    },
    {
        "id": "COMPLAINT_MODULE_SUMMARY",
        "module": "complaint",
        "description": "Complaint module summary",
        "example_questions": ["Complaint summary?", "Complaint module overview?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "summary",
        "security_level": "low"
    }
]


def execute(query_id, params, cur, office_id):
    """Execute complaint queries."""
    p = params or {}
    
    if query_id == "COMPLAINT_TOTAL":
        cur.execute("SELECT COUNT(*) AS total FROM complaints WHERE office_id = %s", (office_id,))
        r = cur.fetchone()
        return f"Total complaints: {r['total'] if r else 0}"
    
    return None
