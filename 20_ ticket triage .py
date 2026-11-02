# Practice: Making Decisions with if
#
# 20. Ticket triage.
#
# A support ticket has a plan ("free", "pro" or "enterprise"),
# hours_open and a message. Use string searching with in to determine
# priority:
# - Urgent if the plan is enterprise and it has been open more than
#   4 hours.
# - High if the message mentions "refund" or "charged twice" in any
#   capitalisation, or the plan is pro and it has been open more than
#   24 hours.
# - Normal otherwise.

cases = [
    ("enterprise", 5, "Payment failed"),
    ("pro", 25, "refund requested"),
    ("free", 1, "normal request"),
    ("enterprise", 3, "charged twice"),
    ("pro", 20, "issue report")
]

for plan, hours_open, message in cases:
    text = message.lower()

    if plan == "enterprise" and hours_open > 4:
        priority = "Urgent"
    elif ("refund" in text or "charged twice" in text) or (plan == "pro" and hours_open > 24):
        priority = "High"
    else:
        priority = "Normal"

    print(f"Plan: {plan}, Hours: {hours_open}, Message: {message} -> {priority}")