"""Faculty and Visiting Lecturer module schema for LLM SQL generation."""

FACULTY_VL_SCHEMA = """
TRMS Faculty and Visiting Lecturer (VL) module schema.

Important rules:
- status = 1 means active record where applicable.
- office_id is used for office-wise filtering where available.
- Always enforce office_id from backend/login context.
- Do not select users.password.
- Use case-insensitive search for names: LOWER(users.name) LIKE LOWER('%name%')

Allowed tables and columns:

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

Table: vl_description
Columns:
- id
- office_id
- vlm_id
- course_id
- from_date
- to_date
- lecture_date
- price
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

Table: designations
Columns:
- id
- grade_id

Table: subjects
Columns:
- id
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

Table: departments
Columns:
- id
- service_id
- office_id

Business meaning:
- vl_management stores visiting lecturer master records.
- vl_description stores detailed VL lecture descriptions.
- feed_que_vls stores VL-related feedback questions.
- users stores faculty/user details.
- designations stores designation master.
- subjects stores subject master.
- courses stores course information.
- training_calendars stores course batch info.

Recommended relationships:
- vl_management.id = vl_description.vlm_id
- vl_management joins with courses via vl_description
- feed_que_vls.vl_id -> vl_management.id
- users.id for faculty information
- subjects for subject details

Common question mapping:
- Total VLs: Count vl_management records
- VL by date: Filter vl_management.vl_date
- VL by subject: Filter vl_management.subject_name
- VL by course: Join with vl_description -> courses
- Faculty lecture schedule: Query vl_description
- VL payment: Sum vl_description.price
"""
