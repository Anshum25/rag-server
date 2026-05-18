"""Field Training and Study Tour module schema for LLM SQL generation."""

FIELD_STUDY_TOUR_SCHEMA = """
TRMS Field Training and Study Tour module schema.

Important rules:
- status = 1 means active record where applicable.
- office_id is used for office-wise filtering where available.
- Always enforce office_id from backend/login context.
- Do not select users.password.
- Use case-insensitive search for names: LOWER(users.name) LIKE LOWER('%name%')

Allowed tables and columns:

Table: field_training
Columns:
- id
- year
- course_id

Table: filled_training_data
Columns:
- id
- filled_id
- zone_id
- div_id
- trainee
- status
- created_at
- updated_at

Table: study_tour
Columns:
- id
- year
- course_id

Table: vehicle_registers
Columns:
- id
- study_id
- from_date
- return_date
- bus_num

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

Table: rail_zones
Columns:
- id
- zone_name
- zone_name_hindi

Table: divisions
Columns:
- id
- division

Business meaning:
- field_training stores field training programs.
- filled_training_data stores filled training details.
- study_tour stores study tour programs.
- vehicle_registers stores vehicle bookings for tours.
- users for trainees/staff.
- rail_zones, divisions for location info.
- tra_masters for trainee enrollment.

Recommended relationships:
- field_training.course_id = training_calendars.id
- study_tour.course_id = training_calendars.id
- filled_training_data.filled_id = field_training.id
- vehicle_registers.study_id = study_tour.id
- filled_training_data.zone_id = rail_zones.id
- filled_training_data.div_id = divisions.id

Common question mapping:
- Field trainings: Count field_training
- Study tours: Count study_tour
- Upcoming tours: Filter by year/current date
- Vehicle assigned: Join with vehicle_registers
- Trainee count: Count filled_training_data
- Zone-wise: Group by rail_zones
"""
