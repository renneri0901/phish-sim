import unittest
from unittest.mock import patch, MagicMock
from phishing_email import send_phishing_email

class TestPhishingEmail(unittest.TestCase):

    @patch('smtplib.SMTP')  # Mock the smtplib.SMTP class
    def test_send_phishing_email_success(self, MockSMTP):
        # Create a mock SMTP object
        mock_smtp_instance = MagicMock()
        MockSMTP.return_value = mock_smtp_instance
        
        # Define test email parameters
        sender_email = 'sender@example.com'
        password = 'password123'
        receiver_email = 'receiver@example.com'
        subject = 'Suspicious Login Attempt'
        body = """
        <html>
        <body>
        <p>Dear Customer,</p>
        <p>We detected suspicious activity...</p>
        </body>
        </html>
        """
        tracking_url = 'http://localhost:5000/track_click'

        # Call the function to test
        send_phishing_email(sender_email, password, receiver_email, subject, body, tracking_url)

        # Assert that the SMTP server was initialized correctly
        MockSMTP.assert_called_once_with('smtp.gmail.com', 587)
        
        # Assert the server started TLS encryption
        mock_smtp_instance.starttls.assert_called_once()
        
        # Assert the login was called with correct credentials
        mock_smtp_instance.login.assert_called_once_with(sender_email, password)
        
        # Assert the sendmail method was called to send the email
        mock_smtp_instance.sendmail.assert_called_once_with(sender_email, receiver_email, MagicMock())

        # Check that the body contains the correct tracking URL
        args, _ = mock_smtp_instance.sendmail.call_args
        email_body = args[2]  # Extract the email body from the sendmail call args
        self.assertIn(tracking_url, email_body)

    @patch('smtplib.SMTP')  # Mock the smtplib.SMTP class
    def test_send_phishing_email_failure(self, MockSMTP):
        # Simulate a failure in sending the email by raising an exception
        mock_smtp_instance = MagicMock()
        MockSMTP.return_value = mock_smtp_instance
        mock_smtp_instance.sendmail.side_effect = Exception("SMTP error")

        sender_email = 'sender@example.com'
        password = 'password123'
        receiver_email = 'receiver@example.com'
        subject = 'Suspicious Login Attempt'
        body = """
        <html>
        <body>
        <p>Dear Customer,</p>
        <p>We detected suspicious activity...</p>
        </body>
        </html>
        """
        tracking_url = 'http://localhost:5000/track_click'

        # Call the function to test
        with self.assertRaises(Exception):  # Check if an exception is raised
            send_phishing_email(sender_email, password, receiver_email, subject, body, tracking_url)

        # Ensure the sendmail method was still called
        mock_smtp_instance.sendmail.assert_called_once()

if __name__ == '__main__':
    unittest.main()
