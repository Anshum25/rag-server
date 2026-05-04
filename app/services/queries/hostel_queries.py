"""Hostel module query templates and dispatcher."""
from app.services.queries import hostel_building_room, hostel_occupancy_trainee, hostel_checkin_stats

TEMPLATES = [
    {"id": "HOSTEL_OCCUPANCY", "description": "Overall hostel occupancy rate/percentage"},
    {"id": "HOSTEL_FULL_ROOMS", "description": "Which rooms are completely full"},
    {"id": "HOSTEL_AVAILABLE_ROOMS", "description": "Available rooms with free beds. Params: gender (optional)"},
    {"id": "HOSTEL_TOTAL_ROOMS", "description": "Total number of hostel rooms"},
    {"id": "HOSTEL_UNUSED_ROOMS", "description": "Rooms with zero occupants"},
    {"id": "HOSTEL_PENDING_COMPLAINTS", "description": "Pending hostel complaints"},
    {"id": "HOSTEL_MOST_COMPLAINTS", "description": "Building with most complaints"},
    {"id": "HOSTEL_TRAINEES_IN_BUILDING", "description": "Trainees in a specific hostel building. Params: building_name (required)"},
    {"id": "HOSTEL_TRAINEES_NO_ROOM", "description": "Trainees without a room assigned"},
    {"id": "HOSTEL_ROOM_OCCUPANTS", "description": "Who stays in a specific room. Params: room_name (required)"},
    {"id": "HOSTEL_LADIES_ROOMS", "description": "Ladies hostel room stats"},
    {"id": "HOSTEL_TRAINEES_LIST", "description": "All trainees currently in hostel"},
    {"id": "HOSTEL_TRAINEE_DETAILS", "description": "Find hostel details for a trainee by name. Params: search_name (required)"},
    {"id": "HOSTEL_RECENT_CHECKINS", "description": "Recent hostel check-ins. Params: limit (default 10)"},
    {"id": "HOSTEL_ACTIVE_BUILDINGS", "description": "List all active hostel buildings"},
    {"id": "HOSTEL_ALL_BUILDINGS", "description": "List all buildings active and inactive"},
    {"id": "HOSTEL_TOTAL_BED_CAPACITY", "description": "Total bed capacity across all buildings"},
    {"id": "HOSTEL_BEDS_IN_SPECIFIC_BUILDING", "description": "Total beds/capacity in a specific building. Params: building_name (required)"},
    {"id": "HOSTEL_BED_CAPACITY_PER_BUILDING", "description": "Bed capacity per building"},
    {"id": "HOSTEL_BUILDING_DETAILS", "description": "Details of a specific building. Params: building_id (required)"},
    {"id": "HOSTEL_ROOMS_IN_BUILDING", "description": "List rooms in a building. Params: building_id (required)"},
    {"id": "HOSTEL_ROOMS_BY_BUILDING_NAME", "description": "Rooms by building name. Params: building_name (optional)"},
    {"id": "HOSTEL_AC_ROOMS", "description": "List all AC rooms"},
    {"id": "HOSTEL_ROOMS_WITH_TOILET", "description": "Rooms with attached toilet"},
    {"id": "HOSTEL_ROOMS_BY_FLOOR", "description": "Rooms on a floor. Params: floor (required)"},
    {"id": "HOSTEL_ROOM_SUMMARY_PER_BUILDING", "description": "Room summary per building"},
    {"id": "HOSTEL_TOTAL_BEDS", "description": "Total beds across all rooms"},
    {"id": "HOSTEL_OCCUPIED_ROOMS", "description": "Count of occupied rooms"},
    {"id": "HOSTEL_AVAILABLE_ROOMS_BY_BUILDING", "description": "Available rooms by building"},
    {"id": "HOSTEL_OCCUPANCY_SUMMARY", "description": "Occupancy summary"},
    {"id": "HOSTEL_FULL_ROOM_LIST_STATUS", "description": "Full room list with status"},
    {"id": "HOSTEL_CURRENT_STAYING_COUNT", "description": "How many trainees currently staying"},
    {"id": "HOSTEL_OCCUPANCY_PER_BUILDING", "description": "Occupancy per building"},
    {"id": "HOSTEL_OCCUPANCY_PER_ROOM", "description": "Occupancy per room. Params: building_id (required)"},
    {"id": "HOSTEL_VACANT_ROOMS_NOW", "description": "Vacant rooms right now"},
    {"id": "HOSTEL_OCCUPANCY_PERCENTAGE", "description": "Overall occupancy percentage"},
    {"id": "HOSTEL_IS_TRAINEE_IN_HOSTEL", "description": "Is trainee in hostel. Params: user_id (required)"},
    {"id": "HOSTEL_TRAINEE_BUILDING_ROOM", "description": "Trainee building and room. Params: user_id (required)"},
    {"id": "HOSTEL_WHO_IN_ROOM", "description": "Who in a room. Params: room_id (required)"},
    {"id": "HOSTEL_WHO_IN_BUILDING", "description": "Who in a building. Params: building_id (required)"},
    {"id": "HOSTEL_FULL_ALLOTMENT_LIST", "description": "Full allotment list"},
    {"id": "HOSTEL_GENDER_WISE_OCCUPANCY", "description": "Gender-wise occupancy"},
    {"id": "HOSTEL_TRAINEES_FOR_COURSE", "description": "Hostel trainees for a course. Params: course_id (required)"},
    {"id": "HOSTEL_SEARCH_TRAINEE_BY_NAME", "description": "Search trainee by name. Params: search_name (required)"},
    {"id": "HOSTEL_TRAINEES_STAYING", "description": "All trainees staying with room details"},
    {"id": "HOSTEL_FIND_TRAINEE_ROOM", "description": "Find trainee room. Params: user_id (required)"},
    {"id": "HOSTEL_CHECKINS_TODAY", "description": "Trainees checking in today"},
    {"id": "HOSTEL_CHECKOUTS_TODAY", "description": "Trainees checking out today"},
    {"id": "HOSTEL_CHECKOUTS_UPCOMING", "description": "Checkouts in next N days. Params: days_ahead (default 7)"},
    {"id": "HOSTEL_TRAINEE_STAY_HISTORY", "description": "Stay history. Params: user_id (required)"},
    {"id": "HOSTEL_CHECKINS_DATE_RANGE", "description": "Check-ins in date range. Params: from_date, to_date"},
    {"id": "HOSTEL_OVERSTAY", "description": "Trainees past checkout date"},
    {"id": "HOSTEL_MONTHLY_CHECKINS", "description": "Month-wise check-ins. Params: year (optional)"},
    {"id": "HOSTEL_COURSE_WISE_OCCUPANCY", "description": "Course-wise occupancy"},
    {"id": "HOSTEL_AVG_STAY_PER_BUILDING", "description": "Avg stay per building"},
    {"id": "HOSTEL_PH_TRAINEES", "description": "PH trainees in hostel"},
    {"id": "HOSTEL_COMPLAINTS_COUNT", "description": "Total complaints count"},
    {"id": "HOSTEL_COMPLAINTS_BY_STATUS", "description": "Complaints by status"},
    {"id": "HOSTEL_TOTAL_REVENUE", "description": "Total hostel charges collected"},
    {"id": "HOSTEL_DUES_PENDING", "description": "Trainees with dues pending"},
    {"id": "HOSTEL_TRAINEE_CHARGES", "description": "Trainee charges. Params: user_id (required)"},
    {"id": "HOSTEL_REVENUE_PER_BUILDING", "description": "Revenue per building"},
    {"id": "HOSTEL_MESS_TRAINEES", "description": "Trainees who opted for mess"},
    {"id": "HOSTEL_MESS_COUNT_PER_BUILDING", "description": "Mess count per building"},
    {"id": "HOSTEL_TOTAL_MESS_STRENGTH", "description": "Total mess strength today"},
    {"id": "HOSTEL_FIND_BY_RECEIPT", "description": "Find by receipt. Params: receipt_no (required)"},
    {"id": "HOSTEL_FIND_BY_ALLOTMENT_ID", "description": "Find by allotment ID. Params: hm_id (required)"},
    {"id": "HOSTEL_EXTRA_ROOM_ALLOTMENTS", "description": "Extra room allotments"},
]

# Ordered list of sub-handler modules
_HANDLERS = [hostel_building_room, hostel_occupancy_trainee, hostel_checkin_stats]


def execute(query_id, params, cur, office_id):
    """Dispatch to the appropriate hostel sub-handler."""
    for handler in _HANDLERS:
        result = handler.execute(query_id, params, cur, office_id)
        if result is not None:
            return result
    return None
