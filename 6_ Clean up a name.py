# 6. Clean up a name.
#
# A form gave you the name " aMNA rAZA ". Clean it so it reads Amna Raza
# (look up the .title() method), then print:
# Welcome, Amna Raza! Your name has 9 characters.
# Use an f-string and len().

name = " aMNA rAZA ".strip().title()
print(f"Welcome, {name}! Your name has {len(name)} characters.")