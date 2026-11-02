# Practice: Making Decisions with if
#
# 19. Shipping rules.
#
# Given weight_kg, order_total and city, work out the shipping charge:
# - Orders over Rs 10,000 ship free anywhere.
# - Karachi, Lahore and Islamabad: Rs 200 up to 5 kg, Rs 400 above that.
# - Every other city: Rs 350 up to 5 kg, Rs 700 above that.
# Clean the city first so " karachi " counts as Karachi. Print:
# Shipping to Karachi: Rs 200
# Test at least five combinations, including exactly 5 kg.

samples = [
    (3, 9000, " karachi "),
    (6, 9000, "Karachi"),
    (5, 2000, "Lahore"),
    (6, 3500, "Islamabad"),
    (5, 15000, "Peshawar"),
    (6, 15000, "Peshawar")
]

for weight_kg, order_total, city in samples:
    cleaned_city = city.strip().title()

    if order_total > 10000:
        shipping_charge = 0
    elif cleaned_city in ["Karachi", "Lahore", "Islamabad"]:
        shipping_charge = 200 if weight_kg <= 5 else 400
    else:
        shipping_charge = 350 if weight_kg <= 5 else 700

    print(f"Shipping to {cleaned_city}: Rs {shipping_charge}")