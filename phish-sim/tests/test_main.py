import unittest
from unittest.mock import patch, MagicMock
import main

class TestMain(unittest.TestCase):

    @patch('builtins.input', return_value='1')  # Mock user input for option 1 (scrape website)
    @patch('WebsiteCopier.fetch')  # Mock the fetch method to avoid real web requests
    @patch('WebsiteCopier.run')  # Mock the run method to avoid starting the server
    def test_scrape_website(self, mock_run, mock_fetch, mock_input):
        main.Banner()
        main.main_menu()
        mock_fetch.assert_called_once()  # Ensure fetch was called
        mock_run.assert_called_once()  # Ensure run was called

    @patch('builtins.input', return_value='2')  # Mock user input for option 2 (spoof login page)
    @patch('WebsiteSpoofer.ChangeHTML')  # Mock the ChangeHTML method
    @patch('WebsiteSpoofer.run')  # Mock the run method to avoid starting the server
    def test_spoof_login_page(self, mock_run, mock_change_html, mock_input):
        main.Banner()
        main.main_menu()
        mock_change_html.assert_called_once()  # Ensure ChangeHTML was called
        mock_run.assert_called_once()  # Ensure run was called

    @patch('builtins.input', return_value='3')  # Mock user input for option 3 (send phishing email)
    @patch('phishing_email.send_phishing_email')  # Mock send_phishing_email function to avoid sending emails
    def test_send_phishing_email(self, mock_send_email, mock_input):
        main.Banner()
        main.main_menu()

        # Simulate user input for sending phishing email
        with patch('builtins.input', side_effect=['sender@example.com', 'password', 'receiver@example.com', 'Phishing Alert', '<html>Phishing Content</html>', 'http://localhost:5000/track_click']):
            main.main_menu()
            mock_send_email.assert_called_once()  # Ensure the send_phishing_email function was called

    @patch('builtins.input', return_value='4')  # Mock user input for option 4 (go to tracking server)
    def test_tracking_server_option(self, mock_input):
        main.Banner()
        with patch('tracking_server.app.run') as mock_tracking_server:
            main.main_menu()
            mock_tracking_server.assert_called_once()  # Ensure tracking server was started

if __name__ == '__main__':
    unittest.main()