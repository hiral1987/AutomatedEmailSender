
# 📧 Automated Email Sender using Python

This project is a Python-based tool to send **personalized emails in bulk** using Gmail SMTP. It reads recipient details from an Excel file and sends custom email messages to each recipient.

---

## ✨ Features

- Sends personalized emails using recipient names
- Reads data from an Excel (`.xlsx`) file
- Uses Gmail's SMTP server for email delivery
- Supports plain text
- Simple and configurable

---

## 📁 Folder Structure

```
AutomatedEmailSender/
│
├── automated_email_sender.py      # Main script
├── recipients.xlsx                # Excel file with Name and Email columns
└── README.md                      # Project documentation
```

---

## 📄 Excel Format (`recipients.xlsx`)

| Name          | Email                |
|---------------|----------------------|
| Alice Johnson | alice@example.com    |
| Bob Smith     | bob@example.com      |

> Ensure there are no empty rows or missing values in the Name or Email columns.

---

## ⚙️ Configuration

Update the following variables in the script:

```python
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_app_password'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
```

> 🔐 If using Gmail, generate an **App Password** under [Google Account > Security > App Passwords](https://myaccount.google.com/apppasswords)

---

## 🚀 How to Run

1. Install required package:
   ```bash
   pip install pandas openpyxl
   ```

2. Run the script:
   ```bash
   python automated_email_sender.py
   ```

---

## 📬 Notes

- Make sure 2-Step Verification is enabled in Gmail.
- Use an [App Password](https://support.google.com/mail/answer/185833?hl=en) instead of your normal password.
- Gmail limits number of emails sent per day (usually 500 for personal accounts).

---

## 📌 To Do (Optional Features)

- [ ] Add support for attachments
- [ ] Add support for rich HTML email templates
- [ ] Add email scheduling (using cron or APScheduler)
- [ ] Add logging and error report export

---

## 🧑‍💻 Author

**Hiral Dharod**

> You’re welcome to contribute or customize the script to fit your team or business needs!
