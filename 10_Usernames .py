# 10. Usernames.
#
# You have:
# first = " bilal "
# last = "QURESHI "
# city = "lahore"
#
# Look up string slicing (for example text[0:3]). Build the username
# bilal.qureshi_lah (lowercase first name, a dot, lowercase last name,
# an underscore and the first three letters of the city), then print:
#
# Welcome, Bilal Qureshi from Lahore!
#
# Your username is bilal.qureshi_lah (17 characters).
#
# Change the three starting values to your own name and city, and check
# that it still works.

first = " bilal ".strip().lower()
last = "QURESHI ".strip().lower()
city = "lahore"
username = f"{first}.{last}_{city[:3]}"
print(f"Welcome, {first.title()} {last.title()} from {city.title()}!")
print(f"Your username is {username} ({len(username)} characters).")