"""Smart query service - dispatches to module-specific query handlers."""
import traceback
from typing import Any, Dict
from app.services.db_service import get_connection
from app.services.queries import exam_queries, hostel_queries, trainee_queries

# Aggregate all templates from module files
QUERY_TEMPLATES = (
    exam_queries.TEMPLATES +
    hostel_queries.TEMPLATES +
    trainee_queries.TEMPLATES
)

# Ordered list of module handlers to try
_MODULE_HANDLERS = [exam_queries, hostel_queries, trainee_queries]


def execute_smart_query(query_id: str, params: Dict[str, Any], office_id: int) -> str:
    conn = get_connection()
    try:
        cur = conn.cursor()
        # Try each module handler in order
        for module in _MODULE_HANDLERS:
            result = module.execute(query_id, params or {}, cur, office_id)
            if result is not None:
                return result
        return None
    except Exception as e:
        print(f"Error executing smart query {query_id}: {traceback.format_exc()}")
        return f"Error processing request: {str(e)}"
    finally:
        conn.close()
