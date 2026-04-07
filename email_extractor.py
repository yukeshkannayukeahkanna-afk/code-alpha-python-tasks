import re

# Read the text file
with open("emails.txt", "r") as file:
    text = file.read()

# Regex pattern for emails
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)

# Save extracted emails
with open("extracted_emails.txt", "w") as output:
    for email in emails:
        output.write(email + "\n")

print("Emails extracted successfully!")
