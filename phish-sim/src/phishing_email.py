import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email details
sender_email = "your_email@gmail.com"  # Your email address
receiver_email = "target_email@example.com"  # Target's email address
password = "your_password"  # Use an app-specific password if using Gmail
subject = "Important Account Update!"
body = """Dear User,

We noticed some suspicious activity on your account. Please click the link below to verify your account:

http://fake-website.com/verify

Thank you,
The Security Team

<!-- Invisible Tracking Pixel -->
<img src="http://your-server-ip:5000/track/email123" width="1" height="1" />
"""

# Set up the MIME (email structure)
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the email body
msg.attach(MIMEText(body, 'html'))

# Send the email via Gmail's SMTP server
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Secure the connection
    server.login(sender_email, password)  # Login to your Gmail account
    
    # Send the email
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    
    print("Email sent successfully!")
    
except Exception as e:
    print(f"Error: {str(e)}")

finally:
    server.quit()
