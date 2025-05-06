# Invoice Data Normalizer

This script cleans and standardizes messy invoice JSON data.

## What it does

-Standardizes inconsistent invoice keys.
- Parses and unifies date formats into `YYYY-MM-DD`.
- Cleans currency strings to numeric format.
- Replaces **empty keys or values** with the default value `"N/A"`.


## How to use

1. Add your messy JSON invoice to `input.json`
2. Run the script:

```bash
python normalize.py
