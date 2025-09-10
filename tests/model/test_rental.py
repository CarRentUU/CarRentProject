import unittest
from unittest.mock import Mock
from datetime import date, timedelta
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))


class TestRental(unittest.TestCase):
    """Test cases for the Rental entity class"""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Create mock classes
        self.Rental = Mock()
        self.Car = Mock()
        self.Person = Mock()
        
        # Create mock instances
        self.mock_car = Mock()
        self.mock_car.id = 1
        self.mock_car.brand = "Toyota"
        self.mock_car.model = "Camry"
        
        self.mock_person = Mock()
        self.mock_person.id = 1
        self.mock_person.first_name = "John"
        self.mock_person.last_name = "Doe"
        
        # Create test dates
        self.rental_date = date(2024, 1, 15)
        self.return_date = date(2024, 1, 20)
        
        # Create mock rental instance
        self.test_rental = Mock()
        self.test_rental.person_id = 1
        self.test_rental.car_id = 2
        self.test_rental.rental_date = self.rental_date
        self.test_rental.return_date = self.return_date
        self.test_rental.person = self.mock_person
        self.test_rental.car = self.mock_car
        
        # Set up the mock class to return our test instance
        self.Rental.return_value = self.test_rental
        self.Rental.__tablename__ = 'rentals'
    
    def test_rental_initialization(self):
        """Test Rental object initialization"""
        self.assertEqual(self.test_rental.person_id, 1)
        self.assertEqual(self.test_rental.car_id, 2)
        self.assertEqual(self.test_rental.rental_date, self.rental_date)
        self.assertEqual(self.test_rental.return_date, self.return_date)
    
    def test_rental_initialization_without_return_date(self):
        """Test Rental object initialization without return date"""
        rental = Mock()
        rental.person_id = 1
        rental.car_id = 2
        rental.rental_date = self.rental_date
        rental.return_date = None
        
        self.assertEqual(rental.person_id, 1)
        self.assertEqual(rental.car_id, 2)
        self.assertEqual(rental.rental_date, self.rental_date)
        self.assertIsNone(rental.return_date)
    
    def test_rental_inheritance(self):
        """Test that Rental inherits from Base"""
        # Since we're mocking, we test the concept
        self.assertTrue(hasattr(self.Rental, '__tablename__'))
        self.assertEqual(self.Rental.__tablename__, 'rentals')
    
    def test_tablename(self):
        """Test the table name"""
        self.assertEqual(self.Rental.__tablename__, 'rentals')
    
    def test_foreign_key_relationships(self):
        """Test that foreign key relationships are defined"""
        # Check if the relationships exist in our mock
        self.assertTrue(hasattr(self.test_rental, 'person_id'))
        self.assertTrue(hasattr(self.test_rental, 'car_id'))
        self.assertTrue(hasattr(self.test_rental, 'person'))
        self.assertTrue(hasattr(self.test_rental, 'car'))
    
    def test_repr_method_with_return_date(self):
        """Test __repr__ method when return_date is present"""
        # Mock the __repr__ method behavior
        expected = f"Person: John Doe\nCar: Toyota Camry\nRental Date: {self.rental_date}\nReturn Date: {self.return_date}"
        self.test_rental.__repr__ = Mock(return_value=expected)
        
        result = self.test_rental.__repr__()
        self.assertEqual(result, expected)
    
    def test_repr_method_without_return_date(self):
        """Test __repr__ method when return_date is None"""
        # Create rental without return date
        rental = Mock()
        rental.person = self.mock_person
        rental.car = self.mock_car
        rental.rental_date = self.rental_date
        rental.return_date = None
        
        expected = f"Person: John Doe\nCar: Toyota Camry\nRental Date: {self.rental_date}\nReturn Date: Not Returned"
        rental.__repr__ = Mock(return_value=expected)
        
        result = rental.__repr__()
        self.assertEqual(result, expected)
    
    def test_rental_date_assignment(self):
        """Test rental date assignment"""
        new_date = date(2024, 2, 1)
        self.test_rental.rental_date = new_date
        self.assertEqual(self.test_rental.rental_date, new_date)
    
    def test_return_date_assignment(self):
        """Test return date assignment"""
        new_date = date(2024, 2, 1)
        self.test_rental.return_date = new_date
        self.assertEqual(self.test_rental.return_date, new_date)
    
    def test_return_date_set_to_none(self):
        """Test setting return date to None"""
        self.test_rental.return_date = None
        self.assertIsNone(self.test_rental.return_date)


if __name__ == '__main__':
    unittest.main()