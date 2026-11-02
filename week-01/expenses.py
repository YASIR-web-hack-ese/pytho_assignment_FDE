# Week 01: Cafe Expense Report
# Load expenses from JSON, calculate totals, show approval items, and save
# a small JSON summary for the accountant.

import json


EXPENSES_FILE = "week-01/expenses.json"
SUMMARY_FILE = "week-01/summary.json"
APPROVAL_LIMIT = 25000


def load_expenses(path):
    # Read the expense list from the JSON file. Return None if the file
    # cannot be read or its contents are not the expected kind of data.
    try:
        with open(path, "r", encoding="utf-8") as expenses_file:
            expenses = json.load(expenses_file)
    except FileNotFoundError:
        print(f"Could not read {path}: file not found.")
        return None
    except json.JSONDecodeError as error:
        print(
            f"Could not read {path}: invalid JSON "
            f"on line {error.lineno}, column {error.colno}."
        )
        return None
    except UnicodeDecodeError:
        print(f"Could not read {path}: file is not valid UTF-8 text.")
        return None
    except OSError as error:
        print(f"Could not read {path}: {error}.")
        return None

    # Check the JSON structure before using its values in the report.
    if not isinstance(expenses, list):
        print(f"Could not read {path}: expected a list of expenses.")
        return None

    expense_number = 1
    for expense in expenses:
        if not isinstance(expense, dict):
            print(
                f"Could not read {path}: expense {expense_number} "
                "is not an object."
            )
            return None

        if (
            "item" not in expense
            or "category" not in expense
            or "amount" not in expense
        ):
            print(
                f"Could not read {path}: expense {expense_number} "
                "needs item, category, and amount."
            )
            return None

        if (
            not isinstance(expense["item"], str)
            or not isinstance(expense["category"], str)
            or not isinstance(expense["amount"], (int, float))
        ):
            print(
                f"Could not read {path}: expense {expense_number} "
                "has an invalid item, category, or amount."
            )
            return None

        expense_number += 1

    return expenses


def format_rupees(amount):
    # Format one amount consistently wherever the report displays money.
    return f"Rs {amount:,}"


def category_totals(expenses):
    # Build totals from the expense data so new categories work automatically.
    totals = {}

    for expense in expenses:
        category = expense["category"]
        if category in totals:
            totals[category] += expense["amount"]
        else:
            totals[category] = expense["amount"]

    return totals


def total_spent(expenses):
    # Add every expense amount to get the overall total.
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def largest_expense(expenses):
    # Keep the first expense with the largest amount found so far.
    if len(expenses) == 0:
        return None

    largest = expenses[0]

    for expense in expenses:
        if expense["amount"] > largest["amount"]:
            largest = expense

    return largest


def expenses_over_limit(expenses, approval_limit):
    # Collect expenses that are strictly greater than the approval limit.
    approval_expenses = []

    for expense in expenses:
        if expense["amount"] > approval_limit:
            approval_expenses.append(expense)

    return approval_expenses


def build_report(expenses, approval_limit):
    # Return the complete text report so main can display it after saving.
    by_category = category_totals(expenses)
    total = total_spent(expenses)
    largest = largest_expense(expenses)
    approval_expenses = expenses_over_limit(expenses, approval_limit)

    report_lines = [
        "Cafe expense report",
        f"Expenses recorded: {len(expenses)}",
        f"Total spent: {format_rupees(total)}",
        "",
        "By category:",
    ]

    for category, amount in by_category.items():
        report_lines.append(f"  {category:<10} Rs {amount:>7,}")

    report_lines.append("")

    if largest is None:
        report_lines.append("Largest expense: None")
    else:
        report_lines.append(
            f"Largest expense: {largest['item']} "
            f"({format_rupees(largest['amount'])})"
        )

    report_lines.append("")
    report_lines.append(
        f"Needs approval (over {format_rupees(approval_limit)}): "
        f"{len(approval_expenses)}"
    )

    for expense in approval_expenses:
        report_lines.append(
            f"  - {expense['item']}: {format_rupees(expense['amount'])}"
        )

    return "\n".join(report_lines)


def save_summary(path, summary):
    # Save the required machine-readable totals and report whether it worked.
    try:
        with open(path, "w", encoding="utf-8") as summary_file:
            json.dump(summary, summary_file, indent=4)
            summary_file.write("\n")
    except OSError as error:
        print(f"Could not write {path}: {error}.")
        return False

    return True


def main():
    # Load, summarize, save, and display the report in that order.
    expenses = load_expenses(EXPENSES_FILE)
    if expenses is None:
        return False

    summary = {
        "expense_count": len(expenses),
        "total": total_spent(expenses),
        "by_category": category_totals(expenses),
    }

    if not save_summary(SUMMARY_FILE, summary):
        return False

    print(build_report(expenses, APPROVAL_LIMIT))
    return True


if __name__ == "__main__":
    main()
