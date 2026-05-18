"""Attendance module query templates."""

TEMPLATES = [
    {
        "id": "ATTENDANCE_TOTAL_RECORDS",
        "module": "attendance",
        "description": "Total attendance records",
        "example_questions": ["Total attendance records?", "How many attendance entries?"],
        "required_params": [],
        "optional_params": ["office_id", "from_date", "to_date"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "ATTENDANCE_COUNT_BY_DATE",
        "module": "attendance",
        "description": "Attendance count by date",
        "example_questions": ["Attendance count by date?", "How many present today?"],
        "required_params": [],
        "optional_params": ["date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "ATTENDANCE_TRAINEE_BY_NAME",
        "module": "attendance",
        "description": "Trainee attendance by name",
        "example_questions": ["Show attendance of trainee?", "Is Mayank present today?"],
        "required_params": [],
        "optional_params": ["user_name", "user_id", "from_date", "to_date"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "ATTENDANCE_COURSE_WISE",
        "module": "attendance",
        "description": "Course-wise attendance",
        "example_questions": ["Course-wise attendance?", "Attendance by course?"],
        "required_params": [],
        "optional_params": ["course_id", "course_name", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "ATTENDANCE_BATCH_WISE",
        "module": "attendance",
        "description": "Batch-wise attendance",
        "example_questions": ["Batch-wise attendance?", "Attendance by batch?"],
        "required_params": [],
        "optional_params": ["batch_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "ATTENDANCE_ABSENT_TRAINEES",
        "module": "attendance",
        "description": "Absent trainees",
        "example_questions": ["Who is absent today?", "List absent trainees"],
        "required_params": [],
        "optional_params": ["date", "course_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "ATTENDANCE_PRESENT_TRAINEES",
        "module": "attendance",
        "description": "Present trainees",
        "example_questions": ["Who is present today?", "List present trainees"],
        "required_params": [],
        "optional_params": ["date", "course_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "ATTENDANCE_PERCENTAGE",
        "module": "attendance",
        "description": "Attendance percentage",
        "example_questions": ["What is attendance percentage?", "Show attendance rate"],
        "required_params": [],
        "optional_params": ["course_id", "from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "ATTENDANCE_PUNCH_COUNT",
        "module": "attendance",
        "description": "Punch count",
        "example_questions": ["Total punches today?", "How many punches?"],
        "required_params": [],
        "optional_params": ["date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "ATTENDANCE_TODAY",
        "module": "attendance",
        "description": "Today's attendance",
        "example_questions": ["Today's attendance?", "Who came today?"],
        "required_params": [],
        "optional_params": ["office_id", "course_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "ATTENDANCE_MONTHLY",
        "module": "attendance",
        "description": "Monthly attendance",
        "example_questions": ["Monthly attendance?", "This month attendance?"],
        "required_params": [],
        "optional_params": ["month", "year", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "ATTENDANCE_YEAR_WISE",
        "module": "attendance",
        "description": "Year-wise attendance",
        "example_questions": ["Year-wise attendance?", "Annual attendance?"],
        "required_params": [],
        "optional_params": ["year", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "ATTENDANCE_BY_TRAINEE",
        "module": "attendance",
        "description": "Attendance by trainee",
        "example_questions": ["Show my attendance?", "Attendance of trainee?"],
        "required_params": [],
        "optional_params": ["user_id", "user_name", "from_date", "to_date"],
        "allowed_roles": ["principal", "admin", "staff", "trainee"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "ATTENDANCE_SUMMARY",
        "module": "attendance",
        "description": "Attendance summary",
        "example_questions": ["Attendance summary?", "Overall attendance stats?"],
        "required_params": [],
        "optional_params": ["from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "ATTENDANCE_BY_DEPARTMENT",
        "module": "attendance",
        "description": "Attendance by department",
        "example_questions": ["Department-wise attendance?", "Attendance by department?"],
        "required_params": [],
        "optional_params": ["department_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "ATTENDANCE_BY_DESIGNATION",
        "module": "attendance",
        "description": "Attendance by designation",
        "example_questions": ["Designation-wise attendance?", "Attendance by designation?"],
        "required_params": [],
        "optional_params": ["designation_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "ATTENDANCE_BY_OFFICE",
        "module": "attendance",
        "description": "Attendance by office",
        "example_questions": ["Office-wise attendance?", "Attendance by office?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "list",
        "security_level": "medium"
    },
    {
        "id": "ATTENDANCE_IRREGULAR",
        "module": "attendance",
        "description": "Irregular/late attendance",
        "example_questions": ["Irregular attendance?", "Late comers?"],
        "required_params": [],
        "optional_params": ["from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "ATTENDANCE_DETAILED_LIST",
        "module": "attendance",
        "description": "Detailed attendance list",
        "example_questions": ["Show attendance details?", "Detailed attendance report?"],
        "required_params": [],
        "optional_params": ["from_date", "to_date", "course_id", "office_id", "limit"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "ATTENDANCE_MODULE_SUMMARY",
        "module": "attendance",
        "description": "Attendance module summary",
        "example_questions": ["Attendance summary?", "Attendance module overview?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "summary",
        "security_level": "low"
    }
]


def execute(query_id, params, cur, office_id):
    """Execute attendance queries."""
    p = params or {}
    
    if query_id == "ATTENDANCE_TOTAL_RECORDS":
        cur.execute("SELECT COUNT(*) AS total FROM attendances a JOIN users u ON u.id = a.user_id WHERE u.office_id = %s", (office_id,))
        r = cur.fetchone()
        return f"Total attendance records: {r['total'] if r else 0}"
        
    elif query_id == "ATTENDANCE_COUNT_BY_DATE":
        date = p.get("date")
        if date:
            cur.execute("SELECT COUNT(*) AS total FROM attendances a JOIN users u ON u.id = a.user_id WHERE u.office_id = %s AND DATE(a.punch_time) = %s", (office_id, date))
        else:
            cur.execute("SELECT COUNT(*) AS total FROM attendances a JOIN users u ON u.id = a.user_id WHERE u.office_id = %s AND DATE(a.punch_time) = CURDATE()", (office_id,))
        r = cur.fetchone()
        return f"Attendance count: {r['total'] if r else 0}"
    
    return None
