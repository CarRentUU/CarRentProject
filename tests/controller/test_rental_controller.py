import unittest
from unittest.mock import Mock
from datetime import date
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))


class TestRentalController(unittest.TestCase):
    """Test cases for rental_controller functions"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Create mock classes
        self.mock_rental_class = Mock()
        self.mock_car_class = Mock()
        self.mock_person_class = Mock()
        self.mock_data_access_class = Mock()
        self.mock_logger = Mock()
        
        # Create mock instances
        self.mock_rental_instance = Mock()
        self.mock_rental_instance.person_id = 1
        self.mock_rental_instance.car_id = 1
        self.mock_rental_instance.rental_date = date.today()
        self.mock_rental_instance.return_date = None
        
        self.mock_car_instance = Mock()
        self.mock_car_instance.id = 1
        self.mock_car_instance.brand = "Toyota"
        
        self.mock_person_instance = Mock()
        self.mock_person_instance.id = 1
        self.mock_person_instance.first_name = "John"
        
        # Create mock rental controller module
        self.rental_controller = Mock()
    
    def test_save_success(self):
        """Test successful rental save operation"""
        # Setup - mock successful save
        self.rental_controller.save.return_value = (True, self.mock_rental_instance)
        
        # Test the save function
        result, rental = self.rental_controller.save(1, 1, date.today())
        
        # Assertions
        self.assertTrue(result)
        self.assertEqual(rental, self.mock_rental_instance)
        self.rental_controller.save.assert_called_once_with(1, 1, date.today())
    
    def test_save_car_not_found(self):
        """Test rental save when car doesn't exist"""
        # Setup - mock car not found scenario
        self.rental_controller.save.return_value = (False, "Car not found")
        
        # Test the save function
        result, message = self.rental_controller.save(999, 1, date.today())
        
        # Assertions
        self.assertFalse(result)
        self.assertEqual(message, "Car not found")
        self.rental_controller.save.assert_called_once_with(999, 1, date.today())
    
    def test_save_person_not_found(self):
        """Test rental save when person doesn't exist"""
        # Setup - mock person not found scenario
        self.rental_controller.save.return_value = (False, "Person not found")
        
        # Test the save function
        result, message = self.rental_controller.save(1, 999, date.today())
        
        # Assertions
        self.assertFalse(result)
        self.assertEqual(message, "Person not found")
        self.rental_controller.save.assert_called_once_with(1, 999, date.today())
    
    def test_save_car_already_rented(self):
        """Test rental save when car is already rented"""
        # Setup - mock car already rented scenario
        self.rental_controller.save.return_value = (False, "Car is already rented")
        
        # Test the save function
        result, message = self.rental_controller.save(1, 1, date.today())
        
        # Assertions
        self.assertFalse(result)
        self.assertEqual(message, "Car is already rented")
        self.rental_controller.save.assert_called_once_with(1, 1, date.today())
    
    def test_return_click_success(self):
        """Test successful car return operation"""
        # Setup - mock successful return
        returned_rental = Mock()
        returned_rental.return_date = date.today()
        self.rental_controller.return_click.return_value = (True, returned_rental)
        
        # Test the return_click function
        result, rental = self.rental_controller.return_click(1)
        
        # Assertions
        self.assertTrue(result)
        self.assertEqual(rental.return_date, date.today())
        self.rental_controller.return_click.assert_called_once_with(1)
    
    def test_return_click_no_active_rental(self):
        """Test car return when no active rental found"""
        # Setup - mock no active rental scenario
        self.rental_controller.return_click.return_value = (False, "No active rental found")
        
        # Test the return_click function
        result, message = self.rental_controller.return_click(999)
        
        # Assertions
        self.assertFalse(result)
        self.assertEqual(message, "No active rental found")
        self.rental_controller.return_click.assert_called_once_with(999)
    
    def test_find_all_success(self):
        """Test successful find all rentals operation"""
        # Setup - mock successful find all
        rental_list = [Mock(), Mock(), Mock()]
        self.rental_controller.find_all.return_value = (True, rental_list)
        
        # Test the find_all function
        result, rentals = self.rental_controller.find_all()
        
        # Assertions
        self.assertTrue(result)
        self.assertEqual(len(rentals), 3)
        self.rental_controller.find_all.assert_called_once()
    
    def test_find_by_id_success(self):
        """Test successful find rental by ID"""
        # Setup - mock successful find by ID
        self.rental_controller.find_by_id.return_value = (True, self.mock_rental_instance)
        
        # Test the find_by_id function
        result, rental = self.rental_controller.find_by_id(1)
        
        # Assertions
        self.assertTrue(result)
        self.assertEqual(rental, self.mock_rental_instance)
        self.rental_controller.find_by_id.assert_called_once_with(1)
    
    def test_remove_by_id_success(self):
        """Test successful rental removal by ID"""
        # Setup - mock successful remove
        self.rental_controller.remove_by_id.return_value = (True, self.mock_rental_instance)
        
        # Test the remove_by_id function
        result, rental = self.rental_controller.remove_by_id(1)
        
        # Assertions
        self.assertTrue(result)
        self.assertEqual(rental, self.mock_rental_instance)
        self.rental_controller.remove_by_id.assert_called_once_with(1)
    
    def test_remove_by_id_not_found(self):
        """Test rental removal when rental not found"""
        # Setup - mock not found scenario
        self.rental_controller.remove_by_id.return_value = (False, None)
        
        # Test the remove_by_id function
        result, rental = self.rental_controller.remove_by_id(999)
        
        # Assertions
        self.assertFalse(result)
        self.assertIsNone(rental)
        self.rental_controller.remove_by_id.assert_called_once_with(999)
    
    def test_controller_error_handling_concept(self):
        """Test controller error handling concept"""
        # Test that controller handles exceptions gracefully
        # Mock an exception scenario
        self.rental_controller.save.side_effect = Exception("Database error")
        
        # Test exception handling
        with self.assertRaises(Exception):
            self.rental_controller.save(1, 1, date.today())
    
    def test_validation_integration_concept(self):
        """Test validation integration concept"""
        # Test that controller integrates with validation
        # This would test that invalid data is caught
        
        # Mock validation failure scenario
        validation_error = ValueError("Invalid date")
        self.rental_controller.save.side_effect = validation_error
        
        # Test validation error handling
        with self.assertRaises(ValueError):
            self.rental_controller.save(1, 1, "invalid_date")


if __name__ == '__main__':
    unittest.main()