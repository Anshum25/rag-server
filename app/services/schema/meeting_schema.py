"""Meeting module schema for LLM SQL generation."""

MEETING_SCHEMA = """
TRMS Meeting module schema.

Important rules:
- status = 1 means active record where applicable.
- office_id is used for office-wise filtering where available.
- Always enforce office_id from backend/login context.
- Do not select users.password.
- Use case-insensitive search for names: LOWER(users.name) LIKE LOWER('%name%')

Allowed tables and columns:

Table: meeting_create
Columns:
- id
- subject
- title
- start_time
- end_time
- description
- date
- creator
- chairman
- invitee

Table: meeting_master
Columns:
- id
- meeting_name
- status
- created_at
- updated_at

Table: meet_agenda
Columns:
- id
- office_id
- meeting_id
- agenda_id
- type_agenda
- status
- created_at
- updated_at

Table: mdl_calenders
Columns:
- ct_id
- id
- office_id
- no
- agenda_title
- description
- incharge

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
- meeting_create stores meeting creation details.
- meeting_master stores meeting type master.
- meet_agenda stores meeting agenda items.
- mdl_calenders stores calendar-based meeting schedules.
- users for attendees/creators.
- departments, designations for organization.

Recommended relationships:
- meet_agenda.meeting_id = meeting_create.id
- mdl_calenders for scheduled meetings
- users for creator, chairman, invitee

Common question mapping:
- Total meetings: Count meeting_create
- Upcoming meetings: Filter by date >= CURDATE()
- Completed meetings: Filter by past dates
- Meeting agenda: Query meet_agenda
- Meetings by chairman: Filter by chairman field
"""
