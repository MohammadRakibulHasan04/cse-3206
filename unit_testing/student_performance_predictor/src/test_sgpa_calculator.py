"""
Test Level 3: SGPA Calculator Tests
Depends on calculator.py, ct_calculator.py - tests SGPA calculations.
"""

import unittest

from sgpa_calculator import (
    marks_to_grade, grade_to_points, calculate_course_marks, calculate_sgpa
)


class TestMarksToGrade(unittest.TestCase):
    """Tests for marks_to_grade function."""
    
    def test_grade_a_plus(self):
        self.assertEqual(marks_to_grade(85), 'A+')
    
    def test_grade_a(self):
        self.assertEqual(marks_to_grade(77), 'A')
    
    def test_grade_b(self):
        self.assertEqual(marks_to_grade(62), 'B')
    
    def test_grade_f(self):
        self.assertEqual(marks_to_grade(30), 'F')
    
    def test_grade_boundary(self):
        self.assertEqual(marks_to_grade(80), 'A+')
        self.assertEqual(marks_to_grade(79), 'A')


class TestGradeToPoints(unittest.TestCase):
    """Tests for grade_to_points function."""
    
    def test_a_plus(self):
        self.assertEqual(grade_to_points('A+'), 4.0)
    
    def test_b(self):
        self.assertEqual(grade_to_points('B'), 3.0)
    
    def test_f(self):
        self.assertEqual(grade_to_points('F'), 0.0)
    
    def test_invalid_grade(self):
        with self.assertRaises(ValueError):
            grade_to_points('X')


class TestCalculateCourseMarks(unittest.TestCase):
    """Tests for calculate_course_marks function."""
    
    def test_course_marks_normal(self):
        ct_marks = [18, 16, 15, 14]  # Best 3 avg = 16.33
        attendance = 8
        final_exam = 55
        result = calculate_course_marks(ct_marks, attendance, final_exam)
        self.assertAlmostEqual(result, 79.33, places=2)


class TestCalculateSGPA(unittest.TestCase):
    """Tests for calculate_sgpa function."""
    
    def test_sgpa_single_course(self):
        courses = [{'credits': 3, 'grade': 'A+'}]
        self.assertEqual(calculate_sgpa(courses), 4.0)
    
    def test_sgpa_multiple_courses(self):
        courses = [
            {'credits': 3, 'grade': 'A+'},  # 4.0 * 3 = 12
            {'credits': 3, 'grade': 'B'},   # 3.0 * 3 = 9
        ]
        # Total: 21 / 6 = 3.5
        self.assertEqual(calculate_sgpa(courses), 3.5)
    
    def test_sgpa_empty_courses(self):
        with self.assertRaises(ValueError):
            calculate_sgpa([])


if __name__ == '__main__':
    unittest.main()
