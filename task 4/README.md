# Invoice Data Normalizer

This script cleans and standardizes messy invoice JSON data.

## What it does
- Renames inconsistent field keys to standard ones
- Parses various date formats into `YYYY-MM-DD`
- Cleans currency fields and converts to float

## How to use

1. Add your messy JSON invoice to `input.json`
2. Run the script:

```bash
python normalize.py
