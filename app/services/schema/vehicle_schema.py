"""Vehicle module schema for LLM SQL generation."""

VEHICLE_SCHEMA = """
TRMS Vehicle module schema.

Important rules:
- status = 1 means active record where applicable.
- office_id is used for office-wise filtering where available.
- Always enforce office_id from backend/login context.
- Do not select users.password.
- Use case-insensitive search for names: LOWER(users.name) LIKE LOWER('%name%')

Allowed tables and columns:

Table: vehicle_masters
Columns:
- id
- user_id
- course_id

Table: vehicle_registers
Columns:
- id
- study_id
- from_date
- return_date
- bus_num

Table: study_tour
Columns:
- id
- year
- course_id

Table: field_training
Columns:
- id
- year
- course_id

Table: users
Columns:
- id
- role_id
- office_id

Table: courses
Columns:
- id
- cf_id

Table: training_calendars
Columns:
- id
- cf_id
- ct_id

Table: tra_masters
Columns:
- id
- user_id
- ct_id

Business meaning:
- vehicle_masters stores vehicle booking master.
- vehicle_registers stores vehicle registration/trip records.
- study_tour stores study tour programs.
- field_training stores field training programs.
- users for trainee/staff info.
- tra_masters for trainee enrollment.

Recommended relationships:
- vehicle_masters.user_id = users.id
- vehicle_masters.course_id = training_calendars.id
- vehicle_registers.study_id = study_tour.id
- study_tour.course_id = training_calendars.id
- field_training.course_id = training_calendars.id

Common question mapping:
- Vehicle bookings: Count vehicle_masters
- Upcoming trips: Filter by from_date > CURDATE()
- Completed trips: Filter by return_date < CURDATE()
- Vehicle by study tour: Join vehicle_registers with study_tour
- Vehicle by field training: Join with field_training
- KM summary: Aggregate distance if available
"""
