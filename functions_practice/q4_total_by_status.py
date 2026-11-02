# Q4. Totals by Status
# Create total_by_status(orders, status) to return the sum of totals for
# orders matching the requested status.

orders = [
    {"id": "A101", "customer": "Ali", "total": 4200, "status": "delivered"},
    {"id": "A102", "customer": "Noor", "total": 12800, "status": "pending"},
    {"id": "A103", "customer": "Hina", "total": 2600, "status": "delivered"},
]


def total_by_status(orders, status):
    matching_total = 0

    for order in orders:
        if order["status"] == status:
            matching_total += order["total"]

    return matching_total


print(f"delivered -> {total_by_status(orders, 'delivered')}")
print(f"pending -> {total_by_status(orders, 'pending')}")
print(f"cancelled -> {total_by_status(orders, 'cancelled')}")
