# Q3. Shipping as a Function
# Charge Rs 200 for Karachi, Lahore, and Islamabad, or Rs 350 for other
# cities. Double the charge above 5 kg. Orders over Rs 10,000 ship free.
# Clean the city name and test at least four examples, including 5 kg.

def format_rupees(amount):
    return f"Rs {amount:,}"


def shipping_charge(weight_kg, city, order_total=0):
    cleaned_city = city.strip().title()

    # Apply the free-shipping rule from the earlier exercise.
    if order_total > 10000:
        return 0

    if cleaned_city in ["Karachi", "Lahore", "Islamabad"]:
        charge = 200
    else:
        charge = 350

    if weight_kg > 5:
        charge *= 2

    return charge


shipping_examples = [
    (3, " karachi ", 9000),
    (5, "Lahore", 2000),
    (6, "Islamabad", 3500),
    (5, "Peshawar", 4000),
    (6, "Peshawar", 15000),
]

for weight_kg, city, order_total in shipping_examples:
    cleaned_city = city.strip().title()
    charge = shipping_charge(weight_kg, city, order_total)
    print(f"Shipping to {cleaned_city}: {format_rupees(charge)}")
