"""Vehicle module query templates."""

TEMPLATES = [
    {
        "id": "VEHICLE_BOOKING_COUNT",
        "module": "vehicle",
        "description": "Vehicle booking count",
        "example_questions": ["Total vehicle bookings?", "How many bookings?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "VEHICLE_BOOKINGS_BY_DATE",
        "module": "vehicle",
        "description": "Vehicle bookings by date",
        "example_questions": ["Bookings on date?", "Date-wise bookings?"],
        "required_params": [],
        "optional_params": ["date", "from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "VEHICLE_UPCOMING",
        "module": "vehicle",
        "description": "Upcoming vehicle bookings",
        "example_questions": ["Upcoming bookings?", "Future vehicle trips?"],
        "required_params": [],
        "optional_params": ["office_id", "limit"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "VEHICLE_COMPLETED",
        "module": "vehicle",
        "description": "Completed vehicle bookings",
        "example_questions": ["Completed trips?", "Past bookings?"],
        "required_params": [],
        "optional_params": ["office_id", "from_date"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "VEHICLE_REGISTER_LIST",
        "module": "vehicle",
        "description": "Vehicle register list",
        "example_questions": ["Vehicle list?", "Registered vehicles?"],
        "required_params": [],
        "optional_params": ["office_id", "limit"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "VEHICLE_BY_COURSE",
        "module": "vehicle",
        "description": "Vehicle by course",
        "example_questions": ["Vehicle by course?", "Course-wise bookings?"],
        "required_params": [],
        "optional_params": ["course_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "VEHICLE_BY_STUDY_TOUR",
        "module": "vehicle",
        "description": "Vehicle by study tour",
        "example_questions": ["Vehicle for study tour?", "Tour vehicles?"],
        "required_params": [],
        "optional_params": ["study_tour_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "VEHICLE_BY_FIELD_TRAINING",
        "module": "vehicle",
        "description": "Vehicle by field training",
        "example_questions": ["Vehicle for field training?", "Training vehicles?"],
        "required_params": [],
        "optional_params": ["field_training_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "VEHICLE_TRAINEE_COUNT",
        "module": "vehicle",
        "description": "Total trainees in vehicle trips",
        "example_questions": ["Trainees in vehicles?", "Passenger count?"],
        "required_params": [],
        "optional_params": ["office_id", "trip_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "VEHICLE_KM_SUMMARY",
        "module": "vehicle",
        "description": "KM summary",
        "example_questions": ["Total KM?", "Kilometer summary?"],
        "required_params": [],
        "optional_params": ["office_id", "from_date", "to_date"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "VEHICLE_ROUTE_SUMMARY",
        "module": "vehicle",
        "description": "Route/from-to summary",
        "example_questions": ["Route summary?", "Popular routes?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "VEHICLE_STATUS_SUMMARY",
        "module": "vehicle",
        "description": "Vehicle status summary",
        "example_questions": ["Vehicle status?", "Booking status?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "VEHICLE_PENDING",
        "module": "vehicle",
        "description": "Pending bookings",
        "example_questions": ["Pending bookings?", "Awaiting approval?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "VEHICLE_APPROVED",
        "module": "vehicle",
        "description": "Approved bookings",
        "example_questions": ["Approved bookings?", "Confirmed trips?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "VEHICLE_CANCELLED",
        "module": "vehicle",
        "description": "Cancelled bookings",
        "example_questions": ["Cancelled bookings?", "Rejected trips?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "VEHICLE_TWO_WAY",
        "module": "vehicle",
        "description": "Two-way bookings",
        "example_questions": ["Two-way bookings?", "Round trips?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "VEHICLE_TRAIN_PNR",
        "module": "vehicle",
        "description": "Train/PNR booking info",
        "example_questions": ["Train bookings?", "PNR details?"],
        "required_params": [],
        "optional_params": ["office_id", "pnr_number"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "medium"
    },
    {
        "id": "VEHICLE_USAGE_MONTHLY",
        "module": "vehicle",
        "description": "Vehicle usage by month",
        "example_questions": ["Monthly usage?", "Vehicle by month?"],
        "required_params": [],
        "optional_params": ["month", "year", "office_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "VEHICLE_DRIVER_DETAILS",
        "module": "vehicle",
        "description": "Driver details",
        "example_questions": ["Driver details?", "Driver assignments?"],
        "required_params": [],
        "optional_params": ["office_id", "vehicle_id"],
        "allowed_roles": ["principal", "admin", "staff"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "VEHICLE_MODULE_SUMMARY",
        "module": "vehicle",
        "description": "Vehicle module summary",
        "example_questions": ["Vehicle summary?", "Vehicle module overview?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "summary",
        "security_level": "low"
    }
]


def execute(query_id, params, cur, office_id):
    """Execute vehicle queries."""
    p = params or {}
    
    if query_id == "VEHICLE_BOOKING_COUNT":
        cur.execute("SELECT COUNT(*) AS total FROM vehicle_masters vm JOIN training_calendars tc ON tc.id = vm.course_id WHERE tc.office_id = %s", (office_id,))
        r = cur.fetchone()
        return f"Total vehicle bookings: {r['total'] if r else 0}"
    
    return None
