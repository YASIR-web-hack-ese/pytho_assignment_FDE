# Q5. Refactor the Reorder Report
# Use needs_reorder(), reorder_quantity(), and reorder_cost() to produce
# the inventory report. The expected total cost is Rs 8,920.

inventory = [
    {"name": "Notebook", "stock": 8, "reorder_level": 15, "unit_cost": 90},
    {"name": "Pen", "stock": 140, "reorder_level": 50, "unit_cost": 25},
    {"name": "Stapler", "stock": 2, "reorder_level": 5, "unit_cost": 650},
    {"name": "Marker", "stock": 30, "reorder_level": 30, "unit_cost": 120},
    {"name": "Folder", "stock": 11, "reorder_level": 20, "unit_cost": 60},
]


def format_rupees(amount):
    return f"Rs {amount:,}"


def needs_reorder(product):
    return product["stock"] < product["reorder_level"]


def reorder_quantity(product):
    target_stock = 2 * product["reorder_level"]
    return target_stock - product["stock"]


def reorder_cost(product):
    return reorder_quantity(product) * product["unit_cost"]


total_reorder_cost = 0
reorders_found = False

for product in inventory:
    if needs_reorder(product):
        quantity = reorder_quantity(product)
        cost = reorder_cost(product)
        print(
            f"Reorder {quantity} x {product['name']} "
            f"({format_rupees(cost)})"
        )
        total_reorder_cost += cost
        reorders_found = True

if reorders_found:
    print(f"Total Cost: {format_rupees(total_reorder_cost)}")
else:
    print("All stock OK")

# Small functions keep the report readable and let each rule be tested,
# maintained, or modified independently.
