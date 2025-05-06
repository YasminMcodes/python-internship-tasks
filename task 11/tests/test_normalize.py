
import pytest
from invoice_normalizer import normalize


# Test Case 1: Test the normalize_keys function
def test_normalize_keys():
    """Test the normalization of keys."""
    raw_data = {
        "inv_no": "INV-2024-001",
        "inv_date": "2024-04-01",
        "TotalAmount": "$1,250.99"
    }
    expected_output = {
        "invoice_number": "INV-2024-001",
        "invoice_date": "2024-04-01",
        "total_amount": "$1,250.99"
    }

    # Call the normalize_keys function
    normalized_data = normalize.normalize_keys(raw_data)

    # Assert that the normalized data matches the expected output
    assert normalized_data == expected_output


# Test Case 2: Test the clean_amount function
def test_clean_amount():
    """Test cleaning a string with currency symbols and commas."""
    amount_str = "$1,250.99"

    # Call the clean_amount function
    cleaned_amount = normalize.clean_amount(amount_str)

    # Assert that the cleaned amount is a float without currency symbols
    assert cleaned_amount == 1250.99

