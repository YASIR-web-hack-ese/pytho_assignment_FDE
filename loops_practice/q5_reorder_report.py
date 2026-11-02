# Q5. Reorder Report
# Report products whose stock is below the reorder level. Order enough to
# reach twice the reorder level, and print the combined reorder cost.

inventory = [
    {"name": "Notebook", "stock": 8, "reorder_level": 15, "unit_cost": 90},
    {"name": "Pen", "stock": 140, "reorder_level": 50, "unit_cost": 25},
    {"name": "Stapler", "stock": 2, "reorder_level": 5, "unit_cost": 650},
    {"name": "Marker", "stock": 30, "reorder_level": 30, "unit_cost": 120},
    {"name": "Folder", "stock": 11, "reorder_level": 20, "unit_cost": 60},
]

total_reorder_cost = 0
reorders_found = False

for product in inventory:
    if product["stock"] < product["reorder_level"]:
        target_stock = 2 * product["reorder_level"]
        quantity_to_reorder = target_stock - product["stock"]
        product_reorder_cost = quantity_to_reorder * product["unit_cost"]

        print(
            f"Reorder {quantity_to_reorder} x {product['name']} "
            f"(Rs {product_reorder_cost:,})"
        )
        total_reorder_cost += product_reorder_cost
        reorders_found = True

if reorders_found:
    print(f"Total Cost: Rs {total_reorder_cost:,}")
else:
    print("All stock OK")

# Marker is not listed because its stock equals its reorder level; it is not
# below the level.
