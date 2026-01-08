"""
Unit tests for calculator module.
Demonstrates testing functions that depend on other modules.
Shows integration testing concepts.
"""

import unittest
from calculator import power, average, percentage, sum_range


class TestCalculator(unittest.TestCase):
    """Test suite for calculator functions."""
    
    # Tests for power function
    def test_power_positive_numbers(self):
        """Test power with positive base and exponent."""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)
        self.assertEqual(power(3, 4), 81)
    
    def test_power_zero_exponent(self):
        """Test that any number to the power of 0 is 1."""
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(100, 0), 1)
        self.assertEqual(power(0, 0), 1)
    
    def test_power_one_exponent(self):
        """Test that any number to the power of 1 is itself."""
        self.assertEqual(power(7, 1), 7)
        self.assertEqual(power(42, 1), 42)
    
    def test_power_negative_exponent_raises_error(self):
        """Test that negative exponent raises ValueError."""
        with self.assertRaises(ValueError):
            power(2, -1)
    
    def test_power_non_integer_exponent_raises_error(self):
        """Test that non-integer exponent raises ValueError."""
        with self.assertRaises(ValueError):
            power(2, 2.5)
    
    # Tests for average function
    def test_average_positive_numbers(self):
        """Test average with positive numbers."""
        self.assertEqual(average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(average([10, 20, 30]), 20.0)
    
    def test_average_negative_numbers(self):
        """Test average with negative numbers."""
        self.assertEqual(average([-1, -2, -3]), -2.0)
        self.assertEqual(average([10, -10]), 0.0)
    
    def test_average_single_number(self):
        """Test average with a single number."""
        self.assertEqual(average([42]), 42.0)
    
    def test_average_empty_list_raises_error(self):
        """Test that empty list raises ValueError."""
        with self.assertRaises(ValueError) as context:
            average([])
        self.assertEqual(str(context.exception), "Cannot calculate average of empty list")
    
    def test_average_decimals(self):
        """Test average with decimal numbers."""
        self.assertAlmostEqual(average([1.5, 2.5, 3.5]), 2.5)
    
    # Tests for percentage function
    def test_percentage_basic(self):
        """Test basic percentage calculations."""
        self.assertEqual(percentage(25, 100), 25.0)
        self.assertEqual(percentage(1, 4), 25.0)
        self.assertEqual(percentage(50, 200), 25.0)
    
    def test_percentage_over_100(self):
        """Test percentage when part is greater than whole."""
        self.assertEqual(percentage(150, 100), 150.0)
    
    def test_percentage_zero_part(self):
        """Test percentage when part is zero."""
        self.assertEqual(percentage(0, 100), 0.0)
    
    def test_percentage_zero_whole_raises_error(self):
        """Test that zero whole raises ValueError."""
        with self.assertRaises(ValueError) as context:
            percentage(50, 0)
        self.assertEqual(str(context.exception), "Whole cannot be zero")
    
    # Tests for sum_range function
    def test_sum_range_positive(self):
        """Test sum_range with positive ranges."""
        self.assertEqual(sum_range(1, 5), 15)  # 1+2+3+4+5
        self.assertEqual(sum_range(1, 10), 55)
        self.assertEqual(sum_range(0, 4), 10)  # 0+1+2+3+4
    
    def test_sum_range_single_number(self):
        """Test sum_range when start equals end."""
        self.assertEqual(sum_range(5, 5), 5)
        self.assertEqual(sum_range(0, 0), 0)
    
    def test_sum_range_negative_numbers(self):
        """Test sum_range with negative numbers."""
        self.assertEqual(sum_range(-3, 3), 0)  # -3-2-1+0+1+2+3
        self.assertEqual(sum_range(-5, -1), -15)  # -5-4-3-2-1
    
    def test_sum_range_start_greater_than_end(self):
        """Test sum_range when start is greater than end."""
        self.assertEqual(sum_range(5, 1), 0)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
