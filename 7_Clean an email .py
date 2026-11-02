# 7. Clean an email.
#
# Clean " Ali.Khan@GMAIL.com " so it has no spaces and is all lowercase,
# then print:
# Email: ali.khan@gmail.com (18 characters)

email = " Ali.Khan@GMAIL.com ".strip().lower()
print(f"Email: {email} ({len(email)} characters)")