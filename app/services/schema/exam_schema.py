"""Exam module schema for LLM SQL generation. Only table/column names — no credentials."""

EXAM_SCHEMA = """
TRMS Exam module schema.

IMPORTANT STATUS RULES:
- status = 1 means active record.
- exam_marks.result = 0 means trainee did not appear in exam.
- exam_marks.result = 1 means trainee passed.
- exam_marks.result = 2 means trainee failed.

Allowed Exam Tables and Columns:

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
- courses.office_id is used for office-wise filtering.
- courses.status = 1 means active course.

Table: et_design
Columns:
- id
- course_id
- subject
- exam_date
- start_time
- end_time
- faculty
- class_id
- examiner
- status
- created_at
- updated_at

Business meaning:
- et_design stores exam schedule / exam timetable.
- et_design.course_id joins with training_calendars.id.
- et_design.subject joins with subjects.id.
- et_design.status = 1 means active schedule.

Table: exam_design
Columns:
- id
- cs_id
- subject_id
- total_marks
- minimum_marks
- mcq
- essay
- office_id
- desi_id
- type_sort
- status
- created_at
- updated_at

Business meaning:
- exam_design stores exam setup/design for course and subject.
- exam_design.cs_id usually refers to courses.id.
- exam_design.subject_id joins with subjects.id.
- exam_design.office_id can be used for office filtering.
- exam_design.minimum_marks is passing marks.
- exam_design.total_marks is total marks.
- exam_design.status = 1 means active design.

Table: exam_marks
Columns:
- id
- user_id
- course_id
- exam_type_id
- subject_id
- mark_obtained
- re_exam_mark
- total_mark
- result
- re_exam_result
- status
- created_at
- updated_at

Business meaning:
- exam_marks stores trainee marks/result.
- exam_marks.user_id joins with users.id.
- exam_marks.subject_id joins with subjects.id.
- exam_marks.exam_type_id joins with exam_type.id.
- exam_marks.result = 0 means not appeared.
- exam_marks.result = 1 means pass.
- exam_marks.result = 2 means fail.
- exam_marks.status = 1 means active mark record.
- In this project, exam_marks.course_id joins with training_calendars.id in existing queries.
- Then training_calendars.ct_id joins with courses.id.
- CRITICAL: exam_marks.mark_obtained is VARCHAR. When sorting by marks, you must cast it: ORDER BY CAST(exam_marks.mark_obtained AS UNSIGNED) DESC. Without casting, alphabetical sorting will incorrectly rank non-numeric values like 'Q' at the top.

Table: exam_type
Columns:
- id
- title
- title_hindi
- total_mark
- weightage
- status
- created_at
- updated_at

Business meaning:
- exam_type stores exam type/test type.
- exam_type.status = 1 means active exam type.

Table: subjects
Columns:
- id
- subject_name
- subject_name_hindi
- total_mark
- status
- created_at
- updated_at

Business meaning:
- subjects stores subject details.
- subjects.status = 1 means active subject.
- subjects.id joins with exam_marks.subject_id, et_design.subject, and exam_design.subject_id.

Table: users
Columns:
- id
- name
- email
- status
- created_at
- updated_at

Business meaning:
- users stores trainee/user details.
- users.id joins with exam_marks.user_id.
- users.name can be used for trainee name search.
- Use case-insensitive search for names using LOWER(users.name) LIKE LOWER('%name%').

Table: training_calendars
Columns:
- id
- ct_id
- course_batch
- from_date
- to_date
- status
- created_at
- updated_at

Business meaning:
- training_calendars stores course batch/calendar.
- training_calendars.id joins with exam_marks.course_id.
- training_calendars.ct_id joins with courses.id.
- training_calendars.status = 1 means active calendar.

Recommended Relationships:
- exam_marks.user_id = users.id
- exam_marks.subject_id = subjects.id
- exam_marks.exam_type_id = exam_type.id
- exam_marks.course_id = training_calendars.id
- training_calendars.ct_id = courses.id
- et_design.course_id = training_calendars.id
- et_design.subject = subjects.id
- exam_design.cs_id = courses.id
- exam_design.subject_id = subjects.id

Office Filtering:
- Prefer courses.office_id = {office_id}
- If using exam_design directly, exam_design.office_id = {office_id} is also available.
- Always enforce office filtering from backend/login context, not from user text.

Default Active Filters:
- Use status = 1 for active records when applicable.

Question Mapping Rules:
- If user asks pass trainees, use exam_marks.result = 1.
- If user asks failed trainees, use exam_marks.result = 2.
- If user asks not appeared trainees, use exam_marks.result = 0.
- If user asks upcoming/completed exam schedule, use et_design.exam_date.
- If user asks exam timetable/schedule, use et_design.
- If user asks marks/result, use exam_marks.
- If user asks exam type/test type, use exam_type.
- If user asks passing marks/minimum marks, use exam_design.minimum_marks.
"""
