# Practice: Lists and Dictionaries
#
# 11. A product record.
#
# Create a list of three prices: [850, 1200, 400]. Print the last price
# and the sum of all three. Then create a dictionary for one product with
# the keys name, price and in_stock. Change in_stock to False and print
# just the product's name.

prices = [850, 1200, 400]
print(f"Last price: {prices[-1]}")
print(f"Total: {sum(prices)}")

product = {"name": "Laptop", "price": 1200, "in_stock": True}
product["in_stock"] = False
print(product["name"])