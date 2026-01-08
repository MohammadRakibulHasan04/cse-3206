"""
Unit tests for basic_operations module.
Demonstrates various testing techniques including:
- Normal cases
- Edge cases
- Error handling
- Multiple assertions
"""

import unittest
from basic_operations import add, subtract, multiply, divide


class TestBasicOperations(unittest.TestCase):
    """Test suite for basic arithmetic operations."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-10, 5), -5)
    
    def test_add_zero(self):
        """Test adding zero."""
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 5), 5)
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(5, 5), 0)
    
    def test_subtract_negative_numbers(self):
        """Test subtracting with negative numbers."""
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(5, -3), 8)
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(7, 5), 35)
    
    def test_multiply_negative_numbers(self):
        """Test multiplying with negative numbers."""
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(-2, -3), 6)
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 5), 0)
    
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(7, 2), 3.5)
    
    def test_divide_negative_numbers(self):
        """Test dividing with negative numbers."""
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(-10, -2), 5.0)
    
    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")
    
    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        self.assertEqual(divide(0, 5), 0.0)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
