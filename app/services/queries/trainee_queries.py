"""Trainee and Training module query handlers."""

import datetime

TEMPLATES = [
    {"id": "TOTAL_TRAINEES", "description": "total trainees / how many trainees"},
    {"id": "ACTIVE_TRAINEES", "description": "active trainees"},
    {"id": "APPROVED_TRAINEES", "description": "approved trainees"},                
    {"id": "TRAINEE_LIST", "description": "Trainee list. Params: limit, offset"},
    {"id": "SEARCH_TRAINEE", "description": "Search trainee by name. Params: trainee_name"},
    {"id": "TRAINEE_PROFILE", "description": "trainee profile / trainee full profile. Params: trainee_id"},
    {"id": "TRAINEES_BY_GENDER", "description": "Trainees by gender"},
    {"id": "TRAINEES_BY_DEPARTMENT", "description": "Trainees by department"},
    {"id": "TRAINEES_JOINED_YEAR", "description": "joined last year / Trainees joined in year. Params: year"},
    {"id": "TRAINEES_JOINED_MONTH_WISE", "description": "Trainees joined month-wise. Params: year"},
    {"id": "BIRTH_YEAR_DISTRIBUTION", "description": "birth year distribution / birth year"},
    {"id": "AGE_DISTRIBUTION", "description": "age distribution / age"},
    {"id": "TOTAL_TRAININGS", "description": "Total training calendars"},
    {"id": "ONGOING_TRAININGS", "description": "Ongoing trainings"},
    {"id": "UPCOMING_TRAININGS", "description": "Upcoming trainings"},
    {"id": "COMPLETED_TRAININGS", "description": "Completed trainings"},
    {"id": "TRAINEES_IN_ONE_TRAINING", "description": "Trainees in one training. Params: training_calendar_id"},
    {"id": "TRAINING_WISE_TRAINEE_COUNT", "description": "Training-wise trainee count"},
    {"id": "TRAINEES_ENROLLED_IN_COURSE", "description": "List all trainees enrolled in a course. Params: course_id"},
    {"id": "COURSES_TRAINEE_ATTENDED", "description": "All courses a trainee has attended. Params: user_id"},
    {"id": "IS_TRAINEE_ENROLLED_IN_COURSE", "description": "Is a specific trainee enrolled in a course? Params: user_id, course_id"},
    {"id": "COUNT_TRAINEES_PER_COURSE", "description": "Count trainees enrolled per course"},
    {"id": "TRAINEES_NOT_APPROVED_IN_COURSE", "description": "Trainees not yet approved in a course. Params: course_id"},
    {"id": "LOCAL_VS_OUTSTATION_TRAINEES", "description": "Local vs outstation trainee count per course. Params: course_id"},
    {"id": "TRAINEES_BY_DESIGNATION_IN_COURSE", "description": "Trainees by designation in a course. Params: course_id"},
    {"id": "TRAINEES_BY_DIVISION_ZONE_IN_COURSE", "description": "Trainees by division/zone in a course. Params: course_id"},
    {"id": "SEARCH_TRAINEE_BY_NAME_ACROSS_COURSES", "description": "Search trainee by name across all courses. Params: name_like"},
    {"id": "ACTIVE_TRAINING_BATCHES", "description": "List all active training batches"},
    {"id": "RUNNING_BATCHES", "description": "Currently running batches"},
    {"id": "UPCOMING_BATCHES_DETAILS", "description": "Upcoming batches"},
    {"id": "DETAILS_OF_BATCH", "description": "Get details of a specific batch. Params: ct_id"},
    {"id": "BATCHES_IN_DATE_RANGE", "description": "Batches within a date range. Params: from_date, to_date"},
    {"id": "SEAT_AVAILABILITY_IN_BATCH", "description": "Seat availability in a batch. Params: ct_id"},
    {"id": "BATCHES_OF_SPECIFIC_COURSE", "description": "All batches of a specific course. Params: course_id"},
    {"id": "ATTENDANCE_FOR_TRAINEE_IN_COURSE", "description": "Attendance for a trainee in a course. Params: user_id, course_id"},
    {"id": "DAY_WISE_ATTENDANCE_COUNT", "description": "Day-wise attendance count for a course. Params: course_id"},
    {"id": "ATTENDANCE_PERCENTAGE_PER_TRAINEE", "description": "Attendance percentage per trainee in a course. Params: course_id"},
    {"id": "TRAINEES_LOW_ATTENDANCE", "description": "Trainees with low attendance (below threshold). Params: course_id, min_pct"},
    {"id": "ABSENT_ON_DATE", "description": "Who was absent on a specific date? Params: course_id, att_date"},
    {"id": "TODAYS_ATTENDANCE_SUMMARY", "description": "Today's attendance summary for a course. Params: course_id"},
    {"id": "ATTENDANCE_SUMMARY_FOR_TRAINEE", "description": "Attendance summary for a trainee (all courses). Params: user_id"},
    {"id": "APPROVED_CERTIFICATES_IN_COURSE", "description": "Trainees with approved certificates in a course. Params: course_id"},
    {"id": "PENDING_CERTIFICATE_APPROVALS", "description": "Pending certificate approvals"},
    {"id": "CERTIFICATE_DETAILS_FOR_TRAINEE", "description": "Certificate details for a specific trainee. Params: user_id"},
    {"id": "NOMINEES_FOR_BATCH", "description": "All nominees for a batch. Params: ct_id"},
    {"id": "PENDING_NOMINEE_APPROVALS", "description": "Pending nominee approvals"},
    {"id": "NOMINEE_COUNT_PER_COURSE", "description": "Nominee count per course"},
    {"id": "LINEN_ISSUED_IN_COURSE", "description": "Linen issued to trainees in a course. Params: course_id"},
    {"id": "LINEN_PENDING_RETURNS", "description": "Linen not yet returned (pending returns). Params: course_id"},
    {"id": "ALL_FIELD_TRAINING_RECORDS", "description": "All field training records. Params: course_id"},
    {"id": "FIELD_TRAINING_BY_YEAR", "description": "Field training by year. Params: year"},
    {"id": "LEAVE_RECORDS_FOR_USER", "description": "Leave records for a user. Params: user_id"},
    {"id": "TRAINEES_ON_LEAVE_TODAY", "description": "Trainees on leave today"},
    {"id": "TRAINEE_ENROLLMENT_TREND", "description": "Trainee count per month (enrollment trend). Params: year"},
    {"id": "TOP_COURSES_BY_TRAINEE_COUNT", "description": "Top courses by trainee count"},
    {"id": "DEPARTMENT_WISE_TRAINEE_COUNT", "description": "Department-wise trainee count"},
    {"id": "COMPLETE_TRAINING_HISTORY", "description": "Complete training history of a trainee. Params: user_id"},
    {"id": "PASS_RATE_VS_ATTENDANCE", "description": "Pass rate vs attendance correlation. Params: course_id"}
]

def execute(query_id, params, cur, office_id):
    p = params or {}
    
    if query_id == "TOTAL_TRAINEES":
        cur.execute("SELECT COUNT(*) AS total_trainees FROM tra_masters WHERE office_id = %s", (office_id,))
        r = cur.fetchone()
        return f"Total trainees: {r['total_trainees'] if r else 0}"

    elif query_id == "ACTIVE_TRAINEES":
        cur.execute("""
            SELECT COUNT(tm.id) AS active_trainees
            FROM tra_masters tm 
            LEFT JOIN training_calendars tc ON tc.id = tm.course_id AND tc.status = 1 
            WHERE tc.from_date <= CURDATE()
            AND tc.to_date >= CURDATE() 
            AND tm.office_id = %s 
            AND tm.status = 1 
            AND tm.is_approved = 1
        """, (office_id,))
        r = cur.fetchone()
        return f"Active trainees: {r['active_trainees'] if r else 0}"

    elif query_id == "APPROVED_TRAINEES":
        cur.execute("SELECT COUNT(*) AS approved_trainees FROM tra_masters WHERE office_id = %s AND is_approved = 1", (office_id,))
        r = cur.fetchone()
        return f"Approved trainees: {r['approved_trainees'] if r else 0}"

    elif query_id == "TRAINEE_LIST":
        limit = int(p.get("limit", 20))
        offset = int(p.get("offset", 0))
        cur.execute("""
            SELECT tm.id, u.name, u.user_code 
            FROM tra_masters tm 
            JOIN users u ON u.id = tm.user_id 
            WHERE tm.office_id = %s 
            ORDER BY tm.id DESC 
            LIMIT %s OFFSET %s
        """, (office_id, limit, offset))
        rows = cur.fetchall()
        if not rows: return "No trainees found."
        lines = [f"- {r.get('name', 'Unknown')} (Code: {r.get('user_code', 'N/A')})" for r in rows]
        return f"Trainees:\n" + "\n".join(lines)

    elif query_id == "SEARCH_TRAINEE":
        name = p.get("trainee_name", "")
        if not name: return "Please specify a trainee name."
        cur.execute("""
            SELECT tm.id, u.name, u.user_code, tm.gender 
            FROM tra_masters tm 
            JOIN users u ON u.id = tm.user_id 
            WHERE tm.office_id = %s AND u.name LIKE %s 
            LIMIT 20
        """, (office_id, f"%{name}%"))
        rows = cur.fetchall()
        if not rows: return f"No trainee found matching '{name}'."
        lines = [f"- {r.get('name', 'Unknown')} (Code: {r.get('user_code', 'N/A')}, Gender: {r.get('gender')})" for r in rows]
        return f"Search Results for '{name}':\n" + "\n".join(lines)

    elif query_id == "TRAINEE_PROFILE":
        tid = p.get("trainee_id")
        if not tid: return "Please specify a trainee_id."
        cur.execute("SELECT * FROM tra_masters WHERE office_id = %s AND id = %s", (office_id, tid))
        r = cur.fetchone()
        if not r: return f"No profile found for trainee ID {tid}."
        return f"Trainee Profile:\nName: {r.get('trainee_name')}\nDOB: {r.get('dob')}\nGender: {r.get('gender')}\nDept: {r.get('department_id')}"

    elif query_id == "TRAINEES_BY_GENDER":
        cur.execute("SELECT gender, COUNT(*) AS total FROM tra_masters WHERE office_id = %s GROUP BY gender", (office_id,))
        rows = cur.fetchall()
        if not rows: return "No gender data found."
        lines = [f"- {r['gender'] or 'Unknown'}: {r['total']}" for r in rows]
        return "Trainees by Gender:\n" + "\n".join(lines)

    elif query_id == "TRAINEES_BY_DEPARTMENT":
        cur.execute("SELECT department_id, COUNT(*) AS total FROM tra_masters WHERE office_id = %s GROUP BY department_id ORDER BY total DESC", (office_id,))
        rows = cur.fetchall()
        if not rows: return "No department data found."
        lines = [f"- Dept {r['department_id'] or 'Unknown'}: {r['total']}" for r in rows]
        return "Trainees by Department:\n" + "\n".join(lines)

    elif query_id == "TRAINEES_JOINED_YEAR":
        year = int(p.get("year", datetime.datetime.now().year))
        cur.execute("SELECT COUNT(*) AS total_joined FROM tra_masters WHERE office_id = %s AND YEAR(created_at) = %s", (office_id, year))
        r = cur.fetchone()
        return f"Trainees joined in {year}: {r['total_joined'] if r else 0}"

    elif query_id == "TRAINEES_JOINED_MONTH_WISE":
        year = int(p.get("year", datetime.datetime.now().year))
        cur.execute("SELECT MONTH(created_at) AS month, COUNT(*) AS total FROM tra_masters WHERE office_id = %s AND YEAR(created_at) = %s GROUP BY MONTH(created_at) ORDER BY month", (office_id, year))
        rows = cur.fetchall()
        if not rows: return f"No trainees joined in {year}."
        lines = [f"- Month {r['month']}: {r['total']}" for r in rows]
        return f"Trainees joined month-wise in {year}:\n" + "\n".join(lines)

    elif query_id == "BIRTH_YEAR_DISTRIBUTION":
        cur.execute("SELECT YEAR(dob) AS birth_year, COUNT(*) AS total FROM tra_masters WHERE office_id = %s AND dob IS NOT NULL GROUP BY YEAR(dob) ORDER BY birth_year", (office_id,))
        rows = cur.fetchall()
        if not rows: return "No DOB data found."
        lines = [f"- {r['birth_year']}: {r['total']}" for r in rows]
        return "Birth Year Distribution:\n" + "\n".join(lines)

    elif query_id == "AGE_DISTRIBUTION":
        cur.execute("SELECT TIMESTAMPDIFF(YEAR, dob, CURDATE()) AS age, COUNT(*) AS total FROM tra_masters WHERE office_id = %s AND dob IS NOT NULL GROUP BY age ORDER BY age", (office_id,))
        rows = cur.fetchall()
        if not rows: return "No age data found."
        lines = [f"- Age {r['age']}: {r['total']}" for r in rows]
        return "Age Distribution:\n" + "\n".join(lines)

    elif query_id == "TOTAL_TRAININGS":
        cur.execute("SELECT COUNT(*) AS total_trainings FROM training_calendars WHERE office_id = %s", (office_id,))
        r = cur.fetchone()
        return f"Total training calendars: {r['total_trainings'] if r else 0}"

    elif query_id == "ONGOING_TRAININGS":
        cur.execute("SELECT COUNT(*) AS ongoing_trainings FROM training_calendars WHERE office_id = %s AND status = 1 AND CURDATE() BETWEEN from_date AND to_date", (office_id,))
        r = cur.fetchone()
        return f"Ongoing trainings: {r['ongoing_trainings'] if r else 0}"

    elif query_id == "UPCOMING_TRAININGS":
        cur.execute("SELECT COUNT(*) AS upcoming_trainings FROM training_calendars WHERE office_id = %s AND status = 1 AND from_date > CURDATE()", (office_id,))
        r = cur.fetchone()
        return f"Upcoming trainings: {r['upcoming_trainings'] if r else 0}"

    elif query_id == "COMPLETED_TRAININGS":
        cur.execute("SELECT COUNT(*) AS completed_trainings FROM training_calendars WHERE office_id = %s AND status = 1 AND to_date < CURDATE()", (office_id,))
        r = cur.fetchone()
        return f"Completed trainings: {r['completed_trainings'] if r else 0}"

    elif query_id == "TRAINEES_IN_ONE_TRAINING":
        tcid = p.get("training_calendar_id")
        if not tcid: return "Please specify a training_calendar_id."
        cur.execute("SELECT COUNT(*) AS total_trainees FROM training_calendars_nominee WHERE office_id = %s AND training_calendar_id = %s", (office_id, tcid))
        r = cur.fetchone()
        return f"Total trainees in training {tcid}: {r['total_trainees'] if r else 0}"

    elif query_id == "TRAINING_WISE_TRAINEE_COUNT":
        cur.execute('''SELECT tc.id AS training_calendar_id, tc.from_date, tc.to_date, COUNT(tcn.id) AS total_trainees 
            FROM training_calendars tc 
            LEFT JOIN training_calendars_nominee tcn ON tcn.training_calendar_id = tc.id AND tcn.office_id = tc.office_id 
            WHERE tc.office_id = %s GROUP BY tc.id, tc.from_date, tc.to_date ORDER BY tc.from_date DESC''', (office_id,))
        rows = cur.fetchall()
        if not rows: return "No training data found."
        lines = [f"- Training ID {r['training_calendar_id']} ({r['from_date']} to {r['to_date']}): {r['total_trainees']} trainees" for r in rows]
        return "Training-wise Trainee Count:\n" + "\n".join(lines)

    # 40 New Queries Added
    elif query_id == "TRAINEES_ENROLLED_IN_COURSE":
        cid = p.get("course_id")
        if not cid: return "Please specify course_id."
        cur.execute("SELECT tm.id, u.name, u.user_code, u.gender, u.designation, u.mobile, tm.role, tm.posted_at, tm.local_trainee, CASE tm.status WHEN 1 THEN 'Active' ELSE 'Inactive' END AS status, tm.is_approved FROM tra_masters tm JOIN users u ON u.id = tm.user_id WHERE tm.course_id = %s AND tm.office_id = %s AND tm.status = 1 ORDER BY u.name", (cid, office_id))
        rows = cur.fetchall()
        if not rows: return "No enrolled trainees found."
        lines = [f"- {r.get('name')} ({r.get('status')})" for r in rows[:50]]
        return f"Enrolled Trainees in Course {cid}:\n" + "\n".join(lines)

    elif query_id == "COURSES_TRAINEE_ATTENDED":
        uid = p.get("user_id")
        if not uid: return "Please specify user_id."
        cur.execute("SELECT c.course_name, tc.course_batch, tc.from_date, tc.to_date, tc.batch_no, tm.role, tm.certy_no, CASE tm.certy_approve WHEN 1 THEN 'Yes' ELSE 'No' END AS cert_approved, CASE tm.status WHEN 1 THEN 'Active' ELSE 'Inactive' END AS status FROM tra_masters tm JOIN courses c ON c.id = tm.course_id LEFT JOIN training_calendars tc ON tc.id = tm.ct_id WHERE tm.user_id = %s AND tm.office_id = %s ORDER BY tc.from_date DESC", (uid, office_id))
        rows = cur.fetchall()
        if not rows: return f"No courses attended by user {uid}."
        lines = [f"- {r.get('course_name')} ({r.get('from_date')} to {r.get('to_date')})" for r in rows[:50]]
        return f"Courses Attended by User {uid}:\n" + "\n".join(lines)

    elif query_id == "IS_TRAINEE_ENROLLED_IN_COURSE":
        uid = p.get("user_id")
        cid = p.get("course_id")
        if not uid or not cid: return "Please specify user_id and course_id."
        cur.execute("SELECT tm.id, tm.role, tm.posted_at, tm.is_approved, tm.certy_no, tc.from_date, tc.to_date, tc.batch_no, CASE tm.status WHEN 1 THEN 'Active' ELSE 'Inactive' END AS status FROM tra_masters tm LEFT JOIN training_calendars tc ON tc.id = tm.ct_id WHERE tm.user_id = %s AND tm.course_id = %s LIMIT 1", (uid, cid))
        r = cur.fetchone()
        if not r: return "Trainee is not enrolled in this course."
        return f"Trainee is enrolled. Status: {r.get('status')}, Approved: {'Yes' if r.get('is_approved') else 'No'}"

    elif query_id == "COUNT_TRAINEES_PER_COURSE":
        cur.execute("SELECT c.course_name, c.cs_code, COUNT(tm.id) AS total_enrolled, SUM(IF(tm.is_approved=1,1,0)) AS approved, SUM(IF(tm.is_approved=0,1,0)) AS pending_approval FROM tra_masters tm JOIN courses c ON c.id = tm.course_id WHERE tm.office_id = %s AND tm.status = 1 GROUP BY tm.course_id, c.course_name, c.cs_code ORDER BY total_enrolled DESC", (office_id,))
        rows = cur.fetchall()
        if not rows: return "No trainee enrollment data found."
        lines = [f"- {r.get('course_name')}: {r.get('total_enrolled')} (Approved: {r.get('approved')})" for r in rows[:50]]
        return "Trainees Per Course:\n" + "\n".join(lines)

    elif query_id == "TRAINEES_NOT_APPROVED_IN_COURSE":
        cid = p.get("course_id")
        if not cid: return "Please specify course_id."
        cur.execute("SELECT u.name, u.user_code, u.mobile, u.designation, tm.posted_at, tm.created_at AS enrolled_on FROM tra_masters tm JOIN users u ON u.id = tm.user_id WHERE tm.course_id = %s AND tm.office_id = %s AND tm.is_approved = 0 AND tm.status = 1 ORDER BY tm.created_at", (cid, office_id))
        rows = cur.fetchall()
        if not rows: return "No pending approvals found."
        lines = [f"- {r.get('name')} (Enrolled On: {r.get('enrolled_on')})" for r in rows[:50]]
        return f"Not Approved Trainees in Course {cid}:\n" + "\n".join(lines)

    elif query_id == "LOCAL_VS_OUTSTATION_TRAINEES":
        cid = p.get("course_id")
        if not cid: return "Please specify course_id."
        cur.execute("SELECT SUM(IF(local_trainee=1,1,0)) AS local_trainees, SUM(IF(local_trainee=0,1,0)) AS outstation_trainees, COUNT(*) AS total FROM tra_masters WHERE course_id = %s AND status = 1", (cid,))
        r = cur.fetchone()
        if not r: return "No data found."
        return f"Local vs Outstation Trainees in Course {cid}:\nLocal: {r.get('local_trainees')}\nOutstation: {r.get('outstation_trainees')}\nTotal: {r.get('total')}"

    elif query_id == "TRAINEES_BY_DESIGNATION_IN_COURSE":
        cid = p.get("course_id")
        if not cid: return "Please specify course_id."
        cur.execute("SELECT d.desi_name, COUNT(tm.id) AS count FROM tra_masters tm JOIN users u ON u.id = tm.user_id LEFT JOIN designations d ON d.id = u.desi_id WHERE tm.course_id = %s AND tm.status = 1 GROUP BY u.desi_id, d.desi_name ORDER BY count DESC", (cid,))
        rows = cur.fetchall()
        if not rows: return "No designation data found."
        lines = [f"- {r.get('desi_name') or 'N/A'}: {r.get('count')}" for r in rows[:50]]
        return f"Trainees by Designation in Course {cid}:\n" + "\n".join(lines)

    elif query_id == "TRAINEES_BY_DIVISION_ZONE_IN_COURSE":
        cid = p.get("course_id")
        if not cid: return "Please specify course_id."
        cur.execute("SELECT z.zone_name, dv.division, COUNT(tm.id) AS count FROM tra_masters tm LEFT JOIN zones z ON z.id = tm.zone_id LEFT JOIN divisions dv ON dv.id = tm.div_id WHERE tm.course_id = %s AND tm.status = 1 GROUP BY tm.zone_id, tm.div_id, z.zone_name, dv.division ORDER BY count DESC", (cid,))
        rows = cur.fetchall()
        if not rows: return "No division/zone data found."
        lines = [f"- Zone {r.get('zone_name') or 'N/A'}, Div {r.get('division') or 'N/A'}: {r.get('count')}" for r in rows[:50]]
        return f"Trainees by Division/Zone in Course {cid}:\n" + "\n".join(lines)

    elif query_id == "SEARCH_TRAINEE_BY_NAME_ACROSS_COURSES":
        name = p.get("name_like", "")
        if not name: return "Please specify name_like."
        cur.execute("SELECT u.name, u.user_code, u.designation, c.course_name, tc.from_date, tc.to_date, tm.role, tm.is_approved FROM tra_masters tm JOIN users u ON u.id = tm.user_id JOIN courses c ON c.id = tm.course_id LEFT JOIN training_calendars tc ON tc.id = tm.ct_id WHERE u.name LIKE %s AND tm.office_id = %s ORDER BY tc.from_date DESC", (f"%{name}%", office_id))
        rows = cur.fetchall()
        if not rows: return "No matching trainees found."
        lines = [f"- {r.get('name')} in {r.get('course_name')} ({r.get('from_date')} to {r.get('to_date')})" for r in rows[:50]]
        return f"Search Results for '{name}':\n" + "\n".join(lines)

    elif query_id == "ACTIVE_TRAINING_BATCHES":
        cur.execute("SELECT tc.id, tc.course_batch, tc.batch_no, c.course_name, tc.from_date, tc.to_date, tc.seat, tc.working_days, tc.course_director, tc.examiner, CASE tc.status WHEN 1 THEN 'Active' ELSE 'Cancelled' END AS status FROM training_calendars tc JOIN courses c ON c.id = tc.cf_id WHERE tc.office_id = %s AND tc.status = 1 ORDER BY tc.from_date DESC", (office_id,))
        rows = cur.fetchall()
        if not rows: return "No active training batches found."
        lines = [f"- {r.get('course_batch')} (Batch {r.get('batch_no')}): {r.get('from_date')} to {r.get('to_date')}" for r in rows[:50]]
        return "Active Training Batches:\n" + "\n".join(lines)

    elif query_id == "RUNNING_BATCHES":
        cur.execute("SELECT tc.course_batch, tc.batch_no, c.course_name, tc.from_date, tc.to_date, tc.seat, tc.working_days, DATEDIFF(tc.to_date, CURDATE()) AS days_remaining FROM training_calendars tc JOIN courses c ON c.id = tc.cf_id WHERE tc.office_id = %s AND tc.status = 1 AND CURDATE() BETWEEN tc.from_date AND tc.to_date ORDER BY tc.from_date", (office_id,))
        rows = cur.fetchall()
        if not rows: return "No running batches found."
        lines = [f"- {r.get('course_batch')}: Ends in {r.get('days_remaining')} days" for r in rows[:50]]
        return "Running Batches:\n" + "\n".join(lines)

    elif query_id == "UPCOMING_BATCHES_DETAILS":
        cur.execute("SELECT tc.course_batch, c.course_name, tc.from_date, tc.to_date, tc.seat, DATEDIFF(tc.from_date, CURDATE()) AS starts_in_days FROM training_calendars tc JOIN courses c ON c.id = tc.cf_id WHERE tc.office_id = %s AND tc.status = 1 AND tc.from_date > CURDATE() ORDER BY tc.from_date", (office_id,))
        rows = cur.fetchall()
        if not rows: return "No upcoming batches found."
        lines = [f"- {r.get('course_batch')}: Starts in {r.get('starts_in_days')} days ({r.get('from_date')})" for r in rows[:50]]
        return "Upcoming Batches:\n" + "\n".join(lines)

    elif query_id == "DETAILS_OF_BATCH":
        ct_id = p.get("ct_id")
        if not ct_id: return "Please specify ct_id."
        cur.execute("SELECT tc.*, c.course_name, c.cs_code, c.cs_duration FROM training_calendars tc JOIN courses c ON c.id = tc.cf_id WHERE tc.id = %s", (ct_id,))
        r = cur.fetchone()
        if not r: return "Batch details not found."
        return f"Batch Details:\nCourse: {r.get('course_name')}\nBatch: {r.get('course_batch')} (No. {r.get('batch_no')})\nDates: {r.get('from_date')} to {r.get('to_date')}\nSeats: {r.get('seat')}"

    elif query_id == "BATCHES_IN_DATE_RANGE":
        f_date = p.get("from_date")
        t_date = p.get("to_date")
        if not f_date or not t_date: return "Please specify from_date and to_date."
        cur.execute("SELECT tc.course_batch, c.course_name, tc.from_date, tc.to_date, tc.seat, tc.working_days FROM training_calendars tc JOIN courses c ON c.id = tc.cf_id WHERE tc.office_id = %s AND tc.from_date BETWEEN %s AND %s AND tc.status = 1 ORDER BY tc.from_date", (office_id, f_date, t_date))
        rows = cur.fetchall()
        if not rows: return "No batches found in the specified range."
        lines = [f"- {r.get('course_batch')}: {r.get('from_date')} to {r.get('to_date')}" for r in rows[:50]]
        return f"Batches from {f_date} to {t_date}:\n" + "\n".join(lines)

    elif query_id == "SEAT_AVAILABILITY_IN_BATCH":
        ct_id = p.get("ct_id")
        if not ct_id: return "Please specify ct_id."
        cur.execute("SELECT tc.seat AS total_seats, COUNT(tm.id) AS enrolled, (tc.seat - COUNT(tm.id)) AS available FROM training_calendars tc LEFT JOIN tra_masters tm ON tm.ct_id = tc.id AND tm.status = 1 WHERE tc.id = %s GROUP BY tc.id, tc.seat", (ct_id,))
        r = cur.fetchone()
        if not r: return "Batch details not found."
        return f"Seat Availability for Batch {ct_id}:\nTotal: {r.get('total_seats')}\nEnrolled: {r.get('enrolled')}\nAvailable: {r.get('available')}"

    elif query_id == "BATCHES_OF_SPECIFIC_COURSE":
        cid = p.get("course_id")
        if not cid: return "Please specify course_id."
        cur.execute("SELECT tc.id, tc.batch_no, tc.course_batch, tc.from_date, tc.to_date, tc.seat, CASE tc.status WHEN 1 THEN 'Active' ELSE 'Cancelled' END AS status FROM training_calendars tc WHERE tc.cf_id = %s AND tc.office_id = %s ORDER BY tc.from_date DESC", (cid, office_id))
        rows = cur.fetchall()
        if not rows: return "No batches found for this course."
        lines = [f"- {r.get('course_batch')}: {r.get('from_date')} to {r.get('to_date')} ({r.get('status')})" for r in rows[:50]]
        return f"Batches of Course {cid}:\n" + "\n".join(lines)

    elif query_id == "ATTENDANCE_FOR_TRAINEE_IN_COURSE":
        uid = p.get("user_id")
        cid = p.get("course_id")
        if not uid or not cid: return "Please specify user_id and course_id."
        cur.execute("SELECT DATE(punch_time) AS att_date, punch_time, punch, CASE a_b WHEN 0 THEN 'Present' WHEN 1 THEN 'Absent' END AS status, remarks FROM attendances WHERE user_id = %s AND course_id = %s AND status = 1 ORDER BY punch_time", (uid, cid))
        rows = cur.fetchall()
        if not rows: return "No attendance records found."
        lines = [f"- {r.get('att_date')}: {r.get('status')} ({r.get('punch')})" for r in rows[:50]]
        return f"Attendance for Trainee {uid} in Course {cid}:\n" + "\n".join(lines)

    elif query_id == "DAY_WISE_ATTENDANCE_COUNT":
        cid = p.get("course_id")
        if not cid: return "Please specify course_id."
        cur.execute("SELECT DATE(punch_time) AS att_date, COUNT(*) AS total_punches, SUM(IF(a_b=0,1,0)) AS present, SUM(IF(a_b=1,1,0)) AS absent FROM attendances WHERE course_id = %s AND status = 1 GROUP BY DATE(punch_time) ORDER BY att_date", (cid,))
        rows = cur.fetchall()
        if not rows: return "No day-wise attendance data found."
        lines = [f"- {r.get('att_date')}: {r.get('present')} Present, {r.get('absent')} Absent" for r in rows[:50]]
        return f"Day-wise Attendance Count in Course {cid}:\n" + "\n".join(lines)

    elif query_id == "ATTENDANCE_PERCENTAGE_PER_TRAINEE":
        cid = p.get("course_id")
        if not cid: return "Please specify course_id."
        cur.execute("SELECT u.name, u.user_code, COUNT(a.id) AS total_days, SUM(IF(a.a_b=0,1,0)) AS present_days, SUM(IF(a.a_b=1,1,0)) AS absent_days, ROUND(SUM(IF(a.a_b=0,1,0))*100.0/NULLIF(COUNT(a.id),0),1) AS att_pct FROM attendances a JOIN users u ON u.id = a.user_id WHERE a.course_id = %s AND a.status = 1 GROUP BY a.user_id, u.name, u.user_code ORDER BY att_pct DESC", (cid,))
        rows = cur.fetchall()
        if not rows: return "No attendance percentage data found."
        lines = [f"- {r.get('name')}: {r.get('att_pct')}% ({r.get('present_days')}/{r.get('total_days')} days)" for r in rows[:50]]
        return f"Attendance Percentage Per Trainee in Course {cid}:\n" + "\n".join(lines)

    elif query_id == "TRAINEES_LOW_ATTENDANCE":
        cid = p.get("course_id")
        min_pct = p.get("min_pct", 75)
        if not cid: return "Please specify course_id."
        cur.execute("SELECT u.name, u.user_code, u.mobile, COUNT(a.id) AS total_days, SUM(IF(a.a_b=0,1,0)) AS present, ROUND(SUM(IF(a.a_b=0,1,0))*100.0/NULLIF(COUNT(a.id),0),1) AS att_pct FROM attendances a JOIN users u ON u.id = a.user_id WHERE a.course_id = %s AND a.status = 1 GROUP BY a.user_id, u.name, u.user_code HAVING att_pct < %s ORDER BY att_pct ASC", (cid, min_pct))
        rows = cur.fetchall()
        if not rows: return "No trainees with low attendance."
        lines = [f"- {r.get('name')}: {r.get('att_pct')}% ({r.get('present')}/{r.get('total_days')} days)" for r in rows[:50]]
        return f"Trainees with Attendance Below {min_pct}% in Course {cid}:\n" + "\n".join(lines)

    elif query_id == "ABSENT_ON_DATE":
        cid = p.get("course_id")
        att_date = p.get("att_date")
        if not cid or not att_date: return "Please specify course_id and att_date."
        cur.execute("SELECT u.name, u.user_code, u.mobile, u.designation FROM attendances a JOIN users u ON u.id = a.user_id WHERE a.course_id = %s AND DATE(a.punch_time) = %s AND a.a_b = 1 AND a.status = 1 ORDER BY u.name", (cid, att_date))
        rows = cur.fetchall()
        if not rows: return "No one was absent on this date."
        lines = [f"- {r.get('name')} ({r.get('designation')})" for r in rows[:50]]
        return f"Absent Trainees on {att_date} in Course {cid}:\n" + "\n".join(lines)

    elif query_id == "TODAYS_ATTENDANCE_SUMMARY":
        cid = p.get("course_id")
        if not cid: return "Please specify course_id."
        cur.execute("SELECT COUNT(*) AS total_punched, SUM(IF(a_b=0,1,0)) AS present, SUM(IF(a_b=1,1,0)) AS absent FROM attendances WHERE course_id = %s AND DATE(punch_time) = CURDATE() AND status = 1", (cid,))
        r = cur.fetchone()
        if not r: return "No attendance recorded today."
        return f"Today's Attendance Summary in Course {cid}:\nTotal: {r.get('total_punched')}\nPresent: {r.get('present')}\nAbsent: {r.get('absent')}"

    elif query_id == "ATTENDANCE_SUMMARY_FOR_TRAINEE":
        uid = p.get("user_id")
        if not uid: return "Please specify user_id."
        cur.execute("SELECT c.course_name, COUNT(a.id) AS total_days, SUM(IF(a.a_b=0,1,0)) AS present, SUM(IF(a.a_b=1,1,0)) AS absent, ROUND(SUM(IF(a.a_b=0,1,0))*100.0/NULLIF(COUNT(a.id),0),1) AS att_pct FROM attendances a JOIN courses c ON c.id = a.course_id WHERE a.user_id = %s AND a.status = 1 GROUP BY a.course_id, c.course_name ORDER BY att_pct", (uid,))
        rows = cur.fetchall()
        if not rows: return "No attendance summary found."
        lines = [f"- {r.get('course_name')}: {r.get('att_pct')}% ({r.get('present')} Present, {r.get('absent')} Absent)" for r in rows[:50]]
        return f"Attendance Summary for Trainee {uid}:\n" + "\n".join(lines)

    elif query_id == "APPROVED_CERTIFICATES_IN_COURSE":
        cid = p.get("course_id")
        if not cid: return "Please specify course_id."
        cur.execute("SELECT u.name, u.user_code, tm.certy_no, tm.is_approved_date, tm.pass_status FROM tra_masters tm JOIN users u ON u.id = tm.user_id WHERE tm.course_id = %s AND tm.office_id = %s AND tm.certy_approve = 1 AND tm.status = 1 ORDER BY u.name", (cid, office_id))
        rows = cur.fetchall()
        if not rows: return "No approved certificates found."
        lines = [f"- {r.get('name')}: Cert No. {r.get('certy_no')} (Passed: {r.get('pass_status')})" for r in rows[:50]]
        return f"Approved Certificates in Course {cid}:\n" + "\n".join(lines)

    elif query_id == "PENDING_CERTIFICATE_APPROVALS":
        cur.execute("SELECT u.name, u.user_code, c.course_name, tc.from_date, tc.to_date, tm.created_at AS enrolled_on FROM tra_masters tm JOIN users u ON u.id = tm.user_id JOIN courses c ON c.id = tm.course_id LEFT JOIN training_calendars tc ON tc.id = tm.ct_id WHERE tm.office_id = %s AND tm.certy_approve = 0 AND tm.status = 1 ORDER BY tc.from_date DESC", (office_id,))
        rows = cur.fetchall()
        if not rows: return "No pending certificate approvals."
        lines = [f"- {r.get('name')} in {r.get('course_name')}" for r in rows[:50]]
        return "Pending Certificate Approvals:\n" + "\n".join(lines)

    elif query_id == "CERTIFICATE_DETAILS_FOR_TRAINEE":
        uid = p.get("user_id")
        if not uid: return "Please specify user_id."
        cur.execute("SELECT c.course_name, tc.from_date, tc.to_date, tm.certy_no, tm.certy_approve, tm.is_approved_date, tm.pass_status FROM tra_masters tm JOIN courses c ON c.id = tm.course_id LEFT JOIN training_calendars tc ON tc.id = tm.ct_id WHERE tm.user_id = %s AND tm.office_id = %s AND tm.certy_approve = 1 ORDER BY tc.from_date DESC", (uid, office_id))
        rows = cur.fetchall()
        if not rows: return "No certificate details found."
        lines = [f"- {r.get('course_name')}: Cert No. {r.get('certy_no')} ({r.get('is_approved_date')})" for r in rows[:50]]
        return f"Certificate Details for Trainee {uid}:\n" + "\n".join(lines)

    elif query_id == "NOMINEES_FOR_BATCH":
        ct_id = p.get("ct_id")
        if not ct_id: return "Please specify ct_id."
        cur.execute("SELECT u.name, u.user_code, u.designation, u.mobile, tmn.posted_at, tmn.zone_id, tmn.div_id, CASE tmn.is_approved WHEN 1 THEN 'Approved' ELSE 'Pending' END AS status, tmn.created_at AS nominated_on FROM tra_masters_nominee tmn JOIN users u ON u.id = tmn.user_id WHERE tmn.ct_id = %s AND tmn.office_id = %s AND tmn.status = 1 ORDER BY u.name", (ct_id, office_id))
        rows = cur.fetchall()
        if not rows: return "No nominees found."
        lines = [f"- {r.get('name')} ({r.get('status')})" for r in rows[:50]]
        return f"Nominees for Batch {ct_id}:\n" + "\n".join(lines)

    elif query_id == "PENDING_NOMINEE_APPROVALS":
        cur.execute("SELECT u.name, u.user_code, c.course_name, tmn.posted_at, tmn.created_at AS nominated_on FROM tra_masters_nominee tmn JOIN users u ON u.id = tmn.user_id JOIN courses c ON c.id = tmn.course_id WHERE tmn.office_id = %s AND tmn.is_approved = 0 AND tmn.status = 1 ORDER BY tmn.created_at", (office_id,))
        rows = cur.fetchall()
        if not rows: return "No pending nominee approvals."
        lines = [f"- {r.get('name')} in {r.get('course_name')}" for r in rows[:50]]
        return "Pending Nominee Approvals:\n" + "\n".join(lines)

    elif query_id == "NOMINEE_COUNT_PER_COURSE":
        cur.execute("SELECT c.course_name, COUNT(tmn.id) AS total_nominees, SUM(IF(tmn.is_approved=1,1,0)) AS approved, SUM(IF(tmn.is_approved=0,1,0)) AS pending FROM tra_masters_nominee tmn JOIN courses c ON c.id = tmn.course_id WHERE tmn.office_id = %s AND tmn.status = 1 GROUP BY tmn.course_id, c.course_name ORDER BY total_nominees DESC", (office_id,))
        rows = cur.fetchall()
        if not rows: return "No nominee count data found."
        lines = [f"- {r.get('course_name')}: {r.get('total_nominees')} (Approved: {r.get('approved')})" for r in rows[:50]]
        return "Nominee Count Per Course:\n" + "\n".join(lines)

    elif query_id == "LINEN_ISSUED_IN_COURSE":
        cid = p.get("course_id")
        if not cid: return "Please specify course_id."
        cur.execute("SELECT u.name, u.user_code, tl.pillow_issue, tl.cumble_issue, tl.bedsheet_issue, tl.bedsheet2_issue, tl.bedsheet3_issue, tl.balti_issue, tl.jug_issue, tl.pillow_return, tl.cumble_return, tl.bedsheet_return FROM trainee_linens tl JOIN users u ON u.id = tl.user_id WHERE tl.course_id = %s AND tl.status = 1 ORDER BY u.name", (cid,))
        rows = cur.fetchall()
        if not rows: return "No linen issued records found."
        lines = [f"- {r.get('name')}: Pillow({r.get('pillow_issue')}), Cumble({r.get('cumble_issue')}), Bedsheet({r.get('bedsheet_issue')})" for r in rows[:50]]
        return f"Linen Issued in Course {cid}:\n" + "\n".join(lines)

    elif query_id == "LINEN_PENDING_RETURNS":
        cid = p.get("course_id")
        if not cid: return "Please specify course_id."
        cur.execute("SELECT u.name, u.user_code, u.mobile, (tl.pillow_issue - tl.pillow_return) AS pillow_pending, (tl.cumble_issue - tl.cumble_return) AS cumble_pending, (tl.bedsheet_issue - tl.bedsheet_return) AS bedsheet_pending, (tl.balti_issue - tl.balti_return) AS balti_pending, (tl.jug_issue - tl.jug_return) AS jug_pending FROM trainee_linens tl JOIN users u ON u.id = tl.user_id WHERE tl.course_id = %s AND tl.status = 1 AND (tl.pillow_issue > tl.pillow_return OR tl.cumble_issue > tl.cumble_return OR tl.bedsheet_issue > tl.bedsheet_return) ORDER BY u.name", (cid,))
        rows = cur.fetchall()
        if not rows: return "No pending linen returns."
        lines = [f"- {r.get('name')}: Pillow({r.get('pillow_pending')}), Cumble({r.get('cumble_pending')}), Bedsheet({r.get('bedsheet_pending')})" for r in rows[:50]]
        return f"Pending Linen Returns in Course {cid}:\n" + "\n".join(lines)

    elif query_id == "ALL_FIELD_TRAINING_RECORDS":
        cid = p.get("course_id")
        if not cid: return "Please specify course_id."
        cur.execute("SELECT ft.from_date, ft.return_date, ft.total_trainee, u.name AS staff_name, ft.car_number, ft.remarks, CASE ft.f_status WHEN 1 THEN 'Approved' ELSE 'Pending' END AS status FROM field_training ft LEFT JOIN users u ON u.id = ft.staff_id WHERE ft.course_id LIKE %s AND ft.status = 1 ORDER BY ft.from_date", (f"%{cid}%",))
        rows = cur.fetchall()
        if not rows: return "No field training records found."
        lines = [f"- {r.get('from_date')} to {r.get('return_date')}: {r.get('total_trainee')} Trainees ({r.get('status')})" for r in rows[:50]]
        return f"Field Training Records for Course {cid}:\n" + "\n".join(lines)

    elif query_id == "FIELD_TRAINING_BY_YEAR":
        year = int(p.get("year", datetime.datetime.now().year))
        cur.execute("SELECT ft.year, ft.from_date, ft.return_date, ft.total_trainee, u.name AS staff_name, ft.car_number, ft.remarks FROM field_training ft LEFT JOIN users u ON u.id = ft.staff_id WHERE ft.year = %s AND ft.status = 1 ORDER BY ft.from_date", (year,))
        rows = cur.fetchall()
        if not rows: return "No field training found."
        lines = [f"- {r.get('from_date')} to {r.get('return_date')}: {r.get('total_trainee')} Trainees (Staff: {r.get('staff_name')})" for r in rows[:50]]
        return f"Field Training in {year}:\n" + "\n".join(lines)

    elif query_id == "LEAVE_RECORDS_FOR_USER":
        uid = p.get("user_id")
        if not uid: return "Please specify user_id."
        cur.execute("SELECT id, type, from_date, to_date, DATEDIFF(to_date, from_date)+1 AS total_days, CASE status WHEN 1 THEN 'Active' ELSE 'Cancelled' END AS status, created_at FROM staff_leave WHERE user_id = %s ORDER BY from_date DESC", (uid,))
        rows = cur.fetchall()
        if not rows: return "No leave records found."
        lines = [f"- {r.get('type')}: {r.get('from_date')} to {r.get('to_date')} ({r.get('total_days')} days)" for r in rows[:50]]
        return f"Leave Records for User {uid}:\n" + "\n".join(lines)

    elif query_id == "TRAINEES_ON_LEAVE_TODAY":
        cur.execute("SELECT u.name, u.user_code, u.designation, sl.from_date, sl.to_date, sl.type, DATEDIFF(sl.to_date, CURDATE()) AS days_remaining FROM staff_leave sl JOIN users u ON u.id = sl.user_id WHERE sl.status = 1 AND CURDATE() BETWEEN sl.from_date AND sl.to_date ORDER BY u.name")
        rows = cur.fetchall()
        if not rows: return "No trainees on leave today."
        lines = [f"- {r.get('name')}: {r.get('type')} ({r.get('days_remaining')} days remaining)" for r in rows[:50]]
        return "Trainees on Leave Today:\n" + "\n".join(lines)

    elif query_id == "TRAINEE_ENROLLMENT_TREND":
        year = int(p.get("year", datetime.datetime.now().year))
        cur.execute("SELECT MONTH(created_at) AS month_no, MONTHNAME(created_at) AS month_name, COUNT(*) AS enrollments FROM tra_masters WHERE office_id = %s AND YEAR(created_at) = %s AND status = 1 GROUP BY MONTH(created_at) ORDER BY month_no", (office_id, year))
        rows = cur.fetchall()
        if not rows: return "No enrollment trend data found."
        lines = [f"- {r.get('month_name')}: {r.get('enrollments')} enrollments" for r in rows[:50]]
        return f"Enrollment Trend for {year}:\n" + "\n".join(lines)

    elif query_id == "TOP_COURSES_BY_TRAINEE_COUNT":
        cur.execute("SELECT c.course_name, c.cs_code, COUNT(tm.id) AS total_trainees, SUM(IF(tm.is_approved=1,1,0)) AS approved FROM tra_masters tm JOIN courses c ON c.id = tm.course_id WHERE tm.office_id = %s AND tm.status = 1 GROUP BY tm.course_id, c.course_name, c.cs_code ORDER BY total_trainees DESC LIMIT 10", (office_id,))
        rows = cur.fetchall()
        if not rows: return "No top courses data found."
        lines = [f"- {r.get('course_name')}: {r.get('total_trainees')} Trainees" for r in rows]
        return "Top 10 Courses by Trainee Count:\n" + "\n".join(lines)

    elif query_id == "DEPARTMENT_WISE_TRAINEE_COUNT":
        cur.execute("SELECT dep.department_name, COUNT(tm.id) AS count FROM tra_masters tm JOIN departments dep ON dep.id = tm.dep_id WHERE tm.office_id = %s AND tm.status = 1 GROUP BY tm.dep_id, dep.department_name ORDER BY count DESC", (office_id,))
        rows = cur.fetchall()
        if not rows: return "No department-wise trainee count data found."
        lines = [f"- {r.get('department_name')}: {r.get('count')} Trainees" for r in rows[:50]]
        return "Department-wise Trainee Count:\n" + "\n".join(lines)

    elif query_id == "COMPLETE_TRAINING_HISTORY":
        uid = p.get("user_id")
        if not uid: return "Please specify user_id."
        cur.execute("SELECT course_name, from_date, to_date, DATEDIFF(to_date,from_date)+1 AS duration_days, training_place, CASE status WHEN 1 THEN 'Active' ELSE 'Inactive' END AS status FROM complete_training WHERE user_id = %s AND office_id = %s ORDER BY from_date DESC", (uid, office_id))
        rows = cur.fetchall()
        if not rows: return "No complete training history found."
        lines = [f"- {r.get('course_name')}: {r.get('from_date')} to {r.get('to_date')} ({r.get('duration_days')} days)" for r in rows[:50]]
        return f"Complete Training History for User {uid}:\n" + "\n".join(lines)

    elif query_id == "PASS_RATE_VS_ATTENDANCE":
        cid = p.get("course_id")
        if not cid: return "Please specify course_id."
        cur.execute("SELECT u.name, u.user_code, ROUND(SUM(IF(a.a_b=0,1,0))*100.0/NULLIF(COUNT(DISTINCT DATE(a.punch_time)),0),1) AS att_pct, MAX(CAST(em.mark_obtained AS UNSIGNED)) AS best_mark, MAX(em.total_mark) AS total_mark, CASE MAX(em.result) WHEN 1 THEN 'Pass' WHEN 2 THEN 'Fail' ELSE 'Pending' END AS result FROM tra_masters tm JOIN users u ON u.id = tm.user_id LEFT JOIN attendances a ON a.user_id = tm.user_id AND a.course_id = tm.course_id LEFT JOIN exam_marks em ON em.user_id = tm.user_id AND em.course_id = tm.course_id WHERE tm.course_id = %s AND tm.status = 1 GROUP BY tm.user_id, u.name, u.user_code ORDER BY att_pct DESC", (cid,))
        rows = cur.fetchall()
        if not rows: return "No data found."
        lines = [f"- {r.get('name')}: Att {r.get('att_pct')}%, Marks {r.get('best_mark')}/{r.get('total_mark')} ({r.get('result')})" for r in rows[:50]]
        return f"Pass Rate vs Attendance for Course {cid}:\n" + "\n".join(lines)

    return None
