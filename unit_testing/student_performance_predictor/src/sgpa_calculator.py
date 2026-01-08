"""
Level 3: SGPA Calculator (Depends on calculator.py, ct_calculator.py)
Calculates Semester GPA from course grades.
"""

from calculator import add, divide, multiply, add_all
from ct_calculator import calculate_ct_average


# Grade point mapping
GRADE_POINTS = {
    'A+': 4.00, 'A': 3.75, 'A-': 3.50,
    'B+': 3.25, 'B': 3.00, 'B-': 2.75,
    'C+': 2.50, 'C': 2.25, 'C-': 2.00,
    'D': 1.75, 'F': 0.00
}


def marks_to_grade(marks):
    """Convert marks (0-100) to letter grade."""
    if marks >= 80: return 'A+'
    if marks >= 75: return 'A'
    if marks >= 70: return 'A-'
    if marks >= 65: return 'B+'
    if marks >= 60: return 'B'
    if marks >= 55: return 'B-'
    if marks >= 50: return 'C+'
    if marks >= 45: return 'C'
    if marks >= 40: return 'C-'
    if marks >= 35: return 'D'
    return 'F'


def grade_to_points(grade):
    """Convert letter grade to grade points."""
    if grade not in GRADE_POINTS:
        raise ValueError(f"Invalid grade: {grade}")
    return GRADE_POINTS[grade]


def calculate_course_marks(ct_marks, attendance, final_exam):
    """Calculate total course marks from components."""
    ct_avg = calculate_ct_average(ct_marks)  # Out of 20
    return add(add(ct_avg, attendance), final_exam)  # 20 + 10 + 70 = 100


def calculate_sgpa(courses):
    """
    Calculate SGPA from list of courses.
    Each course: {'credits': int, 'grade': str}
    """
    if not courses:
        raise ValueError("No courses provided")
    
    total_points = 0
    total_credits = 0
    
    for course in courses:
        points = grade_to_points(course['grade'])
        credits = course['credits']
        total_points = add(total_points, multiply(points, credits))
        total_credits = add(total_credits, credits)
    
    return round(divide(total_points, total_credits), 2)
