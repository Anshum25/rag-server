"""Attendance module schema for LLM SQL generation."""

ATTENDANCE_SCHEMA = """
TRMS Attendance module schema.

Important rules:
- status = 1 means active record where applicable.
- office_id is used for office-wise filtering where available.
- Always enforce office_id from backend/login context.
- Do not select users.password.
- Use case-insensitive search for names: LOWER(users.name) LIKE LOWER('%name%')

Allowed tables and columns:

Table: attendances
Columns:
- id
- user_id
- course_id
- punch_time
- punch
- latitude
- longitude
- imei
- mac
- photo

Table: users
Columns:
- id
- role_id
- office_id

Table: tra_masters
Columns:
- id
- user_id
- ct_id

Table: training_calendars
Columns:
- id
- cf_id
- ct_id

Table: courses
Columns:
- id
- cf_id

Table: departments
Columns:
- id
- service_id
- office_id

Table: designations
Columns:
- id
- grade_id

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
- attendances stores trainee attendance/punch records.
- attendances.user_id joins with users.id.
- attendances.course_id joins with training_calendars.id.
- users stores trainee/user details.
- tra_masters stores trainee course enrollment.
- training_calendars stores course batch information.
- courses stores course master data.
- departments, designations, rail_zones, divisions are master tables.

Recommended relationships:
- attendances.user_id = users.id
- attendances.course_id = training_calendars.id
- tra_masters.user_id = users.id
- tra_masters.ct_id = training_calendars.id
- training_calendars.ct_id = courses.id
- users.office_id for office filtering

Common question mapping:
- Attendance by date: Filter attendances.punch_time
- Present trainees: attendances records for the day
- Absent trainees: trainees in course but no attendance record
- Punch count: Count attendances records
- Course-wise attendance: Group by training_calendars -> courses
"""
