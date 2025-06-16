import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ------------------------ CONFIGURATION ------------------------
# Update these with your own details
SMTP_SERVER = 'smtp.gmail.com'  # e.g., for Gmail
SMTP_PORT = 587
EMAIL_ADDRESS = 'hiral.dharod@gmail.com'
# EMAIL_PASSWORD = 'Hir@l@982108'  # Use App Password if 2FA is enabled
EMAIL_PASSWORD = 'ceae qhtl udgq uacg'  # Use App Password if 2FA is enabled

EXCEL_FILE = 'recipients.xlsx'  # Must have columns: Name, Email
SUBJECT = 'Hello from Python!'
BODY_TEMPLATE = '''
Dear {name},

This is a personalized message sent via our automated Python script.

Best regards,
Your Name
'''
# ---------------------------------------------------------------

def read_recipients(file_path):
    """Reads recipient names and emails from an Excel file."""
    try:
        df = pd.read_excel(file_path)
        return df[['Name', 'Email']].dropna()
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return pd.DataFrame()

def send_email(to_email, to_name):
    """Sends a personalized email."""
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = SUBJECT

        body = BODY_TEMPLATE.format(name=to_name)
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"✅ Email sent to {to_name} ({to_email})")

    except Exception as e:
        print(f"❌ Failed to send email to {to_email}: {e}")

def main():
    recipients = read_recipients(EXCEL_FILE)
    if recipients.empty:
        print("No recipients to send to.")
        return

    for index, row in recipients.iterrows():
        send_email(row['Email'], row['Name'])

if __name__ == "__main__":
    main()