from app.services.db_service import get_connection


def get_exam_chunks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            u.name AS trainee_name,
            c.course_name,
            es.subject_name,
            em.office_id,
            em.mark_obtained,
            em.total_mark,
            em.result
        FROM exam_marks em
        LEFT JOIN users u ON em.user_id = u.id
        LEFT JOIN courses c ON em.course_id = c.id
        LEFT JOIN exam_subject es ON em.sub_id = es.id
        LIMIT 200
    """)

    rows = cursor.fetchall()

    chunks = []

    for row in rows:
        name = row.get("trainee_name") or "Unknown trainee"
        course = row.get("course_name") or "training"
        subject = row.get("subject_name") or "subject"
        marks = row.get("mark_obtained") or 0
        total = row.get("total_mark") or 0
        result = "passed" if row.get("result") == 1 else "failed"
        
        if total == 0:
            text = f"""
Trainee: {name}
Course: {course}
Subject: {subject}
Marks: {marks}
Result: {result}
"""
        else:
            text = f"""
Trainee: {name}
Course: {course}
Subject: {subject}
Marks: {marks} out of {total}
Result: {result}
"""

        chunks.append({
            "text": text,
            "trainee_name": name.lower(),
            "office_id": row.get("office_id") or 1,
            "module": "exam",
            "allowed_roles": ["principal", "admin", "exam_staff"]
        })

    conn.close()
    return chunks