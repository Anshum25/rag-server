"""Inspection module schema for LLM SQL generation."""

INSPECTION_SCHEMA = """
TRMS Inspection module schema.

Important rules:
- status = 1 means active record where applicable.
- office_id is used for office-wise filtering where available.
- Always enforce office_id from backend/login context.
- Do not select users.password.
- Use case-insensitive search for names: LOWER(users.name) LIKE LOWER('%name%')

Allowed tables and columns:

Table: inspection_notes
Columns:
- id
- office_id
- title
- from_date
- to_date
- file_upload
- short_desc
- created_by

Table: inspection_description
Columns:
- id
- office_id
- insp_id
- description
- faculty_id

Table: users
Columns:
- id
- role_id
- office_id

Table: departments
Columns:
- id
- service_id
- office_id

Table: designations
Columns:
- id
- grade_id

Business meaning:
- inspection_notes stores inspection note headers.
- inspection_description stores detailed inspection descriptions.
- users for inspectors and faculty.
- departments, designations for organization.

Recommended relationships:
- inspection_description.insp_id = inspection_notes.id
- inspection_notes.created_by = users.id
- inspection_description.faculty_id = users.id

Common question mapping:
- Total inspections: Count inspection_notes
- Inspection by date: Filter from_date/to_date
- Inspection descriptions: Query inspection_description
- Inspection by faculty: Filter by created_by/faculty_id
"""
