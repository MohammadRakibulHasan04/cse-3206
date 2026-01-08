"""
Test Level 2: CT Calculator Tests
Depends on calculator.py - tests CT mark calculations.
"""

import unittest

from ct_calculator import (
    sort_marks, get_best_n, calculate_ct_average, validate_ct_marks
)


class TestSortMarks(unittest.TestCase):
    """Tests for sort_marks function."""
    
    def test_sort_descending(self):
        self.assertEqual(sort_marks([15, 18, 12, 20]), [20, 18, 15, 12])
    
    def test_sort_already_sorted(self):
        self.assertEqual(sort_marks([20, 18, 15]), [20, 18, 15])


class TestGetBestN(unittest.TestCase):
    """Tests for get_best_n function."""
    
    def test_get_best_3(self):
        self.assertEqual(get_best_n([15, 18, 12, 20], 3), [20, 18, 15])
    
    def test_get_best_2(self):
        self.assertEqual(get_best_n([10, 15, 8, 12], 2), [15, 12])
    
    def test_insufficient_marks(self):
        with self.assertRaises(ValueError):
            get_best_n([10, 15], 3)


class TestCalculateCTAverage(unittest.TestCase):
    """Tests for calculate_ct_average function."""
    
    def test_ct_average_normal(self):
        # Best 3: 18, 16, 15 → avg = 49/3 = 16.33
        result = calculate_ct_average([15, 18, 12, 16])
        self.assertAlmostEqual(result, 16.33, places=2)
    
    def test_ct_average_all_same(self):
        result = calculate_ct_average([15, 15, 15, 15])
        self.assertEqual(result, 15)
    
    def test_ct_not_four_marks(self):
        with self.assertRaises(ValueError):
            calculate_ct_average([15, 18, 12])


class TestValidateCTMarks(unittest.TestCase):
    """Tests for validate_ct_marks function."""
    
    def test_valid_marks(self):
        self.assertTrue(validate_ct_marks([15, 18, 12, 20]))
    
    def test_marks_too_high(self):
        with self.assertRaises(ValueError):
            validate_ct_marks([15, 25, 12, 18])
    
    def test_marks_negative(self):
        with self.assertRaises(ValueError):
            validate_ct_marks([15, -5, 12, 18])


if __name__ == '__main__':
    unittest.main()
