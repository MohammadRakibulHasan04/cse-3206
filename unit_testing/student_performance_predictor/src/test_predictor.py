"""
Test Level 5: Predictor Tests
Depends on ALL modules - tests predictions and recommendations.
"""

import unittest

from predictor import (
    get_academic_standing, predict_graduation_cgpa,
    get_improvement_tips, calculate_required_marks, generate_report
)


class TestGetAcademicStanding(unittest.TestCase):
    """Tests for get_academic_standing function."""
    
    def test_deans_list(self):
        self.assertEqual(get_academic_standing(3.85), "Dean's List")
    
    def test_first_class(self):
        self.assertEqual(get_academic_standing(3.55), "First Class")
    
    def test_second_class(self):
        self.assertEqual(get_academic_standing(3.2), "Second Class")
    
    def test_pass(self):
        self.assertEqual(get_academic_standing(2.5), "Pass")
    
    def test_probation(self):
        self.assertEqual(get_academic_standing(1.8), "Academic Probation")


class TestPredictGraduationCGPA(unittest.TestCase):
    """Tests for predict_graduation_cgpa function."""
    
    def test_predict_with_history(self):
        semesters = [
            {'sgpa': 3.5, 'credits': 15},
            {'sgpa': 3.0, 'credits': 15}
        ]
        result = predict_graduation_cgpa(semesters, 2, 3.5)
        self.assertIsInstance(result, float)
    
    def test_predict_no_history(self):
        result = predict_graduation_cgpa([], 8, 3.5)
        self.assertEqual(result, 3.5)


class TestGetImprovementTips(unittest.TestCase):
    """Tests for get_improvement_tips function."""
    
    def test_already_achieved(self):
        tips = get_improvement_tips(3.5, 3.0)
        self.assertIn("You've already achieved your target!", tips)
    
    def test_small_gap(self):
        tips = get_improvement_tips(2.9, 3.0)
        self.assertTrue(len(tips) > 0)
    
    def test_large_gap(self):
        tips = get_improvement_tips(2.0, 3.0)
        self.assertTrue(len(tips) >= 2)


class TestCalculateRequiredMarks(unittest.TestCase):
    """Tests for calculate_required_marks function."""
    
    def test_required_for_a_plus(self):
        ct_marks = [18, 16, 15, 14]  # avg ~16.33
        attendance = 8
        result = calculate_required_marks('A+', ct_marks, attendance)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 70)


class TestGenerateReport(unittest.TestCase):
    """Tests for generate_report function."""
    
    def test_report_structure(self):
        semesters = [
            {'sgpa': 3.5, 'credits': 15},
            {'sgpa': 3.2, 'credits': 15}
        ]
        report = generate_report(semesters)
        
        self.assertIn('cgpa', report)
        self.assertIn('standing', report)
        self.assertIn('on_track', report)
        self.assertIn('tips', report)
    
    def test_report_values(self):
        semesters = [{'sgpa': 3.8, 'credits': 15}]
        report = generate_report(semesters, target_cgpa=3.5)
        
        self.assertEqual(report['cgpa'], 3.8)
        self.assertTrue(report['on_track'])


if __name__ == '__main__':
    unittest.main()
