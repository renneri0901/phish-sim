import unittest
from flask import Flask
from tracking_server import app
from unittest.mock import patch
import os

class TestTrackingServer(unittest.TestCase):
    def setUp(self):
        """Set up the test client and any necessary initializations."""
        # Set up a test client for Flask
        self.client = app.test_client()
        # Set up the path to the clicks log file
        self.log_file_path = "clicks.log"
        if os.path.exists(self.log_file_path):
            os.remove(self.log_file_path)  # Remove if it exists from previous tests

    def test_track_click_success(self):
        """Test that clicks are logged correctly."""
        email_id = "test_email_id"
        # Simulate a GET request to the /track_click route
        response = self.client.get(f'/track_click/{email_id}')
        
        # Check if the redirect response status code is 302 (indicating a redirect)
        self.assertEqual(response.status_code, 302)

        # Wait for the log file to be written
        with open(self.log_file_path, "r") as f:
            log_content = f.readlines()

        # Assert that the log contains the correct data
        self.assertTrue(len(log_content) > 0)
        self.assertIn(f"Link clicked from", log_content[-1])  # Check if it contains the expected phrase
        self.assertIn(f"Email ID: {email_id}", log_content[-1])  # Check if the email ID is logged

    def test_track_click_invalid_email(self):
        """Test handling of an invalid email ID."""
        email_id = "invalid_email_id"
        # Simulate a GET request to the /track_click route
        response = self.client.get(f'/track_click/{email_id}')
        
        # Check if the redirect response status code is 302 (indicating a redirect)
        self.assertEqual(response.status_code, 302)

        # Wait for the log file to be written
        with open(self.log_file_path, "r") as f:
            log_content = f.readlines()

        # Assert that the log contains the correct data
        self.assertTrue(len(log_content) > 0)
        self.assertIn(f"Link clicked from", log_content[-1])  # Check if it contains the expected phrase
        self.assertIn(f"Email ID: {email_id}", log_content[-1])  # Check if the email ID is logged

    @patch('tracking_server.redirect')  # Mock the redirect to avoid actual redirect
    def test_tracking_server_redirect(self, mock_redirect):
        """Test that the redirect works as expected."""
        email_id = "test_email_for_redirect"
        
        # Simulate a GET request to the /track_click route
        response = self.client.get(f'/track_click/{email_id}')
        
        # Assert the response is a redirect (HTTP 302)
        self.assertEqual(response.status_code, 302)
        
        # Assert that the redirect was called with the expected login page
        mock_redirect.assert_called_once_with("YOUR_LOGIN_PAGE")  # Replace with actual login page URL if needed

    def tearDown(self):
        """Clean up any files or resources after tests."""
        if os.path.exists(self.log_file_path):
            os.remove(self.log_file_path)  # Remove the log file after testing

if __name__ == '__main__':
    unittest.main()
