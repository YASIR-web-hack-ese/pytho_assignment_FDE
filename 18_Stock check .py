# Practice: Making Decisions with if
#
# 18. Stock check.
#
# Given stock = 12 and quantity, print:
# - "Invalid quantity" if the quantity is 0 or less.
# - "Only 12 left in stock" if the quantity is more than the stock.
# - "Confirmed. 7 left after this order" otherwise (for a quantity of 5).
# Work out every number in the message from the variables.

stock = 12
quantity = 5

if quantity <= 0:
    print("Invalid quantity")
elif quantity > stock:
    print(f"Only {stock} left in stock")
else:
    remaining = stock - quantity
    print(f"Confirmed. {remaining} left after this order")