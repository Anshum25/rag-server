"""Sports module schema for LLM SQL generation."""

SPORTS_SCHEMA = """
TRMS Sports module schema.

Important rules:
- status = 1 means active record where applicable.
- office_id is used for office-wise filtering where available.
- Always enforce office_id from backend/login context.
- Do not select users.password.
- Use case-insensitive search for names: LOWER(users.name) LIKE LOWER('%name%')

Allowed tables and columns:

Table: sport
Columns:
- id
- program
- from_date
- to_date
- start_timing
- end_timing
- team

Table: sport_team
Columns:
- id
- program_id

Table: sport_item
Columns:
- id
- office_id
- sport_item

Table: sportitem_issue
Columns:
- id
- office_id

Table: sport_material
Columns:
- id
- office_id
- party_id
- type

Table: sports_photos
Columns:
- id
- sport_id
- sport_photo

Table: srec_sport
Columns:
- id
- office_id
- type_id
- name

Table: particpants
Columns:
- id
- program_id
- participant_id
- team_id

Table: partys
Columns:
- id
- office_id
- p_name
- p_email
- p_mobile
- status
- created_at
- updated_at

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

Business meaning:
- sport stores sports program records.
- sport_team stores team information.
- sport_item stores sports equipment master.
- sportitem_issue stores equipment issue records.
- sport_material stores material purchases.
- sports_photos stores sports event photos.
- srec_sport stores sport records.
- particpants stores participant details.
- partys stores vendor information.
- users for participants/coordinators.

Recommended relationships:
- sport_team.program_id = sport.id
- particpants.program_id = sport.id
- particpants.team_id = sport_team.id
- sportitem_issue links to sport_item
- sport_material.party_id = partys.id
- sports_photos.sport_id = sport.id

Common question mapping:
- Total sports: Count sport
- Upcoming sports: Filter from_date >= CURDATE()
- Sports teams: Query sport_team
- Participants: Count particpants
- Sport items: Query sport_item
- Equipment issued: Query sportitem_issue
"""
