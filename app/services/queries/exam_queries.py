"""Exam module query templates and handlers."""

TEMPLATES = [
    {"id": "EXAM_PASS_PERCENTAGE", "description": "Pass percentage of trainees. Params: year (optional)"},
    {"id": "EXAM_FAIL_COUNT", "description": "How many trainees failed. Params: year (optional)"},
    {"id": "EXAM_PASS_COUNT", "description": "How many trainees passed. Params: year (optional)"},
    {"id": "EXAM_TOTAL_RECORDS", "description": "Total exam records count. Params: year (optional)"},
    {"id": "EXAM_HIGHEST_MARKS", "description": "Trainee with highest marks. Params: year (optional)"},
    {"id": "EXAM_LOWEST_MARKS", "description": "Trainee with lowest marks. Params: year (optional)"},
    {"id": "EXAM_AVERAGE_MARKS", "description": "Average marks of all trainees. Params: year (optional)"},
    {"id": "EXAM_SUBJECT_HIGHEST_FAILURE", "description": "Subject with highest failure rate. Params: year (optional)"},
    {"id": "EXAM_TOP_PERFORMERS", "description": "Top N performers by marks. Params: limit (default 10), year (optional)"},
    {"id": "EXAM_AVG_MARKS_BY_DEPARTMENT", "description": "Average marks grouped by department/designation. Params: year (optional)"},
    {"id": "EXAM_REPEATED_FAILURES", "description": "Trainees who failed multiple times. Params: min_failures (default 2)"},
    {"id": "EXAM_RE_EXAM_ELIGIBLE", "description": "Trainees eligible for re-exam"},
    {"id": "EXAM_BELOW_THRESHOLD", "description": "Trainees scoring below a percentage. Params: threshold_pct (default 40), year (optional)"},
    {"id": "EXAM_COMPARE_YEARS", "description": "Compare exam results between two years. Params: year1, year2"},
    {"id": "EXAM_TRAINEE_REPORT", "description": "Full exam report for a trainee by name. Params: search_name (required)"},
    {"id": "EXAM_TRAINEE_MARKS_BY_ID", "description": "Marks of a trainee by ID. Params: trainee_id (required)"},
    {"id": "EXAM_SCHEDULE", "description": "Show exam schedule/timetable"},
    {"id": "EXAM_UPCOMING_SCHEDULE", "description": "Upcoming exams in next 7 days"},
    {"id": "EXAM_SUBJECT_WISE_RESULTS", "description": "Results grouped by subject. Params: year (optional)"},
]


def _year_filter(alias="em", param_name="year", year_val=None):
    if year_val:
        return f" AND YEAR({alias}.created_at) = %s", (int(year_val),)
    return "", ()


def _cur_year(cur):
    cur.execute("SELECT YEAR(CURDATE()) AS y")
    return int((cur.fetchone() or {}).get("y") or 2025)


def execute(query_id, params, cur, office_id):
    """Execute exam query. Returns result string or None if not handled."""
    p = params or {}

    if query_id == "EXAM_PASS_PERCENTAGE":
        year = p.get("year")
        yf, yp = _year_filter("em", "year", year)
        cur.execute(f"SELECT COUNT(*) as total, SUM(CASE WHEN result=1 THEN 1 ELSE 0 END) as passed FROM exam_marks em WHERE em.office_id=%s{yf}", (office_id,)+yp)
        r = cur.fetchone()
        if not r or r["total"]==0: return "No exam data found."
        pct = round((r["passed"]/r["total"])*100, 2)
        return f"Pass percentage{f' in {year}' if year else ''}: {pct}% (Passed: {r['passed']} / Total: {r['total']})"

    elif query_id == "EXAM_FAIL_COUNT":
        year = p.get("year")
        yf, yp = _year_filter("em", "year", year)
        cur.execute(f"SELECT COUNT(DISTINCT user_id) as cnt FROM exam_marks em WHERE em.office_id=%s AND result!=1{yf}", (office_id,)+yp)
        r = cur.fetchone()
        return f"Total failed trainees{f' in {year}' if year else ''}: {r['cnt'] if r else 0}"

    elif query_id == "EXAM_PASS_COUNT":
        year = p.get("year")
        yf, yp = _year_filter("em", "year", year)
        cur.execute(f"SELECT COUNT(DISTINCT user_id) as cnt FROM exam_marks em WHERE em.office_id=%s AND result=1{yf}", (office_id,)+yp)
        r = cur.fetchone()
        return f"Total passed trainees{f' in {year}' if year else ''}: {r['cnt'] if r else 0}"

    elif query_id == "EXAM_TOTAL_RECORDS":
        year = p.get("year")
        yf, yp = _year_filter("em", "year", year)
        cur.execute(f"SELECT COUNT(*) as cnt FROM exam_marks em WHERE em.office_id=%s{yf}", (office_id,)+yp)
        r = cur.fetchone()
        return f"Total exam records{f' in {year}' if year else ''}: {r['cnt'] if r else 0}"

    elif query_id == "EXAM_HIGHEST_MARKS":
        year = p.get("year")
        yf, yp = _year_filter("em", "year", year)
        cur.execute(f"""SELECT u.name, em.mark_obtained, em.total_mark, c.course_name, es.subject_name
            FROM exam_marks em LEFT JOIN users u ON u.id=em.user_id LEFT JOIN courses c ON c.id=em.course_id
            LEFT JOIN exam_subject es ON es.id=em.sub_id WHERE em.office_id=%s{yf} ORDER BY em.mark_obtained DESC LIMIT 1""", (office_id,)+yp)
        r = cur.fetchone()
        if not r: return "No exam data found."
        return f"Highest marks{f' in {year}' if year else ''}: {r['mark_obtained']}/{r['total_mark']}\nTrainee: {r['name'] or 'N/A'}\nCourse: {r['course_name'] or 'N/A'}\nSubject: {r['subject_name'] or 'N/A'}"

    elif query_id == "EXAM_LOWEST_MARKS":
        year = p.get("year")
        yf, yp = _year_filter("em", "year", year)
        cur.execute(f"""SELECT u.name, em.mark_obtained, em.total_mark, c.course_name, es.subject_name
            FROM exam_marks em LEFT JOIN users u ON u.id=em.user_id LEFT JOIN courses c ON c.id=em.course_id
            LEFT JOIN exam_subject es ON es.id=em.sub_id WHERE em.office_id=%s{yf} ORDER BY em.mark_obtained ASC LIMIT 1""", (office_id,)+yp)
        r = cur.fetchone()
        if not r: return "No exam data found."
        return f"Lowest marks{f' in {year}' if year else ''}: {r['mark_obtained']}/{r['total_mark']}\nTrainee: {r['name'] or 'N/A'}\nCourse: {r['course_name'] or 'N/A'}\nSubject: {r['subject_name'] or 'N/A'}"

    elif query_id == "EXAM_AVERAGE_MARKS":
        year = p.get("year")
        yf, yp = _year_filter("em", "year", year)
        cur.execute(f"SELECT AVG(mark_obtained) as avg_m, COUNT(*) as cnt FROM exam_marks em WHERE em.office_id=%s{yf}", (office_id,)+yp)
        r = cur.fetchone()
        if not r or not r["cnt"]: return "No exam data found."
        return f"Average marks{f' in {year}' if year else ''}: {round(r['avg_m'] or 0, 1)} (from {r['cnt']} records)"

    elif query_id == "EXAM_SUBJECT_HIGHEST_FAILURE":
        year = p.get("year")
        yf, yp = _year_filter("em", "year", year)
        cur.execute(f"""SELECT es.subject_name, COUNT(*) as total, SUM(CASE WHEN em.result!=1 THEN 1 ELSE 0 END) as fails
            FROM exam_marks em LEFT JOIN exam_subject es ON es.id=em.sub_id
            WHERE em.office_id=%s AND es.subject_name IS NOT NULL{yf}
            GROUP BY em.sub_id, es.subject_name HAVING fails>0 ORDER BY (fails/total) DESC LIMIT 1""", (office_id,)+yp)
        r = cur.fetchone()
        if not r: return "No failures recorded."
        rate = round((r["fails"]/r["total"])*100, 2)
        return f"Subject with highest failure rate: {r['subject_name']} ({rate}% - {r['fails']}/{r['total']})"

    elif query_id == "EXAM_TOP_PERFORMERS":
        limit = int(p.get("limit", 10))
        year = p.get("year")
        yf, yp = _year_filter("em", "year", year)
        cur.execute(f"""SELECT u.name, AVG(em.mark_obtained/NULLIF(em.total_mark,0))*100 as avg_pct
            FROM exam_marks em LEFT JOIN users u ON u.id=em.user_id
            WHERE em.office_id=%s AND u.name IS NOT NULL AND em.total_mark>0{yf}
            GROUP BY u.id, u.name ORDER BY avg_pct DESC LIMIT %s""", (office_id,)+yp+(limit,))
        rows = cur.fetchall()
        if not rows: return "No exam performance data."
        lines = [f"{i+1}. {r['name']} - {round(r['avg_pct'],1)}%" for i,r in enumerate(rows)]
        return f"Top {limit} Performers{f' ({year})' if year else ''}:\n" + "\n".join(lines)

    elif query_id == "EXAM_AVG_MARKS_BY_DEPARTMENT":
        year = p.get("year")
        yf, yp = _year_filter("em", "year", year)
        cur.execute(f"""SELECT u.designation as dept, AVG(em.mark_obtained) as avg_m
            FROM exam_marks em LEFT JOIN users u ON u.id=em.user_id
            WHERE em.office_id=%s AND u.designation IS NOT NULL{yf}
            GROUP BY u.designation ORDER BY avg_m DESC""", (office_id,)+yp)
        rows = cur.fetchall()
        if not rows: return "No department-wise data found."
        lines = [f"- {r['dept']}: {round(r['avg_m'],1)} avg marks" for r in rows]
        return "Average marks by department:\n" + "\n".join(lines)

    elif query_id == "EXAM_REPEATED_FAILURES":
        minf = int(p.get("min_failures", 2))
        cur.execute("""SELECT u.name, COUNT(*) as fc FROM exam_marks em
            LEFT JOIN users u ON u.id=em.user_id WHERE em.office_id=%s AND em.result!=1 AND u.name IS NOT NULL
            GROUP BY u.id, u.name HAVING fc>=%s ORDER BY fc DESC""", (office_id, minf))
        rows = cur.fetchall()
        if not rows: return f"No trainees with {minf}+ failures."
        lines = [f"- {r['name']}: {r['fc']} failures" for r in rows]
        return "Trainees with repeated failures:\n" + "\n".join(lines)

    elif query_id == "EXAM_RE_EXAM_ELIGIBLE":
        cur.execute("""SELECT DISTINCT u.name FROM exam_marks em
            LEFT JOIN users u ON u.id=em.user_id WHERE em.office_id=%s AND em.result!=1 AND u.name IS NOT NULL""", (office_id,))
        rows = cur.fetchall()
        if not rows: return "No trainees eligible for re-exam."
        return "Re-exam eligible trainees:\n- " + "\n- ".join([r["name"] for r in rows])

    elif query_id == "EXAM_BELOW_THRESHOLD":
        thr = float(p.get("threshold_pct", 40))
        year = p.get("year")
        yf, yp = _year_filter("em", "year", year)
        cur.execute(f"""SELECT DISTINCT u.name, es.subject_name, em.mark_obtained, em.total_mark
            FROM exam_marks em LEFT JOIN users u ON u.id=em.user_id LEFT JOIN exam_subject es ON es.id=em.sub_id
            WHERE em.office_id=%s AND (em.mark_obtained*100.0/NULLIF(em.total_mark,0))<%s{yf} AND u.name IS NOT NULL
            ORDER BY (em.mark_obtained*100.0/NULLIF(em.total_mark,0)) ASC LIMIT 50""", (office_id, thr)+yp)
        rows = cur.fetchall()
        if not rows: return f"No trainees below {thr}%."
        lines = [f"- {r['name']} in {r['subject_name'] or 'N/A'} ({r['mark_obtained']}/{r['total_mark']})" for r in rows]
        return f"Trainees below {thr}%:\n" + "\n".join(lines)

    elif query_id == "EXAM_COMPARE_YEARS":
        y1 = p.get("year1")
        y2 = p.get("year2")
        if not y1 or not y2:
            cy = _cur_year(cur)
            y1, y2 = y1 or cy, y2 or cy-1
        cur.execute("""SELECT YEAR(created_at) as yr, COUNT(*) as total,
            SUM(CASE WHEN result=1 THEN 1 ELSE 0 END) as passed
            FROM exam_marks WHERE office_id=%s AND YEAR(created_at) IN (%s,%s)
            GROUP BY YEAR(created_at) ORDER BY yr DESC""", (office_id, y1, y2))
        rows = cur.fetchall()
        if len(rows)<2: return "Not enough data for year comparison."
        lines = [f"- {r['yr']}: {round((r['passed']/r['total'])*100,1)}% pass ({r['passed']}/{r['total']})" for r in rows if r['total']>0]
        return "Year Comparison:\n" + "\n".join(lines)

    elif query_id == "EXAM_TRAINEE_REPORT":
        name = p.get("search_name", "")
        if not name: return "Please specify a trainee name."
        cur.execute("""SELECT c.course_name, es.subject_name, em.mark_obtained, em.total_mark, em.result
            FROM exam_marks em LEFT JOIN users u ON u.id=em.user_id LEFT JOIN courses c ON c.id=em.course_id
            LEFT JOIN exam_subject es ON es.id=em.sub_id WHERE em.office_id=%s AND u.name LIKE %s""", (office_id, f"%{name}%"))
        rows = cur.fetchall()
        if not rows: return f"No report found for '{name}'."
        lines = [f"- {r['subject_name'] or 'N/A'} ({r['course_name'] or 'N/A'}): {r['mark_obtained']}/{r['total_mark']} - {'Passed' if r['result']==1 else 'Failed'}" for r in rows]
        return f"Report for {name}:\n" + "\n".join(lines)

    elif query_id == "EXAM_TRAINEE_MARKS_BY_ID":
        tid = p.get("trainee_id")
        if not tid: return "Please specify a trainee ID."
        cur.execute("""SELECT es.subject_name, em.mark_obtained, em.total_mark
            FROM exam_marks em LEFT JOIN exam_subject es ON es.id=em.sub_id
            WHERE em.office_id=%s AND em.user_id=%s""", (office_id, tid))
        rows = cur.fetchall()
        if not rows: return f"No marks for trainee ID {tid}."
        lines = [f"- {r['subject_name']}: {r['mark_obtained']}/{r['total_mark']}" for r in rows]
        return f"Marks for Trainee ID {tid}:\n" + "\n".join(lines)

    elif query_id == "EXAM_SCHEDULE":
        cur.execute("""SELECT sch.date, sch.start_time, sch.end_time, c.course_name, es.subject_name
            FROM exam_schedule sch LEFT JOIN courses c ON c.id=sch.course_id LEFT JOIN exam_subject es ON es.id=sch.sub_id
            WHERE sch.office_id=%s ORDER BY sch.date ASC, sch.start_time ASC""", (office_id,))
        rows = cur.fetchall()
        if not rows: return "No exam schedules found."
        lines = [f"- {r['date']} {r['start_time']}-{r['end_time']} | {r['course_name'] or 'N/A'} | {r['subject_name'] or 'N/A'}" for r in rows[:25]]
        return "Exam Schedule:\n" + "\n".join(lines)

    elif query_id == "EXAM_UPCOMING_SCHEDULE":
        cur.execute("""SELECT sch.date, sch.start_time, sch.end_time, c.course_name, es.subject_name
            FROM exam_schedule sch LEFT JOIN courses c ON c.id=sch.course_id LEFT JOIN exam_subject es ON es.id=sch.sub_id
            WHERE sch.office_id=%s AND sch.date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 7 DAY)
            ORDER BY sch.date ASC""", (office_id,))
        rows = cur.fetchall()
        if not rows: return "No upcoming exams in the next 7 days."
        lines = [f"- {r['date']} {r['start_time']}-{r['end_time']} | {r['course_name'] or 'N/A'} | {r['subject_name'] or 'N/A'}" for r in rows]
        return "Upcoming Exams:\n" + "\n".join(lines)

    elif query_id == "EXAM_SUBJECT_WISE_RESULTS":
        year = p.get("year")
        yf, yp = _year_filter("em", "year", year)
        cur.execute(f"""SELECT es.subject_name, COUNT(*) as total,
            SUM(CASE WHEN em.result=1 THEN 1 ELSE 0 END) as passed,
            SUM(CASE WHEN em.result!=1 THEN 1 ELSE 0 END) as failed,
            AVG(em.mark_obtained) as avg_m
            FROM exam_marks em LEFT JOIN exam_subject es ON es.id=em.sub_id
            WHERE em.office_id=%s AND es.subject_name IS NOT NULL{yf}
            GROUP BY es.subject_name ORDER BY avg_m DESC""", (office_id,)+yp)
        rows = cur.fetchall()
        if not rows: return "No subject-wise data."
        lines = [f"- {r['subject_name']}: Avg {round(r['avg_m'] or 0,1)}, Passed {r['passed']}, Failed {r['failed']}" for r in rows]
        return "Subject-wise Results:\n" + "\n".join(lines)

    return None
