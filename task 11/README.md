# Invoice Normalizer

`invoice_normalizer` is a Python package designed to standardize and normalize invoice data. This package helps in handling inconsistent or messy invoice fields, such as varying date formats, amounts, and keys. It parses and cleans data, making it easier to process invoices for further use in accounting systems, databases, or analytics pipelines.

---

## 🚀 Features

- ✅ **Key Normalization**: Maps multiple possible key names (e.g., `inv_no`, `invoiceID`, `invoice_number`) to standardized keys.
- 📆 **Date Parsing**: Converts inconsistent date formats into a uniform `YYYY-MM-DD` format.
- 💰 **Amount Cleaning**: Handles different number/currency formats and converts to float.
- 📂 **Supports Multiple Invoices**: Works with JSON data containing multiple invoices.
- 🧾 **Handles Missing Values**: Replaces empty keys or values with `"N/A"`.

---

## 📦 Installation

To install the package locally (for development or testing):

```bash
pip install .
