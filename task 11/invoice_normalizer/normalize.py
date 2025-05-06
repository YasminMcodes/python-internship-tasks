import re
from dateutil import parser

# Mapping known inconsistent keys to a standardized version
KEY_MAPPING = {
    "invoice_number": [
        "inv_no", "invoice_no", "InvoiceNumber", "invoiceNumber",
        "invnum", "inv#", "invoice#", "invoiceID", "invoice_id", "inv_id"
    ],
    "invoice_date": [
        "date", "inv_date", "invoiceDate", "Invoice_Date", "bill_date",
        "invoice_date", "issued", "issue_date", "date_of_invoice", "DateIssued"
    ],
    "due_date": [
        "due", "due_date", "dueDate", "payment_due", "dueDateString",
        "final_date", "due_dt", "deadline", "payment_due_date"
    ],
    "total_amount": [
        "total", "amount", "invoice_amount", "totalAmount", "InvoiceTotal",
        "grand_total", "net_amount", "balance_due", "invoiceValue",
        "inv_amount", "invoiceTotal", "amt", "TotalAmount"
    ],
    "vendor": [
        "vendor", "supplier", "vendor_name", "company", "from",
        "biller", "issuer", "vendorName", "seller", "provider"
    ]
}

# Reverse lookup for easy normalization
FLATTENED_KEY_MAPPING = {
    variant.lower(): canonical for canonical, variants in KEY_MAPPING.items() for variant in variants
}


def normalize_keys(record):
    normalized = {}
    for key, value in record.items():
        std_key = FLATTENED_KEY_MAPPING.get(key.strip().lower(), key.strip().lower())
        normalized[std_key] = value if value else "N/A"
    return normalized


def parse_date(date_str):
    try:
        return parser.parse(date_str).strftime("%Y-%m-%d")
    except Exception:
        return date_str


def clean_amount(amount):
    if isinstance(amount, str):
        amount = re.sub(r'[^\d.]', '', amount)
    try:
        return float(amount)
    except ValueError:
        return amount


def normalize_invoice(record):
    record = normalize_keys(record)
    if "invoice_date" in record:
        record["invoice_date"] = parse_date(record["invoice_date"])
    if "due_date" in record:
        record["due_date"] = parse_date(record["due_date"])
    if "total_amount" in record:
        record["total_amount"] = clean_amount(record["total_amount"])
    return record


def normalize_invoices(data):
    if isinstance(data, list):
        return [normalize_invoice(item) for item in data]
    return [normalize_invoice(data)]

