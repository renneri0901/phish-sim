import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_phishing_email(sender_email, password, receiver_email, subject, body, tracking_url):
    """Function to send a phishing email with configurable values."""
    
    # Email details
    subject = subject
    body = body.replace("YOUR_SERVER", tracking_url)  # Replace tracking URL placeholder

    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach HTML body
    msg.attach(MIMEText(body, 'html'))

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        server.quit()
