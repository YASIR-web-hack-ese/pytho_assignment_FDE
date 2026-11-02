# Q1. Delivered Revenue
# Using the sample orders, add the totals of delivered orders and print the
# result. The expected delivered revenue is Rs 6,800.

orders = [
    {"id": "A101", "customer": "Ali", "total": 4200, "status": "delivered"},
    {"id": "A102", "customer": "Noor", "total": 12800, "status": "pending"},
    {"id": "A103", "customer": "Hina", "total": 2600, "status": "delivered"},
]

revenue_total = 0

# Only add an order's total when its status is delivered.
for order in orders:
    if order["status"] == "delivered":
        revenue_total += order["total"]

print(f"Delivered revenue: Rs {revenue_total:,}")
