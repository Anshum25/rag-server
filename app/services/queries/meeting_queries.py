"""Meeting module query templates."""

TEMPLATES = [
    {
        "id": "MEETING_TOTAL",
        "module": "meeting",
        "description": "Total meetings",
        "example_questions": ["Total meetings?", "How many meetings?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "MEETING_UPCOMING",
        "module": "meeting",
        "description": "Upcoming meetings",
        "example_questions": ["Upcoming meetings?", "Future meetings?"],
        "required_params": [],
        "optional_params": ["office_id", "limit"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MEETING_COMPLETED",
        "module": "meeting",
        "description": "Completed meetings",
        "example_questions": ["Completed meetings?", "Past meetings?"],
        "required_params": [],
        "optional_params": ["office_id", "from_date"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MEETING_BY_DATE",
        "module": "meeting",
        "description": "Meeting by date",
        "example_questions": ["Meetings on date?", "Date-wise meetings?"],
        "required_params": [],
        "optional_params": ["date", "from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MEETING_AGENDA_LIST",
        "module": "meeting",
        "description": "Meeting agenda list",
        "example_questions": ["Meeting agenda?", "Agenda items?"],
        "required_params": [],
        "optional_params": ["meeting_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MEETING_BY_CHAIRMAN",
        "module": "meeting",
        "description": "Meeting by chairman",
        "example_questions": ["Meetings by chairman?", "Chairman's meetings?"],
        "required_params": [],
        "optional_params": ["chairman_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MEETING_BY_CREATOR",
        "module": "meeting",
        "description": "Meeting by creator",
        "example_questions": ["Meetings by creator?", "Created meetings?"],
        "required_params": [],
        "optional_params": ["creator_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MEETING_INVITEES",
        "module": "meeting",
        "description": "Meeting invitees",
        "example_questions": ["Meeting invitees?", "Who is invited?"],
        "required_params": [],
        "optional_params": ["meeting_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MEETING_MOM_SUMMARY",
        "module": "meeting",
        "description": "MOM summary",
        "example_questions": ["Minutes of meeting?", "MOM?"],
        "required_params": [],
        "optional_params": ["meeting_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "MEETING_PENDING_AGENDA",
        "module": "meeting",
        "description": "Pending agenda",
        "example_questions": ["Pending agenda?", "Open agenda items?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MEETING_STATUS_SUMMARY",
        "module": "meeting",
        "description": "Meeting status summary",
        "example_questions": ["Meeting status?", "Status summary?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "MEETING_BY_SUBJECT",
        "module": "meeting",
        "description": "Meeting by subject",
        "example_questions": ["Meetings by subject?", "Subject-wise meetings?"],
        "required_params": [],
        "optional_params": ["subject", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MEETING_BY_DEPARTMENT",
        "module": "meeting",
        "description": "Meeting by department",
        "example_questions": ["Dept meetings?", "Department-wise meetings?"],
        "required_params": [],
        "optional_params": ["department_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MEETING_MONTHLY_COUNT",
        "module": "meeting",
        "description": "Monthly meeting count",
        "example_questions": ["Monthly meetings?", "Meetings this month?"],
        "required_params": [],
        "optional_params": ["month", "year", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "MEETING_FILES",
        "module": "meeting",
        "description": "Meeting files",
        "example_questions": ["Meeting files?", "Attachments?"],
        "required_params": [],
        "optional_params": ["meeting_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MEETING_FORWARDED",
        "module": "meeting",
        "description": "Forwarded meetings",
        "example_questions": ["Forwarded meetings?", "Delegated meetings?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MEETING_REMATCH",
        "module": "meeting",
        "description": "Re-meetings",
        "example_questions": ["Re-meetings?", "Follow-up meetings?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MEETING_ACTION_SUMMARY",
        "module": "meeting",
        "description": "Meeting action summary",
        "example_questions": ["Action items?", "Meeting actions?"],
        "required_params": [],
        "optional_params": ["meeting_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "MEETING_MASTER_LIST",
        "module": "meeting",
        "description": "Meeting master list",
        "example_questions": ["Meeting types?", "Master meeting list?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "MEETING_MODULE_SUMMARY",
        "module": "meeting",
        "description": "Meeting module summary",
        "example_questions": ["Meeting summary?", "Meeting module overview?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "summary",
        "security_level": "low"
    }
]


def execute(query_id, params, cur, office_id):
    """Execute meeting queries."""
    p = params or {}
    
    if query_id == "MEETING_TOTAL":
        cur.execute("SELECT COUNT(*) AS total FROM meeting_create mc JOIN mdl_calenders mdl ON mdl.ct_id = mc.id WHERE mdl.office_id = %s", (office_id,))
        r = cur.fetchone()
        return f"Total meetings: {r['total'] if r else 0}"
    
    return None
