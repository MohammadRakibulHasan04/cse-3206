"""
Unit tests for statistics module.
Demonstrates testing complex functions that depend on multiple modules.
Shows advanced testing concepts including float comparisons.
"""

import unittest
from statistics import mean, variance, standard_deviation, median, range_stat, coefficient_of_variation


class TestStatistics(unittest.TestCase):
    """Test suite for statistical functions."""
    
    # Tests for mean function
    def test_mean_positive_numbers(self):
        """Test mean with positive numbers."""
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(mean([10, 20, 30]), 20.0)
    
    def test_mean_negative_numbers(self):
        """Test mean with negative numbers."""
        self.assertEqual(mean([-1, -2, -3]), -2.0)
    
    def test_mean_mixed_numbers(self):
        """Test mean with mixed positive and negative numbers."""
        self.assertEqual(mean([-10, 10]), 0.0)
    
    def test_mean_empty_list_raises_error(self):
        """Test that empty list raises ValueError."""
        with self.assertRaises(ValueError):
            mean([])
    
    # Tests for variance function
    def test_variance_simple(self):
        """Test variance with simple dataset."""
        self.assertEqual(variance([1, 2, 3, 4, 5]), 2.0)
    
    def test_variance_all_same(self):
        """Test variance when all numbers are the same."""
        self.assertEqual(variance([5, 5, 5, 5]), 0.0)
    
    def test_variance_two_numbers(self):
        """Test variance with two numbers."""
        self.assertEqual(variance([1, 3]), 1.0)
    
    def test_variance_empty_list_raises_error(self):
        """Test that empty list raises ValueError."""
        with self.assertRaises(ValueError):
            variance([])
    
    # Tests for standard_deviation function
    def test_standard_deviation_simple(self):
        """Test standard deviation with simple dataset."""
        result = standard_deviation([1, 2, 3, 4, 5])
        self.assertAlmostEqual(result, 1.4142135623730951, places=10)
    
    def test_standard_deviation_all_same(self):
        """Test standard deviation when all numbers are the same."""
        self.assertEqual(standard_deviation([7, 7, 7]), 0.0)
    
    def test_standard_deviation_large_spread(self):
        """Test standard deviation with large spread."""
        result = standard_deviation([0, 10, 20, 30, 40])
        self.assertAlmostEqual(result, 14.142135623730951, places=10)
    
    def test_standard_deviation_empty_list_raises_error(self):
        """Test that empty list raises ValueError."""
        with self.assertRaises(ValueError):
            standard_deviation([])
    
    # Tests for median function
    def test_median_odd_length(self):
        """Test median with odd number of elements."""
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(median([10, 20, 30]), 20)
    
    def test_median_even_length(self):
        """Test median with even number of elements."""
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        self.assertEqual(median([10, 20]), 15.0)
    
    def test_median_unsorted(self):
        """Test median with unsorted data."""
        self.assertEqual(median([3, 1, 4, 1, 5]), 3)
        self.assertEqual(median([8, 3, 5, 2]), 4.0)
    
    def test_median_single_element(self):
        """Test median with single element."""
        self.assertEqual(median([42]), 42)
    
    def test_median_empty_list_raises_error(self):
        """Test that empty list raises ValueError."""
        with self.assertRaises(ValueError):
            median([])
    
    def test_median_negative_numbers(self):
        """Test median with negative numbers."""
        self.assertEqual(median([-5, -1, 0, 1, 5]), 0)
    
    # Tests for range_stat function
    def test_range_stat_positive(self):
        """Test range with positive numbers."""
        self.assertEqual(range_stat([1, 2, 3, 4, 5]), 4)
        self.assertEqual(range_stat([10, 50, 30]), 40)
    
    def test_range_stat_negative(self):
        """Test range with negative numbers."""
        self.assertEqual(range_stat([-10, -5, -1]), 9)
    
    def test_range_stat_mixed(self):
        """Test range with mixed positive and negative numbers."""
        self.assertEqual(range_stat([-5, 0, 5]), 10)
    
    def test_range_stat_single_element(self):
        """Test range with single element."""
        self.assertEqual(range_stat([42]), 0)
    
    def test_range_stat_all_same(self):
        """Test range when all numbers are the same."""
        self.assertEqual(range_stat([5, 5, 5]), 0)
    
    def test_range_stat_empty_list_raises_error(self):
        """Test that empty list raises ValueError."""
        with self.assertRaises(ValueError):
            range_stat([])
    
    # Tests for coefficient_of_variation function
    def test_coefficient_of_variation_normal(self):
        """Test coefficient of variation with normal data."""
        result = coefficient_of_variation([2, 4, 6, 8])
        self.assertAlmostEqual(result, 44.721359549995796, places=5)
    
    def test_coefficient_of_variation_low_variation(self):
        """Test CV with low variation."""
        result = coefficient_of_variation([99, 100, 101])
        self.assertAlmostEqual(result, 0.8164965809277263, places=5)
    
    def test_coefficient_of_variation_empty_list_raises_error(self):
        """Test that empty list raises ValueError."""
        with self.assertRaises(ValueError):
            coefficient_of_variation([])
    
    def test_coefficient_of_variation_zero_mean_raises_error(self):
        """Test that zero mean raises ValueError."""
        with self.assertRaises(ValueError) as context:
            coefficient_of_variation([-1, 0, 1])
        self.assertEqual(str(context.exception), "Cannot calculate CV when mean is zero")


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
