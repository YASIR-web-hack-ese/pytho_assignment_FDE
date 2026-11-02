# Q2. Return or Print?
# Implement add_tax(subtotal, rate=0.18), test both rates, then compare it
# with a version that prints the calculation instead of returning it.

def add_tax(subtotal, rate=0.18):
    # Return the subtotal plus the calculated tax.
    return subtotal + subtotal * rate


print(add_tax(7200))
print(add_tax(7200, 0.05))


def add_tax_and_print(subtotal, rate=0.18):
    # This displays the result but does not return it to the caller.
    print(subtotal + subtotal * rate)


tax_result = add_tax_and_print(7200)
print(tax_result)

# The print-only function implicitly returns None, so tax_result is None.
