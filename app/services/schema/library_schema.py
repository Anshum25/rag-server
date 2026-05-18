"""Library module schema for LLM SQL generation."""

LIBRARY_SCHEMA = """
TRMS Library module schema.

Important rules:
- status = 1 means active record where applicable.
- office_id is used for office-wise filtering where available.
- Always enforce office_id from backend/login context.
- Do not select users.password.
- Use case-insensitive search for names: LOWER(users.name) LIKE LOWER('%name%')

Allowed tables and columns:

Table: books
Columns:
- id
- office_id

Table: book_issue
Columns:
- id
- office_id

Table: book_type
Columns:
- id
- office_id

Table: users
Columns:
- id
- role_id
- office_id

Table: courses
Columns:
- id
- cf_id

Table: training_calendars
Columns:
- id
- cf_id
- ct_id

Business meaning:
- books stores book master records.
- book_issue stores book issue/return transactions.
- book_type stores book categorization.
- users for library members.
- courses, training_calendars for course context.

Recommended relationships:
- book_issue links to users and books
- books may link to book_type

Common question mapping:
- Total books: Count books
- Issued books: Count book_issue where not returned
- Overdue books: book_issue with due date passed
- Books by type: Group by book_type
- Books issued to trainee: Filter by user_id
"""
