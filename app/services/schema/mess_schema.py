"""Mess module schema for LLM SQL generation."""

MESS_SCHEMA = """
TRMS Mess module schema.

Important rules:
- status = 1 means active record where applicable.
- office_id is used for office-wise filtering where available.
- Always enforce office_id from backend/login context.
- Do not select users.password.
- Use case-insensitive search for names: LOWER(users.name) LIKE LOWER('%name%')

Allowed tables and columns:

Table: bills
Columns:
- id
- bill_no

Table: bill_details
Columns:
- id
- bill_id
- item_id
- qty

Table: bill_receipts
Columns:
- id
- bill_id
- user_id
- course_id
- user_name

Table: bill_receipts_refund
Columns:
- id
- bill_id
- user_id
- role_id
- pay_by
- amount
- receipt_no
- receipt_date
- due
- txn_no
- status
- remarks
- online_log
- created_at
- updated_at

Table: mess_bill_format
Columns:
- id
- office_id

Table: mess_material
Columns:
- id
- item_name
- units
- status
- created_at
- updated_at

Table: items
Columns:
- id
- office_id

Table: item_prices
Columns:
- id
- office_id

Table: partys
Columns:
- id
- office_id
- p_name
- p_email
- p_mobile
- status
- created_at
- updated_at

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

Table: hostel_masters
Columns:
- id
- user_id
- role_id
- office_id
- proom_type
- person
- amount
- ct_id
- course_id
- train_no
- ph
- receipt_no

Business meaning:
- bills stores mess bill headers.
- bill_details stores bill line items.
- bill_receipts stores payment receipts.
- bill_receipts_refund stores refund records.
- mess_bill_format stores bill format settings.
- mess_material stores material/item master.
- items, item_prices for item pricing.
- partys stores vendor/party information.
- hostel_masters links to hostel occupancy.

Recommended relationships:
- bill_details.bill_id = bills.id
- bill_receipts.bill_id = bills.id
- bill_receipts_refund.bill_id = bills.id
- mess_material for item details

Common question mapping:
- Total bills: Count bills
- Bill amount: Sum bill_details
- Pending dues: Sum bill_receipts_refund.due
- Receipts: Query bill_receipts
- Refunds: Query bill_receipts_refund
- Mess materials: Query mess_material
"""
