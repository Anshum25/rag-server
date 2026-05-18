"""Seminar module schema for LLM SQL generation."""

SEMINAR_SCHEMA = """
TRMS Seminar module schema.

Important rules:
- status = 1 means active record where applicable.
- office_id is used for office-wise filtering where available.
- Always enforce office_id from backend/login context.
- Do not select users.password.
- Use case-insensitive search for names: LOWER(users.name) LIKE LOWER('%name%')

Allowed tables and columns:

Table: seminars
Columns:
- id
- sem_date
- subject
- start_time
- end_time
- type_id
- topic_id

Table: seminars_topic
Columns:
- id
- office_id
- sub_topic
- status
- created_at
- updated_at

Table: topics
Columns:
- id
- office_id

Table: users
Columns:
- id
- role_id
- office_id

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

Table: subjects
Columns:
- id
- office_id

Table: departments
Columns:
- id
- service_id
- office_id

Business meaning:
- seminars stores seminar event records.
- seminars_topic stores seminar topic details.
- topics stores master topic list.
- users for speakers/judges.
- vl_management for visiting lecturer seminars.
- subjects for subject information.

Recommended relationships:
- seminars.topic_id = topics.id
- seminars_topic for sub-topic details
- vl_management for VL-led seminars

Common question mapping:
- Total seminars: Count seminars
- Upcoming seminars: Filter sem_date >= CURDATE()
- Completed seminars: Filter sem_date < CURDATE()
- Seminar by topic: Join with seminars_topic
- Seminar by speaker: Filter by subject/speaker
"""
