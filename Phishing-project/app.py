import pandas as pd
import random
from datetime import datetime, timedelta
import numpy as np

# Lists of content for generating synthetic emails
legitimate_senders = [
    "support@bank-kenya.com", "info@trustbank.co.ke", "service@nationalbank.ke",
    "customercare@standardbank.co.ke", "help@equitybank.co.ke"
]

phishing_senders = [
    "suport@bank-kenya.com", "info@trustbank-ke.com", "service@national-bank.com",
    "customer.care@standardbank-kenya.com", "help@equity-bank.online"
]

urgent_words = [
    "Urgent", "Immediate action required", "Warning", "Account Alert",
    "Security Notice", "Urgent Update Needed"
]

legitimate_subjects = [
    "Monthly Statement Available", "New Security Features", "Banking Hours Update",
    "Holiday Banking Schedule", "New Mobile App Features"
]

phishing_subjects = [
    "Your account has been suspended", "Verify your account immediately",
    "Urgent: Unusual activity detected", "Security breach - action required",
    "Confirm your details now"
]

def generate_legitimate_content():
    return random.choice([
        "Your monthly statement is now available. Log in to our secure portal to view.",
        "We've updated our mobile banking app. Visit our official website to learn more.",
        "Please note our revised banking hours for the upcoming holiday.",
        "Thank you for your continued trust in our banking services."
    ])

def generate_phishing_content():
    return random.choice([
        "Your account has been compromised. Click here to verify your details immediately: {suspicious_link}",
        "Due to a system upgrade, you must confirm your account information: {suspicious_link}",
        "Unusual activity detected in your account. Verify your identity now: {suspicious_link}",
        "Your account will be suspended unless you update your information: {suspicious_link}"
    ]).replace("{suspicious_link}", f"http://{random.choice(['secure-banking-verify.com', 'bank-verify-account.net', 'account-security-check.com'])}")

def generate_email():
    is_phishing = random.random() < 0.5  # 50% chance of being a phishing email
    
    if is_phishing:
        sender = random.choice(phishing_senders)
        subject = random.choice(phishing_subjects)
        content = generate_phishing_content()
        urgent = random.choice(urgent_words) if random.random() < 0.8 else ""
    else:
        sender = random.choice(legitimate_senders)
        subject = random.choice(legitimate_subjects)
        content = generate_legitimate_content()
        urgent = random.choice(urgent_words) if random.random() < 0.2 else ""
    
    return {
        'sender': sender,
        'subject': subject,
        'content': content,
        'urgent_language': urgent,
        'contains_link': 1 if 'http' in content else 0,
        'spelling_errors': 1 if is_phishing and random.random() < 0.7 else 0,
        'request_personal_info': 1 if is_phishing and random.random() < 0.8 else 0,
        'date': (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d'),
        'is_phishing': 1 if is_phishing else 0
    }

# Generate dataset
data = [generate_email() for _ in range(1000)]
df = pd.DataFrame(data)

# Save to Excel
output_file = 'kenyan_banking_phishing_dataset.xlsx'
df.to_excel(output_file, index=False)

print(f"Dataset has been generated and saved to {output_file}")
print(f"Total emails: {len(df)}")
print(f"Phishing emails: {df['is_phishing'].sum()}")
print(f"Legitimate emails: {len(df) - df['is_phishing'].sum()}")