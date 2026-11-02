# Q2. Numbered Items
# Print each price with an item number, calculate the total, and count how
# many prices are greater than Rs 1,000.

prices = [850, 1200, 400, 3100, 650]

item_number = 1
total_price = 0
items_over_1000 = 0

for price in prices:
    print(f"Item {item_number}: Rs {price:,}")
    total_price += price

    if price > 1000:
        items_over_1000 += 1

    item_number += 1

print(f"Total price: Rs {total_price:,}")
print(f"Items above Rs 1,000: {items_over_1000}")
