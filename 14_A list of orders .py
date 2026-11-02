# Practice: Lists and Dictionaries
#
# 14. A list of orders.
#
# Create a list of three order dictionaries, each with id, customer and
# total. Without a loop:
# - Print the customer of the second order.
# - The third order gets a Rs 500 discount: change its total.
# - Add a fourth order to the end of the list.
# - Print "4 orders. The first is A101 and the last is A104.", taking
#   every value from the list.

orders = [
    {"id": "A101", "customer": "Ali", "total": 4200},
    {"id": "A102", "customer": "Noor", "total": 6800},
    {"id": "A103", "customer": "Hina", "total": 9600}
]

print(orders[1]["customer"])
orders[2]["total"] -= 500
orders.append({"id": "A104", "customer": "Usman", "total": 12000})
print(f"4 orders. The first is {orders[0]['id']} and the last is {orders[-1]['id']}.")