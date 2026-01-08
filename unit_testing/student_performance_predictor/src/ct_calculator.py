"""
Level 2: CT Calculator (Depends on calculator.py)
Calculates best 3 out of 4 CT marks.
"""

from calculator import add, divide, average


def sort_marks(marks):
    """Sort marks in descending order."""
    return sorted(marks, reverse=True)


def get_best_n(marks, n=3):
    """Get best n marks from a list."""
    if len(marks) < n:
        raise ValueError(f"Need at least {n} marks")
    sorted_marks = sort_marks(marks)
    return sorted_marks[:n]


def calculate_ct_average(ct_marks):
    """Calculate average of best 3 out of 4 CTs."""
    if len(ct_marks) != 4:
        raise ValueError("Exactly 4 CT marks required")
    best_3 = get_best_n(ct_marks, 3)
    return average(best_3)


def validate_ct_marks(marks):
    """Validate CT marks are within 0-20 range."""
    for mark in marks:
        if mark < 0 or mark > 20:
            raise ValueError("CT marks must be between 0-20")
    return True
