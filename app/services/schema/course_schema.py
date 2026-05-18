"""Course module schema for LLM SQL generation. Only table/column names — no credentials."""

COURSE_SCHEMA = """
TRMS Course module schema.

IMPORTANT STATUS RULES:
- status = 1 means active record where applicable.
- office_id is used for office-wise filtering.
- courses table stores master course information.
- course_for stores department/category/wing like Establishment, Transportation, S&T, Medical, Engineering etc.
- course_groups stores course group like Promotion, Refresher, Initial, Equipment, Special.
- training_calendars stores course batches/calendar.
- cs_designs stores course facilities/services flags like library, mess, hostel, sports, store.

Allowed Course Tables and Columns:

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
- courses stores course master data.
- courses.office_id is office filter.
- courses.cf_id joins with course_for.id.
- courses.cg_id joins with course_groups.id.
- courses.course_name is course name.
- courses.course_name_hindi is Hindi course name.
- courses.cs_code is course code.
- courses.cs_duration is course duration.
- courses.week_days is week/days setting.
- courses.certificate indicates certificate setting.
- courses.online_exam indicates online exam setting.
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
- course_for stores course category/department/wing.
- Example values: ESTABLISHMENT, TRANSPORTATION, SIGNAL & TELECOM, MEDICAL, MECH/ELECT, COMMERCIAL, ENGINEERING, ACCOUNTS, STORE, INFORMATION TECHNOLOGY, MANAGEMENT, STATISTICAL, SPECIAL.
- course_for.id joins with courses.cf_id.
- course_for.office_id is office filter.
- course_for.status = 1 means active course category.

Table: course_groups
Columns:
- id
- cf_id
- office_id
- course_group
- types
- status
- sort_no
- created_at
- updated_at

Business meaning:
- course_groups stores course group/type.
- Example values: Promotion, Refresher, Initial, Equipment, SPECIAL.
- course_groups.id joins with courses.cg_id.
- course_groups.office_id is office filter.
- course_groups.status = 1 means active group.

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
- training_calendars stores course batches/calendar/schedule.
- training_calendars.ct_id joins with courses.id.
- training_calendars.cf_id may join with course_for.id.
- training_calendars.cg_id may join with course_groups.id.
- training_calendars.office_id is office filter.
- course_batch is batch name/code.
- from_date and to_date define course batch duration.
- seat is batch seat capacity.
- status = 1 means active calendar/batch.
- upcoming course: from_date > CURDATE().
- ongoing course: from_date <= CURDATE() AND to_date >= CURDATE().
- completed course: to_date < CURDATE().

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
- cs_designs stores course service/facility flags.
- cs_designs.course_id joins with courses.id.
- library = 1 means library facility enabled.
- mess = 1 means mess facility enabled.
- hostel = 1 means hostel facility enabled.
- sports = 1 means sports facility enabled.
- store = 1 means store facility enabled.
- status = 1 means active design.

Table: degree
Columns:
- id
- degree
- status
- created_at
- updated_at

Business meaning:
- degree stores degree/qualification master.
- Use only if user asks course eligibility/degree-related question.
- status = 1 means active.

Table: departments
Columns:
- id
- service_id
- office_id
- department_name
- sort_no
- status
- created_at
- updated_at

Business meaning:
- departments stores department master data.
- Use only if user asks department-wise course context.
- departments.office_id is office filter.
- status = 1 means active.

Recommended Relationships:
- courses.cf_id = course_for.id
- courses.cg_id = course_groups.id
- training_calendars.ct_id = courses.id
- training_calendars.cf_id = course_for.id
- training_calendars.cg_id = course_groups.id
- cs_designs.course_id = courses.id

Office Filtering:
- Prefer courses.office_id = {office_id} for course master queries.
- Prefer training_calendars.office_id = {office_id} for batch/calendar queries.
- Prefer course_for.office_id = {office_id} for category queries.
- Prefer course_groups.office_id = {office_id} for group queries.
- Always enforce office_id from backend/login context, not from user text.

Common Question Mapping:
- total courses: COUNT(*) from courses where status = 1.
- active courses: courses.status = 1.
- course details: courses by course_name or cs_code.
- department/category wise courses: join courses with course_for.
- group wise courses: join courses with course_groups.
- promotion/refresher/initial courses: use course_groups.course_group.
- online exam courses: courses.online_exam = 1.
- certificate courses: courses.certificate = 1.
- course duration: courses.cs_duration and courses.week_days.
- course batch count: join training_calendars with courses and group by course.
- upcoming batches: training_calendars.from_date > CURDATE().
- ongoing batches: training_calendars.from_date <= CURDATE() AND training_calendars.to_date >= CURDATE().
- completed batches: training_calendars.to_date < CURDATE().
- hostel facility courses: join cs_designs and use cs_designs.hostel = 1.
- mess facility courses: join cs_designs and use cs_designs.mess = 1.
- library facility courses: join cs_designs and use cs_designs.library = 1.
- seat capacity: use training_calendars.seat.
- case-insensitive course search: LOWER(courses.course_name) LIKE LOWER('%name%') OR LOWER(courses.cs_code) LIKE LOWER('%name%').

CRITICAL - RECENT/LATEST/CURRENT COURSE RULES:
- "recent course", "latest course", "current course", "recent batch", "latest batch" means the LATEST training_calendars record by from_date DESC.
- DO NOT use YEAR(CURDATE()) for "recent course" - it means latest batch, not current year.
- For "recent/latest course": ORDER BY training_calendars.from_date DESC LIMIT 1.
- For "current course" (ongoing): use training_calendars.from_date <= CURDATE() AND training_calendars.to_date >= CURDATE().
- For "this year" or "2026": then use YEAR(training_calendars.from_date) = 2026.
- For "recent course trainees": join training_calendars with tra_masters, ORDER BY tc.from_date DESC LIMIT 1, count trainees.

Example - "show recent course details":
SELECT tc.course_batch, c.course_name, tc.from_date, tc.to_date, tc.seat
FROM training_calendars tc
JOIN courses c ON c.id = tc.ct_id
WHERE tc.office_id = {office_id} AND tc.status = 1
ORDER BY tc.from_date DESC
LIMIT 1;
"""
