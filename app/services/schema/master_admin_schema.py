"""Master Admin module schema for LLM SQL generation."""

MASTER_ADMIN_SCHEMA = """
TRMS Master Admin module schema.

Important rules:
- status = 1 means active record where applicable.
- office_id is used for office-wise filtering where available.
- Always enforce office_id from backend/login context.
- Do not select users.password.
- Use case-insensitive search for names: LOWER(users.name) LIKE LOWER('%name%')

Allowed tables and columns:

Table: users
Columns:
- id
- role_id
- office_id

Table: roles
Columns:
- id
- office_id

Table: permissions
Columns:
- id
- permission

Table: perm_types
Columns:
- id
- type

Table: accesses
Columns:
- id
- user_id
- perm_id
- office_id
- created_at
- updated_at

Table: services
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

Table: grades
Columns:
- id
- grade

Table: grade_pay
Columns:
- id
- level_id
- basic
- status
- created_at
- updated_at

Table: pay_level
Columns:
- id
- level

Table: pay_scale
Columns:
- id
- scale

Table: rail_zones
Columns:
- id
- zone_code (e.g., 'NWR', 'WCR', 'CR')
- zone_name (full name like 'North Western Railway')
- zone_name_hindi

Table: divisions
Columns:
- id
- division

Table: depots
Columns:
- id
- depots

Table: rail_stations
Columns:
- id
- st_name

Table: states
Columns:
- id
- state

Table: places
Columns:
- id
- office_id

Table: company
Columns:
- id
- comp_name

Table: bank
Columns:
- id
- bank_name

Table: holidays
Columns:
- id
- office_id
- holiday_name (varchar) - Name of the holiday
- holiday_date (date) - Date of the holiday
- created_at
- updated_at

Table: site_info
Columns:
- id
- office_id

Business meaning:
- users, roles, permissions, accesses for RBAC.
- services, departments, designations for organization.
- grades, grade_pay, pay_level, pay_scale for pay structure.
- rail_zones.zone_code for zone codes like 'NWR', 'WCR'. Use zone_code for filtering by short codes.
- states, places for geography.
- company, bank for masters.
- holidays for holiday calendar.
- site_info for site configuration.

Recommended relationships:
- users.role_id = roles.id
- accesses.user_id = users.id
- accesses.perm_id = permissions.id
- departments.service_id = services.id
- designations.grade_id = grades.id
- grade_pay.level_id = pay_level.id

Common question mapping:
- Total users: Count users
- Role-wise users: Group by roles
- Departments list: Query departments
- Designations list: Query designations
- Zones/Divisions: Query rail_zones, divisions
- Active users: Filter by status
"""
