"""Field Training and Study Tour module query templates."""

TEMPLATES = [
    {
        "id": "FST_TOTAL_FIELD_TRAINING",
        "module": "field_study_tour",
        "description": "Total field trainings",
        "example_questions": ["Total field trainings?", "How many field trainings?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "FST_TOTAL_STUDY_TOURS",
        "module": "field_study_tour",
        "description": "Total study tours",
        "example_questions": ["Total study tours?", "How many study tours?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "FST_UPCOMING_FIELD_TRAINING",
        "module": "field_study_tour",
        "description": "Upcoming field trainings",
        "example_questions": ["Upcoming field trainings?", "Future trainings?"],
        "required_params": [],
        "optional_params": ["office_id", "limit"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FST_COMPLETED_FIELD_TRAINING",
        "module": "field_study_tour",
        "description": "Completed field trainings",
        "example_questions": ["Completed field trainings?", "Past trainings?"],
        "required_params": [],
        "optional_params": ["office_id", "year"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FST_UPCOMING_STUDY_TOURS",
        "module": "field_study_tour",
        "description": "Upcoming study tours",
        "example_questions": ["Upcoming study tours?", "Future tours?"],
        "required_params": [],
        "optional_params": ["office_id", "limit"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FST_COMPLETED_STUDY_TOURS",
        "module": "field_study_tour",
        "description": "Completed study tours",
        "example_questions": ["Completed study tours?", "Past tours?"],
        "required_params": [],
        "optional_params": ["office_id", "year"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FST_COURSE_WISE_TOURS",
        "module": "field_study_tour",
        "description": "Course-wise tours",
        "example_questions": ["Tours by course?", "Course-wise study tours?"],
        "required_params": [],
        "optional_params": ["course_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FST_YEAR_WISE_TOURS",
        "module": "field_study_tour",
        "description": "Year-wise tours",
        "example_questions": ["Tours by year?", "Year-wise study tours?"],
        "required_params": [],
        "optional_params": ["year", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FST_TRAINEE_COUNT_TOUR",
        "module": "field_study_tour",
        "description": "Trainee count in tour",
        "example_questions": ["Trainees in tour?", "How many trainees?"],
        "required_params": [],
        "optional_params": ["tour_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "FST_STAFF_ASSIGNED",
        "module": "field_study_tour",
        "description": "Staff assigned",
        "example_questions": ["Staff assigned?", "Who is assigned?"],
        "required_params": [],
        "optional_params": ["tour_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FST_VEHICLE_ASSIGNED",
        "module": "field_study_tour",
        "description": "Vehicle assigned",
        "example_questions": ["Vehicle assigned?", "Transport assigned?"],
        "required_params": [],
        "optional_params": ["tour_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FST_ROUTE_SUMMARY",
        "module": "field_study_tour",
        "description": "Route summary",
        "example_questions": ["Route summary?", "Tour routes?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "FST_DATE_RANGE_TOURS",
        "module": "field_study_tour",
        "description": "Date range tours",
        "example_questions": ["Tours in date range?", "Between dates?"],
        "required_params": [],
        "optional_params": ["from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FST_BUS_NUMBER_SUMMARY",
        "module": "field_study_tour",
        "description": "Bus number summary",
        "example_questions": ["Bus summary?", "Which buses used?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "FST_TOUR_STATUS_SUMMARY",
        "module": "field_study_tour",
        "description": "Tour status summary",
        "example_questions": ["Tour status?", "Study tour status?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "FST_FIELD_TRAINING_STATUS",
        "module": "field_study_tour",
        "description": "Field training status summary",
        "example_questions": ["Field training status?", "Training status?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "FST_FILLED_TRAINING_DATA",
        "module": "field_study_tour",
        "description": "Filled training data",
        "example_questions": ["Filled training data?", "Training details?"],
        "required_params": [],
        "optional_params": ["training_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FST_ZONE_DIVISION_WISE",
        "module": "field_study_tour",
        "description": "Zone/division-wise training",
        "example_questions": ["Training by zone?", "Division-wise training?"],
        "required_params": [],
        "optional_params": ["zone_id", "division_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FST_STAFF_WISE_TOURS",
        "module": "field_study_tour",
        "description": "Staff-wise tours",
        "example_questions": ["Tours by staff?", "Staff tour assignments?"],
        "required_params": [],
        "optional_params": ["staff_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "FST_MODULE_SUMMARY",
        "module": "field_study_tour",
        "description": "Field/study tour module summary",
        "example_questions": ["Field study tour summary?", "Module overview?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "summary",
        "security_level": "low"
    }
]


def execute(query_id, params, cur, office_id):
    """Execute field study tour queries."""
    p = params or {}
    
    if query_id == "FST_TOTAL_FIELD_TRAINING":
        cur.execute("SELECT COUNT(*) AS total FROM field_training ft JOIN training_calendars tc ON tc.id = ft.course_id WHERE tc.office_id = %s", (office_id,))
        r = cur.fetchone()
        return f"Total field trainings: {r['total'] if r else 0}"
    
    return None
