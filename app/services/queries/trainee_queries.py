"""Trainee, combined, and other module query handlers."""

TEMPLATES = [
    {"id": "TRAINEE_COUNT", "description": "Total trainee count. Params: gender (optional, male/female)"},
    {"id": "TRAINEE_LIST", "description": "List trainee names. Params: gender (optional), limit (default 50)"},
    {"id": "TRAINEE_JOINED_YEAR", "description": "Trainees who joined in a specific year. Params: year (required)"},
    {"id": "TRAINEE_COUNTS_BY_COURSE", "description": "Trainee count per course"},
    {"id": "COMBINED_HOSTEL_VS_NON_PERFORMANCE", "description": "Compare hostel vs non-hostel trainee performance. Params: year (optional)"},
    {"id": "COMBINED_HOSTEL_VS_NON_FAILURE_RATE", "description": "Failure rate hostel vs non-hostel. Params: year (optional)"},
    {"id": "COMBINED_TOP_PERFORMERS_IN_HOSTEL", "description": "Top performers staying in hostel. Params: limit (default 10), year (optional)"},
    {"id": "TRAINING_CALENDAR_NOMINEES", "description": "Training calendar nominee count"},
    {"id": "ACTIVE_TRAINEES_COUNT", "description": "Count of approved trainees currently undergoing active courses/training"},
]


def _year_filter(alias="em", param_name="year", year_val=None):
    if year_val:
        return f" AND YEAR({alias}.created_at) = %s", (int(year_val),)
    return "", ()


def _cur_year(cur):
    cur.execute("SELECT YEAR(CURDATE()) AS y")
    return int((cur.fetchone() or {}).get("y") or 2025)


def execute(query_id, params, cur, office_id):
    p = params or {}

    if query_id == "TRAINEE_COUNT":
        gender = p.get("gender")
        gf = ""
        if gender:
            g = gender.lower()
            if g in ("male", "m"): gf = " AND u.gender IN ('m','male','1')"
            elif g in ("female", "f"): gf = " AND u.gender IN ('f','female','0','2')"
        cur.execute(f"SELECT COUNT(*) as cnt FROM users u WHERE u.office_id=%s AND role_id=1 AND u.name IS NOT NULL{gf}", (office_id,))
        r = cur.fetchone()
        label = f"{gender} " if gender else ""
        return f"Total {label}trainees: {r['cnt'] if r else 0}"

    elif query_id == "TRAINEE_LIST":
        gender = p.get("gender")
        limit = int(p.get("limit", 50))
        gf = ""
        if gender:
            g = gender.lower()
            if g in ("male", "m"): gf = " AND u.gender IN ('m','male','1')"
            elif g in ("female", "f"): gf = " AND u.gender IN ('f','female','0','2')"
        cur.execute(f"SELECT u.name FROM users u WHERE u.office_id=%s AND u.name IS NOT NULL{gf} ORDER BY u.name ASC LIMIT %s", (office_id, limit))
        rows = cur.fetchall()
        if not rows: return "No trainees found."
        names = [r["name"] for r in rows]
        return f"Trainees ({len(names)}):\n- " + "\n- ".join(names)

    elif query_id == "TRAINEE_JOINED_YEAR":
        year = p.get("year")
        if not year: year = _cur_year(cur)
        cur.execute("""SELECT DISTINCT u.name FROM tra_masters tm JOIN users u ON u.id=tm.user_id
            WHERE tm.office_id=%s AND tm.j_date IS NOT NULL AND tm.j_date>='1000-01-01'
            AND YEAR(tm.j_date)=%s AND u.name IS NOT NULL ORDER BY u.name ASC""", (office_id, year))
        rows = cur.fetchall()
        if not rows: return f"No trainees joined in {year}."
        names = [r["name"] for r in rows]
        return f"Trainees joined in {year} ({len(names)}):\n- " + "\n- ".join(names[:50])

    elif query_id == "TRAINEE_COUNTS_BY_COURSE":
        cur.execute("""SELECT c.course_name, COUNT(DISTINCT tm.user_id) AS cnt
            FROM tra_masters tm LEFT JOIN courses c ON c.id=tm.course_id
            WHERE tm.office_id=%s GROUP BY c.course_name ORDER BY cnt DESC""", (office_id,))
        rows = cur.fetchall()
        if not rows: return "No course data found."
        lines = [f"- {r['course_name'] or 'N/A'}: {r['cnt']}" for r in rows]
        return "Trainee counts by course:\n" + "\n".join(lines)

    elif query_id == "COMBINED_HOSTEL_VS_NON_PERFORMANCE":
        year = p.get("year")
        yf, yp = _year_filter("em", "year", year)
        cur.execute(f"""SELECT CASE WHEN hm.id IS NOT NULL THEN 'Hostel' ELSE 'Non-Hostel' END as cat,
            AVG(em.mark_obtained/NULLIF(em.total_mark,0))*100 as avg_pct
            FROM exam_marks em LEFT JOIN hostel_masters hm ON hm.user_id=em.user_id AND hm.h_status=1
            WHERE em.office_id=%s{yf} GROUP BY cat""", (office_id,)+yp)
        rows = cur.fetchall()
        if not rows: return "Not enough data for comparison."
        lines = [f"- {r['cat']}: {round(r['avg_pct'] or 0,1)}% average" for r in rows]
        return "Hostel vs Non-Hostel Performance:\n" + "\n".join(lines)

    elif query_id == "COMBINED_HOSTEL_VS_NON_FAILURE_RATE":
        year = p.get("year")
        yf, yp = _year_filter("em", "year", year)
        cur.execute(f"""SELECT CASE WHEN hm.id IS NOT NULL THEN 'Hostel' ELSE 'Non-Hostel' END as cat,
            COUNT(*) as total, SUM(CASE WHEN em.result!=1 THEN 1 ELSE 0 END) as fails
            FROM exam_marks em LEFT JOIN hostel_masters hm ON hm.user_id=em.user_id AND hm.h_status=1
            WHERE em.office_id=%s{yf} GROUP BY cat""", (office_id,)+yp)
        rows = cur.fetchall()
        if not rows: return "Not enough data."
        lines = [f"- {r['cat']}: {round((r['fails']/r['total'])*100,1)}% failure rate" for r in rows if r['total']>0]
        return "Failure Rate Comparison:\n" + "\n".join(lines)

    elif query_id == "COMBINED_TOP_PERFORMERS_IN_HOSTEL":
        limit = int(p.get("limit", 10))
        year = p.get("year")
        yf, yp = _year_filter("em", "year", year)
        cur.execute(f"""SELECT u.name, AVG(em.mark_obtained/NULLIF(em.total_mark,0))*100 as avg_pct
            FROM exam_marks em JOIN hostel_masters hm ON hm.user_id=em.user_id AND hm.h_status=1
            JOIN users u ON u.id=em.user_id WHERE em.office_id=%s{yf}
            GROUP BY u.id, u.name ORDER BY avg_pct DESC LIMIT %s""", (office_id,)+yp+(limit,))
        rows = cur.fetchall()
        if not rows: return "No hostel performer data."
        lines = [f"{i+1}. {r['name']} - {round(r['avg_pct'] or 0,1)}%" for i,r in enumerate(rows)]
        return f"Top {limit} Hostel Performers:\n" + "\n".join(lines)

    elif query_id == "TRAINING_CALENDAR_NOMINEES":
        cur.execute("SELECT COUNT(*) AS cnt FROM training_calendars_nominee WHERE office_id=%s", (office_id,))
        r = cur.fetchone()
        return f"Training calendar nominees: {r['cnt'] if r else 0}"

    elif query_id == "ACTIVE_TRAINEES_COUNT":
        cur.execute("""SELECT COUNT(tm.id) as cnt
            FROM tra_masters tm 
            LEFT JOIN training_calendars tc on tc.id = tm.course_id AND tc.status=1 
            WHERE tc.from_date <= CURDATE() AND tc.to_date >= CURDATE() 
            AND tm.office_id = %s AND tm.status = 1 AND tm.is_approved = 1""", (office_id,))
        r = cur.fetchone()
        return f"Currently active trainees undergoing training: {r['cnt'] if r else 0}"

    return None
