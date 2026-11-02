# Practice: Lists and Dictionaries
#
# 15. A customer profile.
#
# Build one dictionary for a customer that contains a nested dictionary
# and a list. Print the customer's city, their number of orders and the
# total they've spent. Add a new order of Rs 6,100, then print the new
# total. Finally, use the dictionary .get() method to print
# "No phone number" instead of crashing if the phone number does not
# exist.

customer = {
    "name": "Ayesha",
    "city": "Karachi",
    "orders": [
        {"id": "O1", "total": 4500},
        {"id": "O2", "total": 6400}
    ],
    "details": {"member": "gold"}
}
print(customer["city"])
print(len(customer["orders"]))
print(sum(order["total"] for order in customer["orders"]))
customer["orders"].append({"id": "O3", "total": 6100})
print(sum(order["total"] for order in customer["orders"]))
print(customer.get("details", {}).get("phone", "No phone number"))