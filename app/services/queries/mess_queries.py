"""Mess module query templates."""

TEMPLATES = [
    {
        "id": "MESS_TOTAL_BILLS",
        "module": "mess",
        "description": "Total bills",
        "example_questions": ["Total mess bills?", "How many bills?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff", "mess_manager"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "MESS_BILL_AMOUNT_SUMMARY",
        "module": "mess",
        "description": "Bill amount summary",
        "example_questions": ["Total bill amount?", "Mess collection?"],
        "required_params": [],
        "optional_params": ["office_id", "from_date", "to_date"],
        "allowed_roles": ["principal", "admin", "mess_manager"],
        "result_type": "summary",
        "security_level": "medium"
    },
    {
        "id": "MESS_BILL_DETAILS_TRAINEE",
        "module": "mess",
        "description": "Bill details by trainee",
        "example_questions": ["Trainee bill details?", "Show trainee mess bill?"],
        "required_params": [],
        "optional_params": ["user_id", "user_name", "office_id"],
        "allowed_roles": ["principal", "admin", "mess_manager", "trainee"],
        "result_type": "detail",
        "security_level": "low"
    },
    {
        "id": "MESS_RECEIPTS",
        "module": "mess",
        "description": "Bill receipts",
        "example_questions": ["Mess receipts?", "Show receipts?"],
        "required_params": [],
        "optional_params": ["office_id", "from_date", "to_date"],
        "allowed_roles": ["principal", "admin", "mess_manager"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MESS_PENDING_DUES",
        "module": "mess",
        "description": "Pending dues",
        "example_questions": ["Pending mess dues?", "Unpaid mess bills?"],
        "required_params": [],
        "optional_params": ["office_id", "user_id"],
        "allowed_roles": ["principal", "admin", "mess_manager"],
        "result_type": "list",
        "security_level": "medium"
    },
    {
        "id": "MESS_PAID_RECEIPTS",
        "module": "mess",
        "description": "Paid receipts",
        "example_questions": ["Paid mess bills?", "Paid receipts?"],
        "required_params": [],
        "optional_params": ["office_id", "from_date", "to_date"],
        "allowed_roles": ["principal", "admin", "mess_manager"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MESS_REFUND_SUMMARY",
        "module": "mess",
        "description": "Refund summary",
        "example_questions": ["Mess refunds?", "Total refunds?"],
        "required_params": [],
        "optional_params": ["office_id", "from_date", "to_date"],
        "allowed_roles": ["principal", "admin", "mess_manager"],
        "result_type": "summary",
        "security_level": "medium"
    },
    {
        "id": "MESS_MATERIAL_LIST",
        "module": "mess",
        "description": "Mess material list",
        "example_questions": ["Mess materials?", "List mess items?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "mess_manager"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MESS_ITEM_PRICE_LIST",
        "module": "mess",
        "description": "Item price list",
        "example_questions": ["Item prices?", "Mess item rates?"],
        "required_params": [],
        "optional_params": ["office_id", "item_id"],
        "allowed_roles": ["principal", "admin", "mess_manager"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MESS_MONTHLY_BILL_SUMMARY",
        "module": "mess",
        "description": "Monthly bill summary",
        "example_questions": ["Monthly mess bill?", "This month mess collection?"],
        "required_params": [],
        "optional_params": ["month", "year", "office_id"],
        "allowed_roles": ["principal", "admin", "mess_manager"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "MESS_COURSE_WISE",
        "module": "mess",
        "description": "Course-wise mess bills",
        "example_questions": ["Course-wise mess bills?", "Mess by course?"],
        "required_params": [],
        "optional_params": ["course_id", "office_id"],
        "allowed_roles": ["principal", "admin", "mess_manager"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MESS_HOSTEL_WISE",
        "module": "mess",
        "description": "Hostel-wise mess bills",
        "example_questions": ["Hostel-wise mess?", "Mess by hostel?"],
        "required_params": [],
        "optional_params": ["hostel_id", "office_id"],
        "allowed_roles": ["principal", "admin", "mess_manager"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MESS_TOTAL_COLLECTION",
        "module": "mess",
        "description": "Total collection",
        "example_questions": ["Total mess collection?", "Overall mess revenue?"],
        "required_params": [],
        "optional_params": ["office_id", "from_date", "to_date"],
        "allowed_roles": ["principal", "admin", "mess_manager"],
        "result_type": "summary",
        "security_level": "medium"
    },
    {
        "id": "MESS_TOTAL_DUE",
        "module": "mess",
        "description": "Total due",
        "example_questions": ["Total mess dues?", "Outstanding mess amount?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "mess_manager"],
        "result_type": "summary",
        "security_level": "medium"
    },
    {
        "id": "MESS_BILL_BY_DATE",
        "module": "mess",
        "description": "Bill by date",
        "example_questions": ["Bills on date?", "Date-wise bills?"],
        "required_params": [],
        "optional_params": ["date", "from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin", "mess_manager"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MESS_RECEIPT_BY_DATE",
        "module": "mess",
        "description": "Receipt by date",
        "example_questions": ["Receipts on date?", "Date-wise receipts?"],
        "required_params": [],
        "optional_params": ["date", "from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin", "mess_manager"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MESS_ITEM_WISE_SUMMARY",
        "module": "mess",
        "description": "Item-wise bill summary",
        "example_questions": ["Item-wise bill?", "Bill by item?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "mess_manager"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "MESS_PARTY_VENDOR_SUMMARY",
        "module": "mess",
        "description": "Party/vendor summary",
        "example_questions": ["Vendor summary?", "Party-wise summary?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "mess_manager"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "MESS_FORMAT_DETAILS",
        "module": "mess",
        "description": "Mess format/company details",
        "example_questions": ["Mess format?", "Company details?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "mess_manager"],
        "result_type": "detail",
        "security_level": "low"
    },
    {
        "id": "MESS_MODULE_SUMMARY",
        "module": "mess",
        "description": "Mess module summary",
        "example_questions": ["Mess summary?", "Mess module overview?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "summary",
        "security_level": "low"
    }
]


def execute(query_id, params, cur, office_id):
    """Execute mess queries."""
    p = params or {}
    
    if query_id == "MESS_TOTAL_BILLS":
        cur.execute("SELECT COUNT(*) AS total FROM bills WHERE office_id = %s", (office_id,))
        r = cur.fetchone()
        return f"Total mess bills: {r['total'] if r else 0}"
    
    return None
