import unittest
import os
from unittest.mock import mock_open, patch

import file_parser as fp

class TestWriteFile(unittest.TestCase):
    def setUp(self):
        # Create any test files or data needed
        self.test_filename = "test_file.txt"
        self.test_data = ["Line 1\n", "Line 2\n", "Line 3\n"]

    def tearDown(self):
        # Clean up any test files
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    @patch('builtins.open', new_callable=mock_open)
    def test_successful_write(self, mock_file):
        # Test successful file write
        result = fp.write_file(self.test_filename, self.test_data)
        
        # Assert the function returns True on success
        self.assertTrue(result)
        
        # Verify open was called with correct parameters
        mock_file.assert_called_once_with(self.test_filename, 'w')
        
        # Verify writelines was called with correct data
        handle = mock_file()
        handle.writelines.assert_called_once_with(self.test_data)

    def test_write_to_invalid_path(self):
        # Test writing to an invalid file path
        invalid_filename = "/invalid/path/file.txt"
        result = fp.write_file(invalid_filename, self.test_data)
        
        # Assert the function returns False on failure
        self.assertFalse(result)

    def test_write_with_none_data(self):
        # Test writing None as data
        result = fp.write_file(self.test_filename, None)
        
        # Assert the function returns False when data is None
        self.assertFalse(result)

    def test_write_with_empty_data(self):
        # Test writing empty list
        result = fp.write_file(self.test_filename, [])
        
        # Assert the function returns True even with empty data
        self.assertTrue(result)

    # @patch('builtins.open')
    # def test_file_close_called(self, mock_file):
    #     # Test that file is properly closed
    #     mock_file_handle = mock_file.return_value
        
    #     fp.write_file(self.test_filename, self.test_data)
        
    #     # Verify close was called
    #     mock_file_handle.close.assert_called_once() 
    #     # mock_file_handle.close.assert_called_with()
    #     # mock_file_handle.close.assert_not_called()

if __name__ == '__main__':
    unittest.main()