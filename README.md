# Python Loops and Functions Practice

This project contains ten independently runnable solutions: five loop
exercises and five function exercises. Each question has its own Python file.

## Folder structure

```text
loops_practice/
    q1_delivered_revenue.py
    q2_numbered_items.py
    q3_biggest_order.py
    q4_totals_per_customer.py
    q5_reorder_report.py
functions_practice/
    q1_format_rupees.py
    q2_add_tax.py
    q3_shipping_charge.py
    q4_total_by_status.py
    q5_refactor_reorder_report.py
```

## How to run

Run a script from the project root using Python:

```text
python loops_practice/q1_delivered_revenue.py
python loops_practice/q2_numbered_items.py
python loops_practice/q3_biggest_order.py
python loops_practice/q4_totals_per_customer.py
python loops_practice/q5_reorder_report.py
python functions_practice/q1_format_rupees.py
python functions_practice/q2_add_tax.py
python functions_practice/q3_shipping_charge.py
python functions_practice/q4_total_by_status.py
python functions_practice/q5_refactor_reorder_report.py
```

On Windows, replace `python` with `py` if that is how Python is configured
on your computer. Each command runs that question independently.

## Questions

### Loops practice

- **Q1 — Delivered Revenue:** Sum the totals for delivered orders.
- **Q2 — Numbered Items:** Number the prices, calculate their total, and
  count how many exceed Rs 1,000.
- **Q3 — The Biggest Order:** Find and print the order with the largest
  total, retaining the first order if totals are tied.
- **Q4 — Totals Per Customer:** Group orders by customer and sum each
  customer's totals.
- **Q5 — Reorder Report:** Identify low-stock products, calculate reorder
  quantities, and print the combined cost.

### Functions practice

- **Q1 — Formatting Rupees:** Format amounts with a rupee label and
  thousands separators.
- **Q2 — Return or Print?:** Calculate tax with a returned value and
  compare it to a print-only function.
- **Q3 — Shipping as a Function:** Calculate shipping based on city,
  weight, and the free-shipping order threshold.
- **Q4 — Totals by Status:** Return the sum of orders matching a status.
- **Q5 — Refactor the Reorder Report:** Build the inventory report using
  small functions for reorder checks, quantities, and costs.

## Week 01 Café Expense Report

The script loads café expenses from `week-01/expenses.json`, calculates the
overall and per-category totals, finds the largest expense, and lists expenses
above the approval limit. It also writes the totals to
`week-01/summary.json` for use by another program. Categories are calculated
from the data, so adding a category does not require changing the script.

### Project structure

```text
week-01/
    expenses.json
    expenses.py
    summary.json  # created when the script runs successfully
```

### How to run

From the project root, run:

```text
python3 week-01/expenses.py
```

On Windows, you can use `py week-01/expenses.py` or replace `python3` with
the Python command configured on your computer. The approval limit is set by
`APPROVAL_LIMIT` near the top of `week-01/expenses.py`.

### Functions

- `load_expenses(path)` reads and checks the JSON file so missing or invalid
  input is reported clearly instead of causing a traceback.
- `format_rupees(amount)` keeps displayed rupee amounts consistently
  formatted with commas.
- `category_totals(expenses)` uses a loop to build totals for all categories
  present in the data.
- The other helper functions calculate the overall total, find the largest
  expense, select expenses needing approval, build the report, and save the
  accountant's JSON summary. Each has one focused job and returns its result.
