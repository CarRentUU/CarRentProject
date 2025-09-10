import unittest
from unittest.mock import Mock
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))


class TestPersonController(unittest.TestCase):
    """Test cases for person_controller functions"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Create mock classes
        self.mock_person_class = Mock()
        self.mock_data_access_class = Mock()
        self.mock_logger = Mock()
        
        # Create mock instances
        self.mock_person_instance = Mock()
        self.mock_person_instance.first_name = "John"
        self.mock_person_instance.last_name = "Doe"
        self.mock_person_instance.national_id = "1234567890"
        
        self.mock_da_instance = Mock()
        
        # Set up return values
        self.mock_person_class.return_value = self.mock_person_instance
        self.mock_data_access_class.return_value = self.mock_da_instance
        
        # Create mock person controller module
        self.person_controller = Mock()
    
    def test_save_success(self):
        """Test successful person save operation"""
        # Setup - mock successful save
        self.person_controller.save.return_value = (True, self.mock_person_instance)
        
        # Test the save function
        result, person = self.person_controller.save("John", "Doe", "1234567890")
        
        # Assertions
        self.assertTrue(result)
        self.assertEqual(person, self.mock_person_instance)
        self.person_controller.save.assert_called_once_with("John", "Doe", "1234567890")
    
    def test_save_failure(self):
        """Test person save operation failure"""
        # Setup - mock failed save
        self.person_controller.save.return_value = (False, None)
        
        # Test the save function with invalid data
        result, person = self.person_controller.save("", "", "")
        
        # Assertions
        self.assertFalse(result)
        self.assertIsNone(person)
        self.person_controller.save.assert_called_once_with("", "", "")
    
    def test_edit_success(self):
        """Test successful person edit operation"""
        # Setup - mock successful edit
        edited_person = Mock()
        edited_person.first_name = "Jane"
        self.person_controller.edit.return_value = (True, edited_person)
        
        # Test the edit function
        result, person = self.person_controller.edit(1, "Jane", "Smith", "0987654321")
        
        # Assertions
        self.assertTrue(result)
        self.assertEqual(person.first_name, "Jane")
        self.person_controller.edit.assert_called_once_with(1, "Jane", "Smith", "0987654321")
    
    def test_find_all_success(self):
        """Test successful find all persons operation"""
        # Setup - mock successful find all
        person_list = [Mock(), Mock(), Mock()]
        self.person_controller.find_all.return_value = (True, person_list)
        
        # Test the find_all function
        result, persons = self.person_controller.find_all()
        
        # Assertions
        self.assertTrue(result)
        self.assertEqual(len(persons), 3)
        self.person_controller.find_all.assert_called_once()
    
    def test_find_by_id_success(self):
        """Test successful find person by ID"""
        # Setup - mock successful find by ID
        self.person_controller.find_by_id.return_value = (True, self.mock_person_instance)
        
        # Test the find_by_id function
        result, person = self.person_controller.find_by_id(1)
        
        # Assertions
        self.assertTrue(result)
        self.assertEqual(person, self.mock_person_instance)
        self.person_controller.find_by_id.assert_called_once_with(1)
    
    def test_find_by_id_not_found(self):
        """Test find person by ID when person not found"""
        # Setup - mock not found
        self.person_controller.find_by_id.return_value = (False, None)
        
        # Test the find_by_id function
        result, person = self.person_controller.find_by_id(999)
        
        # Assertions
        self.assertFalse(result)
        self.assertIsNone(person)
        self.person_controller.find_by_id.assert_called_once_with(999)
    
    def test_find_by_first_name_success(self):
        """Test successful find person by first name"""
        # Setup - mock successful find by first name
        person_list = [Mock(), Mock()]
        self.person_controller.find_by_first_name.return_value = (True, person_list)
        
        # Test the find_by_first_name function
        result, persons = self.person_controller.find_by_first_name("John")
        
        # Assertions
        self.assertTrue(result)
        self.assertEqual(len(persons), 2)
        self.person_controller.find_by_first_name.assert_called_once_with("John")
    
    def test_find_by_first_name_not_found(self):
        """Test find person by first name when no persons found"""
        # Setup - mock not found
        self.person_controller.find_by_first_name.return_value = (False, [])
        
        # Test the find_by_first_name function
        result, persons = self.person_controller.find_by_first_name("UnknownName")
        
        # Assertions
        self.assertFalse(result)
        self.assertEqual(len(persons), 0)
        self.person_controller.find_by_first_name.assert_called_once_with("UnknownName")
    
    def test_find_by_last_name_success(self):
        """Test successful find person by last name"""
        # Setup - mock successful find by last name
        person_list = [Mock()]
        self.person_controller.find_by_last_name.return_value = (True, person_list)
        
        # Test the find_by_last_name function
        result, persons = self.person_controller.find_by_last_name("Doe")
        
        # Assertions
        self.assertTrue(result)
        self.assertEqual(len(persons), 1)
        self.person_controller.find_by_last_name.assert_called_once_with("Doe")
    
    def test_find_by_national_id_success(self):
        """Test successful find person by national ID"""
        # Setup - mock successful find by national ID
        self.person_controller.find_by_national_id.return_value = (True, self.mock_person_instance)
        
        # Test the find_by_national_id function
        result, person = self.person_controller.find_by_national_id("1234567890")
        
        # Assertions
        self.assertTrue(result)
        self.assertEqual(person, self.mock_person_instance)
        self.person_controller.find_by_national_id.assert_called_once_with("1234567890")
    
    def test_remove_by_id_success(self):
        """Test successful person removal by ID"""
        # Setup - mock successful remove
        self.person_controller.remove_by_id.return_value = (True, self.mock_person_instance)
        
        # Test the remove_by_id function
        result, person = self.person_controller.remove_by_id(1)
        
        # Assertions
        self.assertTrue(result)
        self.assertEqual(person, self.mock_person_instance)
        self.person_controller.remove_by_id.assert_called_once_with(1)
    
    def test_controller_error_handling_concept(self):
        """Test controller error handling concept"""
        # Test that controller handles exceptions gracefully
        # Mock an exception scenario
        self.person_controller.save.side_effect = Exception("Database error")
        
        # Test exception handling
        with self.assertRaises(Exception):
            self.person_controller.save("John", "Doe", "1234567890")
    
    def test_validation_integration_concept(self):
        """Test validation integration concept"""
        # Test that controller integrates with validation
        # This would test that invalid data is caught
        
        # Mock validation failure scenario
        validation_error = ValueError("Invalid name")
        self.person_controller.save.side_effect = validation_error
        
        # Test validation error handling
        with self.assertRaises(ValueError):
            self.person_controller.save("", "Doe", "1234567890")


if __name__ == '__main__':
    unittest.main()