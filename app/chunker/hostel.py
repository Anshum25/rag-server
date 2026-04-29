import logging
from app.services.db_service import get_connection

logger = logging.getLogger(__name__)

def get_hostel_chunks():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                hm.id AS entity_id,
                u.name AS trainee_name,
                hm.office_id,
                hb.building_name,
                hr.room_name,
                hm.beds,
                hm.in_date,
                hm.out_date,
                hm.days,
                hm.h_status,
                hm.remark
            FROM hostel_masters hm
            LEFT JOIN users u ON hm.user_id = u.id
            LEFT JOIN hostel_rooms hr ON hm.room_id = hr.id
            LEFT JOIN hostel_buildings hb ON hm.building_id = hb.id
            WHERE hm.office_id IS NOT NULL AND hm.user_id > 0
            LIMIT 200
        """)
        rows = cursor.fetchall()
        chunks = []
        for row in rows:
            name = row.get("trainee_name") or "Unknown trainee"
            building = row.get("building_name") or "Unknown building"
            room = row.get("room_name") or "N/A"
            text = f"Trainee: {name}\nBuilding: {building}\nRoom: {room}\nCheck In: {row.get('in_date')}\nCheck Out: {row.get('out_date')}\nDays: {row.get('days')}\nStatus: {row.get('h_status')}\n"
            chunks.append({
                "text": text,
                "office_id": row.get("office_id"),
                "module": "hostel",
                "allowed_roles": ["principal", "admin", "hostel_staff", "warden"],
                "entity_id": row.get("entity_id"),
                "entity_type": "hostel_allocation",
                "trainee_name": name.lower()
            })
        conn.close()
        return chunks
    except Exception as e:
        logger.warning(f"Hostel sync skipped: {e}")
        return []