# Practice: Lists and Dictionaries
#
# 12. A week of sales.
#
# Store a shop's daily sales for one week in a list:
# [18500, 22300, 19800, 25400, 31200, 42800, 38600]
# Print Monday's and Sunday's sales, the weekly total and the daily
# average, formatted as Rs with commas and no decimals. Then look up
# max() and min() and print the best and worst days' sales.

sales = [18500, 22300, 19800, 25400, 31200, 42800, 38600]
print(f"Monday: Rs {sales[0]:,}")
print(f"Sunday: Rs {sales[-1]:,}")
weekly_total = sum(sales)
print(f"Weekly total: Rs {weekly_total:,}")
daily_average = weekly_total / len(sales)
print(f"Daily average: Rs {daily_average:,.0f}")
print(f"Best day: Rs {max(sales):,}")
print(f"Worst day: Rs {min(sales):,}")