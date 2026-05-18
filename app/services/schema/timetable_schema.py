"""Timetable module schema for LLM SQL generation."""

TIMETABLE_SCHEMA = """
TRMS Timetable module schema.

Important rules:
- status = 1 means active record where applicable.
- office_id is used for office-wise filtering where available.
- Always enforce office_id from backend/login context.
- Do not select users.password.
- Use case-insensitive search for names: LOWER(users.name) LIKE LOWER('%name%')

Allowed tables and columns:

Table: time_masters
Columns:
- id
- course_id
- cs_id
- office_id

Table: tt_designs
Columns:
- id
- course_id

Table: tt_designs_daywise
Columns:
- id
- tt_design_id

Table: training_calendars
Columns:
- id
- cf_id
- ct_id

Table: courses
Columns:
- id
- cf_id

Table: subjects
Columns:
- id
- office_id

Table: topics
Columns:
- id
- office_id

Table: sessions
Columns:
- id
- office_id

Table: class_rooms
Columns:
- id
- office_id

Table: users
Columns:
- id
- role_id
- office_id

Table: designations
Columns:
- id
- grade_id

Table: vl_management
Columns:
- id
- office_id
- vl_id
- vl_date
- subject_name
- description_1
- description_2
- user_type
- status
- created_at
- updated_at

Business meaning:
- time_masters stores time table master records.
- tt_designs stores timetable design/schedule.
- tt_designs_daywise stores day-wise timetable entries.
- training_calendars stores course batch/calendar info.
- courses stores course master data.
- subjects, topics, sessions are master tables for content.
- class_rooms stores classroom information.
- vl_management stores visiting lecturer schedule.

Recommended relationships:
- time_masters.course_id -> training_calendars.id
- tt_designs.course_id -> training_calendars.id
- tt_designs_daywise.tt_design_id -> tt_designs.id
- training_calendars.ct_id -> courses.id
- vl_management for visiting lecturer sessions

Common question mapping:
- Today's timetable: Filter by current date on tt_designs_daywise
- Weekly timetable: Group by day of week
- Course timetable: Filter by course_id
- Faculty timetable: Join with users/faculty
- VL lectures: Query vl_management
- Classroom usage: Query class_rooms with timetable
"""
