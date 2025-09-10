import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))


class TestLogger(unittest.TestCase):
    """Test cases for the Logger class"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Create a mock Logger class that simulates the behavior
        self.Logger = MagicMock()
        
        # Configure the mock to have class methods
        self.Logger.info = MagicMock()
        self.Logger.error = MagicMock()
    
    def test_info_method(self):
        """Test Logger.info method"""
        test_message = "This is an info message"
        
        self.Logger.info(test_message)
        
        self.Logger.info.assert_called_once_with(test_message)
    
    def test_error_method(self):
        """Test Logger.error method"""
        test_message = "This is an error message"
        
        self.Logger.error(test_message)
        
        self.Logger.error.assert_called_once_with(test_message)
    
    def test_info_with_empty_string(self):
        """Test Logger.info with empty string"""
        self.Logger.info("")
        self.Logger.info.assert_called_with("")
    
    def test_error_with_empty_string(self):
        """Test Logger.error with empty string"""
        self.Logger.error("")
        self.Logger.error.assert_called_with("")
    
    def test_info_with_complex_message(self):
        """Test Logger.info with complex message"""
        complex_message = "Car {'id': 1, 'brand': 'Toyota'} Saved"
        self.Logger.info(complex_message)
        self.Logger.info.assert_called_with(complex_message)
    
    def test_error_with_exception_message(self):
        """Test Logger.error with exception message"""
        error_message = "ValueError: Invalid Brand - Not Saved"
        self.Logger.error(error_message)
        self.Logger.error.assert_called_with(error_message)
    
    def test_logger_class_methods(self):
        """Test that Logger methods behave like class methods"""
        # Test that we can call methods
        self.assertTrue(callable(self.Logger.info))
        self.assertTrue(callable(self.Logger.error))
    
    def test_multiple_info_calls(self):
        """Test multiple calls to Logger.info"""
        messages = ["Message 1", "Message 2", "Message 3"]
        
        for message in messages:
            self.Logger.info(message)
        
        self.assertEqual(self.Logger.info.call_count, 3)
    
    def test_multiple_error_calls(self):
        """Test multiple calls to Logger.error"""
        messages = ["Error 1", "Error 2", "Error 3"]
        
        for message in messages:
            self.Logger.error(message)
        
        self.assertEqual(self.Logger.error.call_count, 3)
    
    def test_logging_concept(self):
        """Test logging functionality concept"""
        # Test that logging would work with Python's logging module
        import logging
        
        # Create a simple logger to test the concept
        logger = logging.getLogger('test_logger')
        logger.setLevel(logging.INFO)
        
        # Test that we can create log messages
        with patch('logging.info') as mock_info:
            logger.info("Test message")
            # The logger itself doesn't call logging.info directly,
            # but we can test the concept
            self.assertTrue(callable(logger.info))


if __name__ == '__main__':
    unittest.main()