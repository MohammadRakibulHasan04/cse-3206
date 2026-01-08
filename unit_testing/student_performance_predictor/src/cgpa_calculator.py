"""
Level 4: CGPA Calculator (Depends on calculator.py, sgpa_calculator.py)
Calculates Cumulative GPA across multiple semesters.
"""

from calculator import add, divide, multiply, add_all
from sgpa_calculator import calculate_sgpa, grade_to_points


def calculate_cgpa(semesters):
    """
    Calculate CGPA from multiple semesters.
    Each semester: {'sgpa': float, 'credits': int}
    """
    if not semesters:
        raise ValueError("No semesters provided")
    
    total_points = 0
    total_credits = 0
    
    for sem in semesters:
        weighted = multiply(sem['sgpa'], sem['credits'])
        total_points = add(total_points, weighted)
        total_credits = add(total_credits, sem['credits'])
    
    return round(divide(total_points, total_credits), 2)


def get_total_credits(semesters):
    """Get total credits completed."""
    return add_all([sem['credits'] for sem in semesters])


def get_completed_semesters(semesters):
    """Count completed semesters."""
    return len(semesters)


def is_on_track(cgpa, min_cgpa=2.0):
    """Check if student is on track (not on probation)."""
    return cgpa >= min_cgpa


def calculate_required_sgpa(current_cgpa, current_credits, target_cgpa, new_credits):
    """Calculate required SGPA in next semester to achieve target CGPA."""
    target_total = multiply(target_cgpa, add(current_credits, new_credits))
    current_total = multiply(current_cgpa, current_credits)
    required_points = divide(target_total - current_total, new_credits)
    return round(required_points, 2)
