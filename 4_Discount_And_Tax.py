phone_price = 15000
discount_rate = 10
tax_rate = 18

discounted_price = phone_price * (1 - discount_rate / 100)
discount_then_tax = discounted_price * (1 + tax_rate / 100)

taxed_price = phone_price * (1 + tax_rate / 100)
tax_then_discount = taxed_price * (1 - discount_rate / 100)

print(f"Total after discount then tax: Rs. {discount_then_tax:.2f}")
print(f"Total after tax then discount: Rs. {tax_then_discount:.2f}")
# The results are the same because multiplying by the tax and discount factors
# in either order gives the same product.