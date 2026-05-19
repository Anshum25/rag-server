"""Feedback module schema for LLM SQL generation."""

FEEDBACK_SCHEMA = """
TRMS Feedback module schema.

Important rules:
- status = 1 means active record where applicable.
- office_id is used for office-wise filtering where available.
- Always enforce office_id from backend/login context.
- Do not select users.password.
- Use case-insensitive search for names: LOWER(users.name) LIKE LOWER('%name%')

Allowed tables and columns:

Table: feed_master
Columns:
- id
- user_id
- course_id
- fs_id
- fs_type
- fq_id
- fq_type
- response
- final_submit
- status
- created_at
- updated_at

Table: feed_que
Columns:
- fq_id
- fs_id
- office_id

Table: feed_section
Columns:
- fs_id
- office_id

Table: feed_forwards
Columns:
- id
- user_id
- course_id
- expec
- in_depth
- hands_on
- feed
- status
- created_at
- updated_at

Table: feed_que_vls
Columns:
- id
- office_id
- vl_id
- subject

Table: users
Columns:
- id
- role_id
- office_id
- name
- email
- status

Table: courses
Columns:
- id
- office_id
- course_name
- status
- created_at
- updated_at

Table: training_calendars
Columns:
- id
- office_id
- cf_id
- ct_id
- from_date
- to_date
- status
- created_at
- updated_at

Table: subjects
Columns:
- id
- office_id
- subject_name
- status

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
- feed_master stores main feedback responses.
- feed_que stores feedback questions.
- feed_section stores feedback sections.
- feed_forwards stores forwarded feedback entries.
- feed_que_vls stores VL-specific feedback questions.
- users for trainee information.
- courses for course information.
- vl_management for visiting lecturer feedback.

Recommended relationships:
- feed_master.user_id = users.id
- feed_master.course_id = training_calendars.id
- training_calendars.ct_id = courses.id
- feed_master.fq_id = feed_que.fq_id
- feed_master.fs_id = feed_section.fs_id
- feed_que_vls.vl_id = vl_management.id

Common question mapping:
- Total feedback: Count feed_master
- Feedback by course: Group by course_id
- Question-wise feedback: Join feed_master with feed_que
- Average rating: Aggregate feed_master.response
- Feedback pending: Users without feed_master entry
- VL feedback: Query feed_que_vls
"""
