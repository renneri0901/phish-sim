import unittest
from unittest.mock import patch, mock_open
from websitespoofer import app, ResetHTML, ChangeHTML
import os
import datetime

class TestWebsiteSpoofer(unittest.TestCase):

    @patch('websitespoofer.render_template_string')  # Mock render_template_string to avoid rendering HTML in tests
    def test_login_page(self, mock_render):
        """Test the login page rendering."""
        mock_render.return_value = "Login Page HTML"
        
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.data.decode(), "Login Page HTML")

    @patch('websitespoofer.open', mock_open())  # Mock open to avoid writing to a real file
    def test_login_post(self):
        """Test the POST method for login."""
        with app.test_client() as client:
            # Simulate POST request with email and password
            response = client.post('/', data={'email': 'test@example.com', 'password': 'password123'})
            # Ensure credentials are written to log.txt
            open.assert_called_with("log.txt", "a")
            # Check if the data was written in the correct format
            mock_file = open()
            mock_file.write.assert_called_with(f"{datetime.datetime.now()} | test@example.com:password123\n")
            self.assertIn("Login failed. Try again later.", response.data.decode())

    @patch('websitespoofer.open', mock_open(read_data="Fake HTML content"))
    def test_change_html(self):
        """Test if ChangeHTML correctly updates the LOGIN_HTML."""
        test_html = "new_login.html"
        
        # Simulate reading a new HTML file
        ChangeHTML(test_html)
        
        # Check if the LOGIN_HTML was updated by reading the file contents
        with open(test_html, 'r') as file:
            content = file.read()
        
        self.assertEqual(content, "Fake HTML content")

    @patch('websitespoofer.open', mock_open())
    def test_reset_html(self):
        """Test if ResetHTML correctly restores the original HTML."""
        # Change the LOGIN_HTML first
        ChangeHTML("new_login.html")
        
        # Ensure that the HTML has been changed
        self.assertNotEqual(app.view_functions['/'](), "Secure Login Page")
        
        # Reset the HTML back to the original
        ResetHTML()
        
        # Ensure that the HTML has been restored to the original template
        self.assertEqual(app.view_functions['/'](), "Secure Login Page")
        
    def tearDown(self):
        """Clean up any files or resources after tests."""
        if os.path.exists('log.txt'):
            os.remove('log.txt')  # Clean up the log file created during tests

if __name__ == '__main__':
    unittest.main()
