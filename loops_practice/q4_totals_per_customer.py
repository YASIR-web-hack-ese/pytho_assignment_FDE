# Q4. Totals Per Customer
# Add together all order totals for each customer and print the resulting
# dictionary's entries.

orders = [
    {"customer": "Noor Foods", "total": 4500},
    {"customer": "Karachi Crafts", "total": 12800},
    {"customer": "Noor Foods", "total": 2300},
    {"customer": "Bilal Traders", "total": 7600},
    {"customer": "Karachi Crafts", "total": 3900},
    {"customer": "Noor Foods", "total": 6100},
]

customer_totals = {}

# Add to an existing customer total or create a new dictionary entry.
for order in orders:
    customer = order["customer"]
    if customer in customer_totals:
        customer_totals[customer] += order["total"]
    else:
        customer_totals[customer] = order["total"]

for customer, total in customer_totals.items():
    print(f"{customer}: Rs {total:,}")
