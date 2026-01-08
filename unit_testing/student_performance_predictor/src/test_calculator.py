"""
Test Level 1: Basic Calculator Tests
No dependencies - tests arithmetic operations.
"""

import unittest

from calculator import add, subtract, multiply, divide, average, add_all


class TestAdd(unittest.TestCase):
    """Tests for add function."""
    
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)
    
    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)


class TestSubtract(unittest.TestCase):
    """Tests for subtract function."""
    
    def test_subtract_positive(self):
        self.assertEqual(subtract(10, 4), 6)
    
    def test_subtract_negative_result(self):
        self.assertEqual(subtract(3, 5), -2)


class TestMultiply(unittest.TestCase):
    """Tests for multiply function."""
    
    def test_multiply_positive(self):
        self.assertEqual(multiply(3, 4), 12)
    
    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)


class TestDivide(unittest.TestCase):
    """Tests for divide function."""
    
    def test_divide_positive(self):
        self.assertEqual(divide(10, 2), 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


class TestAverage(unittest.TestCase):
    """Tests for average function."""
    
    def test_average_normal(self):
        self.assertEqual(average([10, 20, 30]), 20)
    
    def test_average_empty_list(self):
        with self.assertRaises(ValueError):
            average([])


class TestAddAll(unittest.TestCase):
    """Tests for add_all function."""
    
    def test_add_all_normal(self):
        self.assertEqual(add_all([1, 2, 3, 4]), 10)
    
    def test_add_all_empty(self):
        self.assertEqual(add_all([]), 0)


if __name__ == '__main__':
    unittest.main()
