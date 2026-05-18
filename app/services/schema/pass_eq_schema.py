"""Pass and EQ (Privilege Pass/Employee Quarters) module schema for LLM SQL generation."""

PASS_EQ_SCHEMA = """
TRMS Pass and EQ module schema.

Important rules:
- status = 1 means active record where applicable.
- office_id is used for office-wise filtering where available.
- Always enforce office_id from backend/login context.
- Do not select users.password.
- Use case-insensitive search for names: LOWER(users.name) LIKE LOWER('%name%')

Allowed tables and columns:

Table: pass
Columns:
- id
- user_id
- forward_id
- pass_type
- c_d
- out_from
- out_to
- out_via
- out_break
- return_from
- return_to
- return_via
- return_break
- sets
- train_class
- onduty
- pass_year
- auto_log
- pass_no

Table: pass_type
Columns:
- id
- pass_type
- sort_no
- status
- created_at
- updated_at

Table: eqs
Columns:
- id
- user_id
- course_id
- journey_date
- dep_time
- train_no
- from_place

Table: users
Columns:
- id
- role_id
- office_id

Table: train_class
Columns:
- id
- class_name

Table: rail_stations
Columns:
- id
- st_name

Table: tra_masters
Columns:
- id
- user_id
- ct_id

Table: courses
Columns:
- id
- cf_id

Table: training_calendars
Columns:
- id
- cf_id
- ct_id

Business meaning:
- pass stores privilege pass requests.
- pass_type stores pass type master.
- eqs stores employee quarter/transport requests.
- users for pass applicants.
- train_class for train class types.
- rail_stations for station names.
- tra_masters for trainee enrollment.

Recommended relationships:
- pass.user_id = users.id
- pass.pass_type = pass_type.id
- eqs.user_id = users.id
- eqs.course_id = training_calendars.id

Common question mapping:
- Total pass requests: Count pass
- Pending pass: Filter by status
- Approved pass: Filter by status
- Pass by type: Join with pass_type
- EQ requests: Count eqs
- EQ by journey date: Filter eqs.journey_date
- Train class summary: Group by train_class
"""
