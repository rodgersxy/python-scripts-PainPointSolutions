import random
import string
import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Kenyan bank and financial institution names
kenyan_financial_institutions = [
    "Equity Bank", "Kenya Commercial Bank (KCB)", "Co-operative Bank", "Absa Bank Kenya",
    "Standard Chartered Bank Kenya", "NCBA Bank", "Diamond Trust Bank", "I&M Bank",
    "Family Bank", "Bank of Africa Kenya", "Stanbic Bank", "Barclays Bank Kenya",
    "CBA Bank", "NIC Bank", "Housing Finance Company of Kenya", "Chase Bank Kenya",
    "Central Bank of Kenya", "Safaricom M-PESA", "Airtel Money", "Kenya Post Office Savings Bank",
    "SACCOs", "Kenya Bankers Association", "Capital Markets Authority", "Insurance Regulatory Authority"
]

# Comprehensive list of phishing keywords and phrases for Kenyan banking and finance sector
phishing_keywords = [
    "urgent account verification", "mpesa pin reset", "loan approved", "account suspended",
    "verify your account", "unusual login attempt", "security alert", "update your information",
    "claim your reward", "account locked", "mobile banking update required", "tax refund available",
    "government stimulus payment", "win a new car", "lottery winner", "inheritance claim",
    "investment opportunity", "business proposal", "rate change alert", "credit card offer",
    "debt consolidation", "loan pre-approval", "account closure notice", "free gift card",
    "bank merger notice", "system upgrade required", "sim swap protection", "fraud alert",
    "mobile money transfer issue", "kyc update needed", "account dormancy warning",
    "new security feature activation", "bank statement available", "password expiry notice",
    "branch closure information", "atm card renewal", "digital wallet upgrade", "interest rate change",
    "mobile app mandatory update", "account balance discrepancy", "cheque book request confirmation",
    "credit score improvement offer", "instant loan approval", "bank holiday notice",
    "account reactivation required", "payment failed notification", "successful transaction reversal",
    "bank charges refund", "new banking regulation compliance", "account upgrade offer"
]

def generate_random_email(is_phishing):
    sender = fake.email()
    subject = fake.sentence()
    body = fake.paragraph()

    if is_phishing:
        # Add phishing elements
        institution = random.choice(kenyan_financial_institutions)
        keyword = random.choice(phishing_keywords)
        subject = f"{institution}: {keyword.capitalize()}"
        body = (f"Dear esteemed customer,\n\n"
                f"{body}\n\n"
                f"Urgent: {keyword}. Click here to take action: "
                f"http://{fake.domain_name()}/secure-portal\n\n"
                f"Failure to act may result in account suspension.\n\n"
                f"Best regards,\n{institution} Customer Service Team")
    else:
        # Add legitimate-looking elements
        if random.random() < 0.3:  # 30% chance of being a bank email
            institution = random.choice(kenyan_financial_institutions)
            subject = f"{institution}: {subject}"
            body = (f"Dear valued customer,\n\n"
                    f"{body}\n\n"
                    f"For any inquiries, please visit our official website or contact our customer service.\n\n"
                    f"Best regards,\n{institution} Customer Service")

    return {
        "sender": sender,
        "subject": subject,
        "body": body,
        "is_phishing": int(is_phishing)
    }

# Generate 30,000 emails
num_emails = 30000
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