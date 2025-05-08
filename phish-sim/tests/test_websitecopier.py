import unittest
from unittest.mock import patch, mock_open
from websitecopier import fetch_url, changefile, app
import os
import requests

class TestWebsiteCopier(unittest.TestCase):
    
    @patch('websitecopier.requests.get')  # Mock the requests.get method to avoid actual HTTP calls
    def test_fetch_url(self, mock_get):
        """Test the fetch_url function."""
        # Define mock HTML content to be returned by the mock request
        mock_html = "<html><body><h1>Test</h1></body></html>"
        mock_response = mock_get.return_value
        mock_response.text = mock_html
        
        # Call the fetch_url function with a test URL
        test_url = "http://example.com"
        fetch_url(test_url)
        
        # Check if the file was written with the correct content
        with open('example.html', 'r', encoding='utf-8') as file:
            content = file.read()
        
        self.assertIn('<html><body><h1>Test</h1></body></html>', content)
        self.assertTrue(os.path.exists('example.html'))  # Ensure the file exists

    @patch('websitecopier.os.path.exists')  # Mock os.path.exists to control file existence check
    def test_changefile(self, mock_exists):
        """Test the changefile function."""
        # Mock os.path.exists to return True as if the file exists
        mock_exists.return_value = True
        
        # Call the changefile function with a test file path
        test_file = "new_example.html"
        changefile(test_file)
        
        # Check if the file path has been updated
        global file  # Access the global 'file' variable
        self.assertEqual(file, test_file)

    @patch('websitecopier.send_file')  # Mock send_file to avoid serving the actual file during tests
    def test_display(self, mock_send_file):
        """Test the Flask route that displays the file."""
        # Simulate a GET request to the "/" route
        with app.test_client() as client:
            client.get('/')  # Make a request to the root route
            
            # Check that the send_file function was called with the correct file
            mock_send_file.assert_called_with(file)
    
    @patch('websitecopier.os.path.exists')  # Mock os.path.exists for file checking
    def test_file_does_not_exist_in_changefile(self, mock_exists):
        """Test the changefile function when the file does not exist."""
        # Mock os.path.exists to return False, simulating the file not existing
        mock_exists.return_value = False
        
        # Call the changefile function with a test file path
        test_file = "non_existent_file.html"
        changefile(test_file)
        
        # Ensure the file path hasn't changed since the file doesn't exist
        global file  # Access the global 'file' variable
        self.assertNotEqual(file, test_file)  # The file should remain unchanged
        
    def tearDown(self):
        """Clean up any files or resources after tests."""
        if os.path.exists('example.html'):
            os.remove('example.html')  # Clean up the test file

if __name__ == '__main__':
    unittest.main()
