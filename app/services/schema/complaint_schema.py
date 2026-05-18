"""Complaint module schema for LLM SQL generation."""

COMPLAINT_SCHEMA = """
TRMS Complaint module schema.

Important rules:
- status = 1 means active record where applicable.
- office_id is used for office-wise filtering where available.
- Always enforce office_id from backend/login context.
- Do not select users.password.
- Use case-insensitive search for names: LOWER(users.name) LIKE LOWER('%name%')

Allowed tables and columns:

Table: complaints
Columns:
- id
- office_id
- cm_no
- building_id

Table: complaints_files
Columns:
- id
- cm_id
- attachment
- status
- created_at
- updated_at

Table: complaint_cat
Columns:
- id
- comp_name

Table: complaint_subcat
Columns:
- id
- cat_id
- subcat_name

Table: comp_categories
Columns:
- id
- parent_id
- agent_id

Table: users
Columns:
- id
- role_id
- office_id

Table: hostel_buildings
Columns:
- id
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
- complaints stores main complaint records.
- complaints_files stores complaint attachments.
- complaint_cat stores complaint categories.
- complaint_subcat stores complaint subcategories.
- comp_categories stores complaint classification.
- users for complainant information.
- hostel_buildings for building-related complaints.
- departments, designations for organization info.

Recommended relationships:
- complaints.building_id = hostel_buildings.id
- complaints_files.cm_id = complaints.id
- complaint_subcat.cat_id = complaint_cat.id

Common question mapping:
- Total complaints: Count complaints
- Pending complaints: Filter by status
- Complaint by category: Join with complaint_cat
- Complaint by building: Join with hostel_buildings
- Complaint attachments: Query complaints_files
"""
