subtotal = 7200
tax_rate = 18

tax = subtotal * tax_rate /100
total = subtotal + tax

print(tax)
print(total)
print(type(tax))
# Division with / produces a float, even when both input values are integers.