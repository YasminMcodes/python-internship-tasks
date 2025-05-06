import json
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

# 🔁 Invert the KEY_MAPPING to map variant -> standard key
INVERTED_MAPPING = {}
for standard_key, variants in KEY_MAPPING.items():
    for variant in variants:
        INVERTED_MAPPING[variant.lower()] = standard_key


def normalize_keys(data, default_value="N/A"):
    """Standardize invoice keys using a mapping dictionary, replace empty values with a default."""
    normalized = {}
    for k, v in data.items():
        clean_key = k.strip()

        # If key or value is empty, replace with the default value
        if not clean_key or not v:
            print(f"Warning: Empty key or value detected. Replacing with default: {clean_key} -> {default_value}")
            v = default_value

        # Find standardized key name
        for standard, variants in KEY_MAPPING.items():
            if clean_key.lower() in [x.lower() for x in variants]:
                clean_key = standard
                break

        # Store normalized key-value pair
        normalized[clean_key.lower()] = v

    return normalized


def parse_date(date_str):
    """Try to parse any string date format into YYYY-MM-DD."""
    try:
        return parser.parse(date_str).strftime("%Y-%m-%d")
    except Exception:
        return date_str  # leave as-is if unparseable

def clean_amount(amount):
    """Convert currency strings like '$1,000.50' to float 1000.5."""
    if isinstance(amount, str):
        amount = re.sub(r'[^\d.]', '', amount)
    try:
        return float(amount)
    except ValueError:
        return amount

def normalize_invoice(data):
    """Main function to normalize invoice fields."""
    data = normalize_keys(data)

    if 'invoice_date' in data:
        data['invoice_date'] = parse_date(data['invoice_date'])

    if 'due_date' in data:
        data['due_date'] = parse_date(data['due_date'])

    if 'total_amount' in data:
        data['total_amount'] = clean_amount(data['total_amount'])

    return data

if __name__ == "__main__":
    with open("input.json") as f:
        raw = json.load(f)

    if isinstance(raw, list):
        normalized = [normalize_invoice(invoice) for invoice in raw]
    else:
        normalized = normalize_invoice(raw)

    with open("output.json", "w") as f:
        json.dump(normalized, f, indent=2)

    print("Normalization complete! See output.json.")

