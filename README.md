# Python Internship Tasks

Welcome to the **Python Internship Tasks** repository!  
This repository contains a collection of Python-based tasks completed as part of a developer internship. Each task demonstrates a specific programming skill such as data normalization, Python packaging, CLI scripting, and unit testing.

---

## 📁 Repository Structure

Each task is organized into its own folder, and includes source code, documentation, and (when applicable) tests.

### ✅ Tasks Overview

#### 🔹 `task 4/` — **Data Normalization Utility**
- A Python script that parses and standardizes messy invoice data from JSON files.
- Handles inconsistent key names, missing values, and varying date formats.
- Includes:
  - `normalize.py`: Main script for data normalization.
  - `input.json`: Sample messy data.
  - `README.md`: Explanation of features and usage.

#### 🔹 `task 11/` — **Python Package: invoice_normalizer**
- Converts the normalization logic from Task 4 into a pip-installable Python package.
- Features:
  - `invoice_normalizer/`: Package module with `normalize.py` and CLI support.
  - `test/`: Unit tests using `pytest`.
  - `setup.py`, `requirements.txt`: For packaging and dependencies.
  - `README.md`: Usage and installation instructions.

---

## 🛠 Technologies Used

- Python 3.11+
- `setuptools` for packaging
- `pytest` for unit testing
- `python-dateutil` for robust date parsing

---

## 📦 How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/python-internship-tasks.git
   cd python-internship-tasks
