import argparse
import json
from invoice_normalizer.parser import normalize_invoice

def main():
    parser = argparse.ArgumentParser(description="Normalize messy invoice data")
    parser.add_argument("input", help="Path to the input JSON file")
    parser.add_argument("output", help="Path to save the normalized output JSON file")
    args = parser.parse_args()

    with open(args.input, "r") as f:
        data = json.load(f)

    if isinstance(data, list):
        normalized_data = [normalize_invoice(d) for d in data]
    else:
        normalized_data = normalize_invoice(data)

    with open(args.output, "w") as f:
        json.dump(normalized_data, f, indent=2)

    print(f"Normalization complete. Output saved to {args.output}")


