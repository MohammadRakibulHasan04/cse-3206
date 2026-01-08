"""
Level 5: Performance Predictor (Depends on ALL previous modules)
Makes predictions and recommendations for students.
"""

from calculator import add, subtract, divide, multiply
from ct_calculator import calculate_ct_average
from sgpa_calculator import marks_to_grade, grade_to_points, GRADE_POINTS
from cgpa_calculator import calculate_cgpa, calculate_required_sgpa, is_on_track


# Academic standing thresholds
STANDINGS = {
    'DEANS_LIST': 3.75,
    'FIRST_CLASS': 3.50,
    'SECOND_CLASS': 3.00,
    'PASS': 2.00,
    'PROBATION': 0.00
}


def get_academic_standing(cgpa):
    """Determine academic standing based on CGPA."""
    if cgpa >= STANDINGS['DEANS_LIST']:
        return "Dean's List"
    if cgpa >= STANDINGS['FIRST_CLASS']:
        return "First Class"
    if cgpa >= STANDINGS['SECOND_CLASS']:
        return "Second Class"
    if cgpa >= STANDINGS['PASS']:
        return "Pass"
    return "Academic Probation"


def predict_graduation_cgpa(semesters, remaining_sems, expected_sgpa):
    """Predict final CGPA at graduation."""
    from cgpa_calculator import calculate_cgpa
    
    current_credits = sum(s['credits'] for s in semesters)
    current_cgpa = calculate_cgpa(semesters) if semesters else 0
    
    future_credits = multiply(remaining_sems, 15)  # Assume 15 credits/sem
    total_credits = add(current_credits, future_credits)
    
    current_total = multiply(current_cgpa, current_credits)
    future_total = multiply(expected_sgpa, future_credits)
    
    predicted = divide(add(current_total, future_total), total_credits)
    return round(predicted, 2)


def get_improvement_tips(cgpa, target_cgpa):
    """Generate tips to improve CGPA."""
    tips = []
    gap = subtract(target_cgpa, cgpa)
    
    if gap <= 0:
        tips.append("You've already achieved your target!")
    elif gap < 0.25:
        tips.append("Focus on attendance and CT marks.")
    elif gap < 0.5:
        tips.append("Aim for A- or above in all courses.")
    else:
        tips.append("Significant improvement needed.")
        tips.append("Consider retaking failed courses.")
    
    return tips


def calculate_required_marks(target_grade, ct_marks, attendance):
    """Calculate required final exam marks to achieve target grade."""
    ct_avg = calculate_ct_average(ct_marks)
    current = add(ct_avg, attendance)
    
    # Find minimum marks for target grade
    min_marks = {'A+': 80, 'A': 75, 'A-': 70, 'B+': 65, 'B': 60}
    target_total = min_marks.get(target_grade, 60)
    
    required = subtract(target_total, current)
    return max(0, min(70, required))  # Final exam is out of 70


def generate_report(semesters, target_cgpa=3.0):
    """Generate complete performance report."""
    cgpa = calculate_cgpa(semesters)
    standing = get_academic_standing(cgpa)
    on_track = is_on_track(cgpa)
    tips = get_improvement_tips(cgpa, target_cgpa)
    
    return {
        'cgpa': cgpa,
        'standing': standing,
        'on_track': on_track,
        'tips': tips
    }
