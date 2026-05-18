"""Hostel module schema for LLM SQL generation. Only table/column names — no credentials."""

HOSTEL_SCHEMA = """
TRMS Hostel module schema.

IMPORTANT STATUS RULES:

status = 1 means active record where applicable.
office_id is used for office-wise filtering.
hostel_buildings stores hostel/building capacity.
hostel_rooms stores rooms and bed capacity per room.
hostel_masters stores trainee hostel allotment/check-in/check-out records.
all_dues stores dues and facility flags.
complaints stores complaint records, including hostel complaints.
tra_masters and users may be used to get trainee details.

Allowed Hostel Tables and Columns:

Table: hostel_buildings
Columns:

id
office_id
building_name
bed_capacity
location
desi_id
sort_no
status
created_at
updated_at

Business meaning:

hostel_buildings stores hostel/building master data.
hostel_buildings.bed_capacity is total capacity of that hostel building.
hostel_buildings.office_id is office filter.
status = 1 means active building.

Table: hostel_rooms
Columns:

id
building_id
office_id
room_name
room_beds
r_category
floor
ac
toilet
remarks
sort_no
status
created_at
updated_at
direction

Business meaning:

hostel_rooms stores room details.
hostel_rooms.building_id joins with hostel_buildings.id.
hostel_rooms.office_id is office filter.
hostel_rooms.room_beds is number of beds in room.
status = 1 means active room.

Table: hostel_masters
Columns:

id
user_id
role_id
office_id
room_type
person
amount
ct_id
course_id
train_no
ph
receipt_no
building_id
room_id
beds
food
in_date
out_date
days
item_id
mess
plusbed
remark
charge
total_charges
extra_room
preference
tour
hostel_dues
room_log
h_status
status
created_at
updated_at

Business meaning:

hostel_masters stores hostel allotment/check-in/check-out/occupancy.
hostel_masters.user_id joins with users.id.
hostel_masters.building_id joins with hostel_buildings.id.
hostel_masters.room_id joins with hostel_rooms.id.
hostel_masters.course_id joins with training_calendars.id (NOT courses.id directly).
hostel_masters.office_id is office filter.
in_date and out_date are used for occupancy date range.
If out_date is future or NULL-like, trainee may currently be staying.
beds indicates booked/used beds for allotment if available.
h_status and status indicate hostel/allotment state. Use status = 1 for active records unless question needs history.

IMPORTANT - Getting Course Names:
- hostel_masters.course_id -> training_calendars.id -> training_calendars.ct_id -> courses.id -> courses.course_name
- To get course name: JOIN training_calendars tc ON hm.course_id = tc.id, then JOIN courses c ON tc.ct_id = c.id, then select c.course_name
- NEVER use tra_masters.course_name directly - it doesn't exist. Always join through training_calendars.

Table: training_calendars
Columns:
- id
- ct_id (links to courses.id)
- office_id
- course_batch
- from_date
- to_date
- status

Business meaning:
- training_calendars stores course batch/calendar information.
- ct_id joins with courses.id to get course details.
- course_batch is the batch number (e.g., 75, 76).
- status = 1 means active calendar.

Table: courses
Columns:
- id
- course_name (e.g., 'Induction Course for Clerk/Sr. Clerk/OS', 'OS/S&WI Promotion (20%-LDCE)')
- office_id
- status

Business meaning:
- courses stores course master data with course names.
- To get course name in hostel queries: JOIN training_calendars ON hostel_masters.course_id = training_calendars.id, then JOIN courses ON training_calendars.ct_id = courses.id

Table: all_dues
Columns:

id
course_id
zone_id
library
mess
hostel
sports
store
status
created_at
updated_at

Business meaning:

all_dues stores dues/facility usage flags for a course or trainee/course context.
hostel = 1 may indicate hostel dues/facility applicable.
mess = 1 may indicate mess dues/facility applicable.
course_id can join with courses.id or training calendar/course context depending existing code.
status = 1 means active.

Table: complaints
Columns:

id
office_id
cm_no
building_id
ctype_id
ctype_sub_id
user_id
forwarded_to
description
remarks
remarks_log
rating
review
attachment
cm_status
status
created_at
updated_at

Business meaning :

complaints stores complaint records.
Hostel complaints may use building_id or complaint category/type fields.
complaints.office_id is office filter.
complaints.building_id joins with hostel_buildings.id where applicable.
complaints.user_id joins with users.id.
cm_status may indicate complaint workflow status.
status = 1 means active complaint.

Table: users
Columns:

id
role_id
office_id
user_code
user_type
desi_id
designation
parent_id
cti
prefix
name
mobile
whatsapp_number
emergency_numbers
office_mobile
emg_mobile_no
email
office_email
aadhar
uan
name_hindi
s_name
father_name
father_name_hindi
controlling_office
experience_rail
gender
language
birth_date
date_of_appointment
railway_join_date
retire_date
posting_date
blood
pf_no
food
ph
marital
category
country_code
account_office
country
upsc_year
upsc_rank
upsc_state
organization
useful
qualification
additional_qualification
bank_id
bank_acc
ifsc_code
service_id
grade_id
zone_id
div_id
depo_id
station_id
dep_id
group_id
comp_id
grade_pay
pay_level
pay_basic
posted_at
permanent_address
present_address
permanent_identity
city
resi_address
representative
android_id
photo
signature
password
lang
status
hrms_id
mod_rec
is_approved
ex_is_approved
forced
created_by
created_at
updated_at

Business meaning:

users stores trainee/user profile.
users.id joins with hostel_masters.user_id and complaints.user_id.
users.name is trainee/person name.
Use LOWER(users.name) LIKE LOWER('%name%') for case-insensitive name search.
Do NOT select password column.
Avoid selecting sensitive identity/contact columns unless specifically needed and allowed.

Table: tra_masters
Columns:

user_id
ct_id
course_id
office_id
email
course_code
role
desi_id
service_id
grade_id
application_id
controlling_officer
zone_id
div_id
depo_id
station_id
dep_id
group_id
posted_at
certy_no
certy_approve
certi_ap_user
certi_ap_desi
representative
remarks
user_log
pass_file
nomination_letter
rank
local_trainee
status
out_stay
pass_status
is_approved
is_approved_date
created_at
updated_at

Business meaning:

tra_masters stores trainee enrollment/training records.
tra_masters.user_id joins with users.id.
tra_masters.course_id joins with training_calendars.id.
tra_masters.office_id is office filter.

Table: training_calendars
Columns:

id
cf_id
ct_id
cg_id
office_id
course_code
batch_no
course_batch
program_name
program_name_hindi
class_id
from_date
to_date
extended_date
seat
exam_note
working_days
file_no
course_director
examiner
cd
cd_user_id
ccd
dir_desig
dir_user_id
ati
modes
mcdo
feedback
feedback_vl
place
short_code
cancel
reason
copy_by
fail_status
status
created_at
updated_at

Business meaning:

training_calendars stores course batch/calendar.
training_calendars.id may join with hostel_masters.course_id and tra_masters.course_id.
training_calendars.office_id is office filter.

Table: courses
Columns:

id
cf_id
cg_id
office_id
course_name
course_name_hindi
cs_code
cs_description
cs_duration
week_days
certificate
feed_type
online_exam
sort_no
status
created_at
updated_at

Business meaning:

courses stores course/training details.
courses.office_id is office filter.
courses.status = 1 means active course.

Recommended Relationships:

hostel_rooms.building_id = hostel_buildings.id
hostel_masters.building_id = hostel_buildings.id
hostel_masters.room_id = hostel_rooms.id
hostel_masters.user_id = users.id
complaints.building_id = hostel_buildings.id
complaints.user_id = users.id
hostel_masters.course_id = training_calendars.id
tra_masters.course_id = training_calendars.id
training_calendars.ct_id = courses.id
tra_masters.user_id = users.id

Office Filtering:

Prefer hostel_buildings.office_id = {office_id} for building queries.
Prefer hostel_rooms.office_id = {office_id} for room queries.
Prefer hostel_masters.office_id = {office_id} for allotment/occupancy queries.
Prefer complaints.office_id = {office_id} for complaint queries.
Always enforce office_id from backend/login context, not from user text.

Common Question Mapping:

total hostel buildings: COUNT(*) from hostel_buildings where status = 1.
total rooms: COUNT(*) from hostel_rooms where status = 1.
total beds: SUM(hostel_rooms.room_beds) or SUM(hostel_buildings.bed_capacity), depending question.
occupied/booked beds: SUM(hostel_masters.beds) for active/current allotments.
current occupancy: hostel_masters.in_date <= CURDATE() AND (hostel_masters.out_date IS NULL OR hostel_masters.out_date >= CURDATE()).
available beds: total room beds - occupied/current booked beds.
room-wise occupancy: group by hostel_rooms.room_name.
building-wise occupancy: group by hostel_buildings.building_name.
trainee hostel details: join hostel_masters with users and hostel_rooms/buildings.
hostel complaints: use complaints joined with hostel_buildings where building_id exists.
complaint status summary: group by complaints.cm_status.
"""
