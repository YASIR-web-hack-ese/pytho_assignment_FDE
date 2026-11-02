# 8. A receipt line.
#
# The item name is " wireless MOUSE ", the price is 2499 and the quantity
# is 3. Print exactly:
# Wireless Mouse x3 = Rs 7,497
# Work out the total in code; do not type the number.

item_name = " wireless MOUSE ".strip().title()
price = 2499
quantity = 3
total = price * quantity
print(f"{item_name} x{quantity} = Rs {total:,}")