"""Trainee module schema for LLM SQL generation. Only table/column names — no credentials."""

TRAINEE_SCHEMA = """
TRMS Trainee module schema.

IMPORTANT STATUS RULES:
- status = 1 means active record where applicable.
- is_approved = 1 usually means approved trainee/application where applicable.
- office_id is used for office-wise filtering.
- In trainee-related questions, prefer tra_masters for trainee training/admission records.
- users table stores user profile/name/mobile/email.
- training_calendars table stores batch/calendar information.
- courses table stores course details.

Allowed Trainee Tables and Columns:

Table: tra_masters
Columns:
- user_id
- ct_id
- course_id
- office_id
- email
- course_code
- role
- desi_id
- service_id
- grade_id
- application_id
- controlling_officer
- zone_id
- div_id
- depo_id
- station_id
- dep_id
- group_id
- posted_at
- certy_no
- certy_approve
- certi_ap_user
- certi_ap_desi
- representative
- remarks
- user_log
- pass_file
- nomination_letter
- rank
- local_trainee
- status
- out_stay
- pass_status
- is_approved
- is_approved_date
- created_at
- updated_at

Business meaning:
- tra_masters stores trainee enrollment/application/training records.
- tra_masters.user_id joins with users.id.
- tra_masters.course_id joins with training_calendars.id.
- training_calendars.ct_id joins with courses.id.
- tra_masters.office_id is office filter.
- tra_masters.status = 1 means active trainee record.
- tra_masters.is_approved = 1 means approved trainee.

Table: users
Columns:
- id
- role_id
- office_id
- user_code
- user_type
- desi_id
- designation
- parent_id
- cti
- prefix
- name
- mobile
- whatsapp_number
- emergency_numbers
- office_mobile
- emg_mobile_no
- email
- office_email
- aadhar
- uan
- name_hindi
- s_name
- father_name
- father_name_hindi
- controlling_office
- experience_rail
- gender
- language
- birth_date
- date_of_appointment
- railway_join_date
- retire_date
- posting_date
- blood
- pf_no
- food
- ph
- marital
- category
- country_code
- account_office
- country
- upsc_year
- upsc_rank
- upsc_state
- organization
- useful
- qualification
- additional_qualification
- bank_id
- bank_acc
- ifsc_code
- service_id
- grade_id
- zone_id
- div_id
- depo_id
- station_id
- dep_id
- group_id
- comp_id
- grade_pay
- pay_level
- pay_basic
- posted_at
- permanent_address
- present_address
- permanent_identity
- city
- resi_address
- representative
- android_id
- photo
- signature
- password
- lang
- status
- hrms_id
- mod_rec
- is_approved
- ex_is_approved
- forced
- created_by
- created_at
- updated_at

Business meaning:
- users stores trainee/user personal profile.
- users.id joins with tra_masters.user_id and exam_marks.user_id.
- users.name is trainee/person name.
- Use LOWER(users.name) LIKE LOWER('%name%') for case-insensitive trainee name search.
- users.gender can be used for gender-wise trainee count.
- users.status = 1 means active user where applicable.
- Do NOT select password column.
- Avoid selecting sensitive identity/contact columns unless user specifically asks and role allows.

Table: training_calendars
Columns:
- id
- cf_id
- ct_id
- cg_id
- office_id
- course_code
- batch_no
- course_batch
- program_name
- program_name_hindi
- class_id
- from_date
- to_date
- extended_date
- seat
- exam_note
- working_days
- file_no
- course_director
- examiner
- cd
- cd_user_id
- ccd
- dir_desig
- dir_user_id
- ati
- modes
- mcdo
- feedback
- feedback_vl
- place
- short_code
- cancel
- reason
- copy_by
- fail_status
- status
- created_at
- updated_at

Business meaning:
- training_calendars stores course batch/calendar.
- training_calendars.id joins with tra_masters.course_id.
- training_calendars.ct_id joins with courses.id.
- training_calendars.office_id is office filter.
- from_date and to_date are used for year/month/date range and ongoing/completed training logic.
- status = 1 means active calendar.

Table: courses
Columns:
- id
- cf_id
- cg_id
- office_id
- course_name
- course_name_hindi
- cs_code
- cs_description
- cs_duration
- week_days
- certificate
- feed_type
- online_exam
- sort_no
- status
- created_at
- updated_at

Business meaning:
- courses stores course/training information.
- courses.office_id is office filter.
- courses.status = 1 means active course.

Table: course_for
Columns:
- id
- office_id
- course_for
- types
- type_name
- status
- sort_no
- created_at
- updated_at

Business meaning:
- course_for stores course category/department/wing such as Establishment, Transportation, S&T, Medical, Engineering etc.
- course_for.id can join with courses.cf_id where applicable.
- status = 1 means active.

Table: cs_designs
Columns:
- id
- course_id
- zone_id
- library
- mess
- hostel
- sports
- store
- status
- created_at
- updated_at

Business meaning:
- cs_designs stores course service/design flags.
- course_id joins with courses.id.
- hostel/mess/library/sports/store flags may indicate which facilities are included.
- status = 1 means active.

Table: hostel_buildings
Columns:
- id
- office_id
- building_name (e.g., 'GEETANJALEE (गीतांजली)', 'CHETAK (चेतक)', 'ARAVLI (अरावली)')
- bed_capacity
- location
- status
- created_at
- updated_at

Business meaning:
- hostel_buildings stores hostel building master data.
- building_name contains the hostel name like Geetanjali, Chetak, Aravali, etc.
- status = 1 means active building.
- When filtering by building name, use: hostel_buildings.building_name LIKE '%Geetanjali%'

Table: hostel_masters
Columns:
- id
- user_id
- office_id
- building_id
- room_id
- course_id
- in_date
- out_date
- beds
- food
- mess
- h_status
- created_at
- updated_at

Business meaning:
- hostel_masters stores trainee hostel allotment/check-in/check-out records.
- hostel_masters.user_id joins with users.id.
- hostel_masters.building_id joins with hostel_buildings.id.
- h_status = 1 means currently staying/active allotment.
- When finding trainees in a specific building, join: hostel_masters.building_id = hostel_buildings.id

Table: hostel_rooms
Columns:
- id
- building_id
- office_id
- room_name
- room_beds
- floor
- ac
- toilet
- status

Business meaning:
- hostel_rooms stores room details.
- building_id joins with hostel_buildings.id.
- room_beds is number of beds in the room.

Table: rail_zones
Columns:
- id
- zone_code (e.g., 'NWR', 'WCR', 'CR') - USE THIS for filtering
- zone_name (full name like 'North Western Railway')
- zone_name_hindi

Table: divisions
Columns:
- id
- division (division name)
- zone_id

Business meaning:
- rail_zones stores railway zones.
- zone_code is the short code like 'NWR', 'WCR', 'CR' - USE zone_code for filtering.
- zone_name is the full descriptive name.
- divisions stores railway divisions within zones.
- depots stores depots within divisions.
- Use rail_zones.zone_code (not zone_name) to filter trainees by zone code like 'NWR', 'WCR'.

Table: depots
Columns:
- id
- depot (depot name)
- div_id

Recommended Relationships:
- tra_masters.user_id = users.id
- tra_masters.course_id = training_calendars.id
- training_calendars.ct_id = courses.id
- courses.cf_id = course_for.id
- cs_designs.course_id = courses.id
- tra_masters.zone_id = rail_zones.id (for zone name filtering)
- tra_masters.div_id = divisions.id (for division name filtering)
- tra_masters.depo_id = depots.id (for depot name filtering)
- users.zone_id = rail_zones.id (alternative for zone filtering)

Office Filtering:
- Prefer tra_masters.office_id = {office_id} for trainee records.
- Also use training_calendars.office_id = {office_id} or courses.office_id = {office_id} when joining course/calendar.
- Always enforce office_id from backend/login context, not from user text.

Common Question Mapping:
- trainee count: COUNT(*) from tra_masters joined with users if needed.
- active trainees: tra_masters.status = 1.
- approved trainees: tra_masters.is_approved = 1.
- trainee by name: join users and use LOWER(users.name) LIKE LOWER('%name%').
- ongoing trainees/training: use training_calendars.from_date <= CURDATE() AND training_calendars.to_date >= CURDATE().
- completed training: training_calendars.to_date < CURDATE().
- upcoming training: training_calendars.from_date > CURDATE().
- course/batch-wise trainees: group by training_calendars.course_batch or courses.course_name.
- gender-wise trainees: group by users.gender.
- zone/division/depot/station-wise trainees: JOIN with rail_zones/divisions/depots tables and filter by zone_code/division/depot.
- trainees in a specific hostel/building (e.g., 'Geetanjali', 'Chetak', 'Aravali'): 
  1. JOIN hostel_masters ON tra_masters.user_id = hostel_masters.user_id
  2. JOIN hostel_buildings ON hostel_masters.building_id = hostel_buildings.id
  3. Filter: hostel_buildings.building_name LIKE '%Geetanjali%' AND hostel_masters.h_status = 1
- IMPORTANT: When user asks for zone by CODE (like 'NWR', 'WCR'), JOIN rail_zones ON tra_masters.zone_id = rail_zones.id AND filter by rail_zones.zone_code (NOT zone_name).

CRITICAL - RECENT/LATEST/CURRENT COURSE RULES:
- "recent course", "latest course", "current course", "recent batch", "latest batch" means the LATEST training_calendars record by from_date DESC.
- DO NOT use YEAR(CURDATE()) for "recent course" - it means latest batch, not current year.
- For "recent/latest course trainees": ORDER BY training_calendars.from_date DESC LIMIT 1, then count tra_masters.
- For "current course" (ongoing): use training_calendars.from_date <= CURDATE() AND training_calendars.to_date >= CURDATE().
- For "this year" or "2026": then use YEAR(training_calendars.from_date) = 2026.

Example - "how many student join recent course?":
SELECT tc.course_batch, c.course_name, tc.from_date, COUNT(tm.user_id) AS trainee_count
FROM training_calendars tc
JOIN courses c ON c.id = tc.ct_id
LEFT JOIN tra_masters tm ON tm.course_id = tc.id AND tm.status = 1
WHERE tc.office_id = {office_id} AND tc.status = 1
GROUP BY tc.id, tc.course_batch, c.course_name, tc.from_date
ORDER BY tc.from_date DESC
LIMIT 1;
"""
