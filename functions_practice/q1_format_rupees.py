# Q1. Formatting Rupees
# Create format_rupees(amount) to return a comma-formatted rupee amount.
# Test the sample amounts and print the amount Noor Foods owes.

def format_rupees(amount):
    return f"Rs {amount:,}"


print(format_rupees(12800))
print(format_rupees(999))
print(format_rupees(1250000))
print(f"Noor Foods owes {format_rupees(11520)}")
