"""
Test Level 4: CGPA Calculator Tests
Depends on calculator.py, sgpa_calculator.py - tests CGPA calculations.
"""

import unittest

from cgpa_calculator import (
    calculate_cgpa, get_total_credits, get_completed_semesters,
    is_on_track, calculate_required_sgpa
)


class TestCalculateCGPA(unittest.TestCase):
    """Tests for calculate_cgpa function."""
    
    def test_cgpa_single_semester(self):
        semesters = [{'sgpa': 3.5, 'credits': 15}]
        self.assertEqual(calculate_cgpa(semesters), 3.5)
    
    def test_cgpa_multiple_semesters(self):
        semesters = [
            {'sgpa': 3.5, 'credits': 15},  # 52.5
            {'sgpa': 3.0, 'credits': 15},  # 45.0
        ]
        # Total: 97.5 / 30 = 3.25
        self.assertEqual(calculate_cgpa(semesters), 3.25)
    
    def test_cgpa_empty_semesters(self):
        with self.assertRaises(ValueError):
            calculate_cgpa([])


class TestGetTotalCredits(unittest.TestCase):
    """Tests for get_total_credits function."""
    
    def test_total_credits(self):
        semesters = [
            {'sgpa': 3.5, 'credits': 15},
            {'sgpa': 3.0, 'credits': 18},
        ]
        self.assertEqual(get_total_credits(semesters), 33)


class TestGetCompletedSemesters(unittest.TestCase):
    """Tests for get_completed_semesters function."""
    
    def test_completed_count(self):
        semesters = [{'sgpa': 3.5, 'credits': 15}] * 4
        self.assertEqual(get_completed_semesters(semesters), 4)


class TestIsOnTrack(unittest.TestCase):
    """Tests for is_on_track function."""
    
    def test_on_track(self):
        self.assertTrue(is_on_track(2.5))
    
    def test_not_on_track(self):
        self.assertFalse(is_on_track(1.8))
    
    def test_exactly_minimum(self):
        self.assertTrue(is_on_track(2.0))


class TestCalculateRequiredSGPA(unittest.TestCase):
    """Tests for calculate_required_sgpa function."""
    
    def test_required_sgpa_normal(self):
        # Current: 3.0 with 30 credits, target: 3.25 with 15 new credits
        # (3.25 * 45) - (3.0 * 30) = 146.25 - 90 = 56.25
        # 56.25 / 15 = 3.75
        result = calculate_required_sgpa(3.0, 30, 3.25, 15)
        self.assertEqual(result, 3.75)
    
    def test_required_sgpa_maintain(self):
        result = calculate_required_sgpa(3.5, 30, 3.5, 15)
        self.assertEqual(result, 3.5)


if __name__ == '__main__':
    unittest.main()
