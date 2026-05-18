"""Library module query templates."""

TEMPLATES = [
    {
        "id": "LIBRARY_TOTAL_BOOKS",
        "module": "library",
        "description": "Total books",
        "example_questions": ["Total books?", "How many books in library?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff", "librarian"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "LIBRARY_BOOK_LIST",
        "module": "library",
        "description": "Book list",
        "example_questions": ["List all books?", "Show books?"],
        "required_params": [],
        "optional_params": ["office_id", "book_type", "limit"],
        "allowed_roles": ["principal", "admin", "staff", "librarian"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "LIBRARY_BOOKS_BY_TYPE",
        "module": "library",
        "description": "Books by type",
        "example_questions": ["Books by type?", "Show books by category?"],
        "required_params": [],
        "optional_params": ["book_type_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff", "librarian"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "LIBRARY_BOOK_DETAILS",
        "module": "library",
        "description": "Book details by title",
        "example_questions": ["Book details?", "Show book information?"],
        "required_params": [],
        "optional_params": ["book_title", "book_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff", "librarian"],
        "result_type": "detail",
        "security_level": "low"
    },
    {
        "id": "LIBRARY_ISSUED_BOOKS",
        "module": "library",
        "description": "Issued books",
        "example_questions": ["Which books are issued?", "Show issued books?"],
        "required_params": [],
        "optional_params": ["office_id", "from_date", "to_date"],
        "allowed_roles": ["principal", "admin", "staff", "librarian"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "LIBRARY_RETURNED_BOOKS",
        "module": "library",
        "description": "Returned books",
        "example_questions": ["Returned books?", "Show returned books?"],
        "required_params": [],
        "optional_params": ["office_id", "from_date", "to_date"],
        "allowed_roles": ["principal", "admin", "staff", "librarian"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "LIBRARY_OVERDUE_BOOKS",
        "module": "library",
        "description": "Overdue books",
        "example_questions": ["Overdue books?", "Which books are overdue?"],
        "required_params": [],
        "optional_params": ["office_id", "due_date"],
        "allowed_roles": ["principal", "admin", "staff", "librarian"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "LIBRARY_BOOKS_ISSUED_TO_TRAINEE",
        "module": "library",
        "description": "Books issued to trainee",
        "example_questions": ["Books issued to trainee?", "What books does trainee have?"],
        "required_params": [],
        "optional_params": ["user_id", "user_name", "office_id"],
        "allowed_roles": ["principal", "admin", "staff", "librarian", "trainee"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "LIBRARY_ISSUE_COUNT_BY_COURSE",
        "module": "library",
        "description": "Issue count by course",
        "example_questions": ["Issues by course?", "Book issues course-wise?"],
        "required_params": [],
        "optional_params": ["course_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff", "librarian"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "LIBRARY_BOOK_STOCK",
        "module": "library",
        "description": "Book stock quantity",
        "example_questions": ["Book stock?", "How many copies available?"],
        "required_params": [],
        "optional_params": ["book_id", "office_id"],
        "allowed_roles": ["principal", "admin", "staff", "librarian"],
        "result_type": "count",
        "security_level": "low"
    },
    {
        "id": "LIBRARY_FINE_SUMMARY",
        "module": "library",
        "description": "Book fine summary",
        "example_questions": ["Library fines?", "Total fines collected?"],
        "required_params": [],
        "optional_params": ["office_id", "from_date", "to_date"],
        "allowed_roles": ["principal", "admin", "staff", "librarian"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "LIBRARY_BOOKS_BY_AUTHOR",
        "module": "library",
        "description": "Books by author",
        "example_questions": ["Books by author?", "Author-wise books?"],
        "required_params": [],
        "optional_params": ["author_name", "office_id"],
        "allowed_roles": ["principal", "admin", "staff", "librarian"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "LIBRARY_BOOKS_PURCHASED",
        "module": "library",
        "description": "Books purchased by date",
        "example_questions": ["Books purchased?", "New book arrivals?"],
        "required_params": [],
        "optional_params": ["from_date", "to_date", "office_id"],
        "allowed_roles": ["principal", "admin", "staff", "librarian"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "LIBRARY_AVAILABLE_BOOKS",
        "module": "library",
        "description": "Available books",
        "example_questions": ["Available books?", "Books in stock?"],
        "required_params": [],
        "optional_params": ["office_id", "book_type"],
        "allowed_roles": ["principal", "admin", "staff", "librarian"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "LIBRARY_MOST_ISSUED",
        "module": "library",
        "description": "Most issued books",
        "example_questions": ["Most issued books?", "Popular books?"],
        "required_params": [],
        "optional_params": ["office_id", "limit"],
        "allowed_roles": ["principal", "admin", "staff", "librarian"],
        "result_type": "ranking",
        "security_level": "low"
    },
    {
        "id": "LIBRARY_BOOK_TYPE_SUMMARY",
        "module": "library",
        "description": "Book type summary",
        "example_questions": ["Book type summary?", "Books by category count?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin", "staff", "librarian"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "LIBRARY_OFFICE_SUMMARY",
        "module": "library",
        "description": "Library office summary",
        "example_questions": ["Library summary?", "Office library stats?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "summary",
        "security_level": "low"
    },
    {
        "id": "LIBRARY_PENDING_RETURNS",
        "module": "library",
        "description": "Pending returns",
        "example_questions": ["Pending returns?", "Books not returned?"],
        "required_params": [],
        "optional_params": ["office_id", "due_date"],
        "allowed_roles": ["principal", "admin", "staff", "librarian"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "LIBRARY_ISSUE_HISTORY",
        "module": "library",
        "description": "Book issue history",
        "example_questions": ["Issue history?", "Book transaction history?"],
        "required_params": [],
        "optional_params": ["book_id", "user_id", "office_id", "limit"],
        "allowed_roles": ["principal", "admin", "staff", "librarian"],
        "result_type": "list",
        "security_level": "low"
    },
    {
        "id": "LIBRARY_MODULE_SUMMARY",
        "module": "library",
        "description": "Library module summary",
        "example_questions": ["Library module summary?", "Overall library stats?"],
        "required_params": [],
        "optional_params": ["office_id"],
        "allowed_roles": ["principal", "admin"],
        "result_type": "summary",
        "security_level": "low"
    }
]


def execute(query_id, params, cur, office_id):
    """Execute library queries."""
    p = params or {}
    
    if query_id == "LIBRARY_TOTAL_BOOKS":
        cur.execute("SELECT COUNT(*) AS total FROM books WHERE office_id = %s", (office_id,))
        r = cur.fetchone()
        return f"Total books: {r['total'] if r else 0}"
    
    return None
