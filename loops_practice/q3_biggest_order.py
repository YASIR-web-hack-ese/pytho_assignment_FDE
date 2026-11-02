# Q3. The Biggest Order
# Find and print the order with the highest total. If two orders tie for
# the highest total, this solution keeps the first one encountered.

orders = [
    {"id": "A101", "customer": "Ali", "total": 4200},
    {"id": "A102", "customer": "Noor", "total": 12800},
    {"id": "A103", "customer": "Hina", "total": 9600},
]

biggest_order = orders[0]

# Replace the current biggest order whenever a larger total is found.
for order in orders:
    if order["total"] > biggest_order["total"]:
        biggest_order = order

print(
    f"Biggest order: {biggest_order['id']} "
    f"(Rs {biggest_order['total']:,})"
)
