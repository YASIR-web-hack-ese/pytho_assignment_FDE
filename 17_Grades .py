# Practice: Making Decisions with if
#
# 17. Grades.
#
# Given marks, print A for 80 and above, B for 65-79, C for 50-64 and
# Fail below 50. Test with exactly 80, 79, 50 and 49.

for marks in [80, 79, 50, 49]:
    if marks >= 80:
        grade = "A"
    elif marks >= 65:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print(f"Marks: {marks} -> Grade {grade}")