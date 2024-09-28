import random
import string
import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Kenyan bank names (for demonstration purposes)
kenyan_banks = [
    "Equity Bank", "Kenya Commercial Bank", "Co-operative Bank", "Absa Bank Kenya",
    "Standard Chartered Bank Kenya", "NCBA Bank", "Diamond Trust Bank", "I&M Bank",
    "Family Bank", "Bank of Africa Kenya"
]

# Common phishing keywords
phishing_keywords = [
    "urgent", "account suspended", "verify your account", "login attempt",
    "security alert", "update your information", "claim your reward",
    "unusual activity", "password reset", "account locked"
]

def generate_random_email(is_phishing):
    sender = fake.email()
    subject = fake.sentence()
    body = fake.paragraph()

    if is_phishing:
        # Add phishing elements
        bank = random.choice(kenyan_banks)
        keyword = random.choice(phishing_keywords)
        subject = f"{bank}: {keyword.capitalize()}"
        body = f"Dear valued customer,\n\n{body}\n\nClick here to {keyword}: http://{fake.domain_name()}/secure-login"
    else:
        # Add legitimate-looking elements
        if random.random() < 0.3:  # 30% chance of being a bank email
            bank = random.choice(kenyan_banks)
            subject = f"{bank}: {subject}"
            body = f"Dear valued customer,\n\n{body}\n\nBest regards,\n{bank} Customer Service"

    return {
        "sender": sender,
        "subject": subject,
        "body": body,
        "is_phishing": int(is_phishing)
    }

# Generate 20,000 emails
num_emails = 20000
emails = []

for _ in range(num_emails):
    is_phishing = random.random() < 0.4  # 40% chance of being a phishing email
    emails.append(generate_random_email(is_phishing))

# Create a DataFrame
df = pd.DataFrame(emails)

# Save to Excel file
excel_file = "kenyan_banking_emails.xlsx"
df.to_excel(excel_file, index=False)

print(f"{num_emails} emails generated and saved to {excel_file}")