"""
Student Performance Predictor - CLI Demo
Demonstrates all modules working together.
"""

from calculator import add, average
from ct_calculator import calculate_ct_average, validate_ct_marks
from sgpa_calculator import marks_to_grade, calculate_sgpa, calculate_course_marks
from cgpa_calculator import calculate_cgpa, calculate_required_sgpa
from predictor import get_academic_standing, generate_report, get_improvement_tips


def print_header(text):
    print("\n" + "=" * 50)
    print(f"  {text}")
    print("=" * 50)


def demo_calculator():
    print_header("Level 1: Basic Calculator")
    print(f"  5 + 3 = {add(5, 3)}")
    print(f"  Average of [85, 90, 78] = {average([85, 90, 78])}")


def demo_ct_calculator():
    print_header("Level 2: CT Calculator")
    ct_marks = [18, 15, 12, 16]
    print(f"  CT Marks: {ct_marks}")
    print(f"  Best 3 Average: {calculate_ct_average(ct_marks):.2f}/20")


def demo_sgpa_calculator():
    print_header("Level 3: SGPA Calculator")
    
    # Single course calculation
    ct_marks = [18, 16, 14, 15]
    attendance = 8
    final = 55
    total = calculate_course_marks(ct_marks, attendance, final)
    grade = marks_to_grade(total)
    
    print(f"  Course: CSE 3206")
    print(f"  CT Average: {calculate_ct_average(ct_marks):.2f}/20")
    print(f"  Attendance: {attendance}/10")
    print(f"  Final Exam: {final}/70")
    print(f"  Total: {total:.2f}/100 → Grade: {grade}")
    
    # SGPA
    courses = [
        {'credits': 3, 'grade': 'A'},
        {'credits': 3, 'grade': 'B+'},
        {'credits': 3, 'grade': 'A-'},
        {'credits': 2, 'grade': 'A'},
    ]
    print(f"\n  Semester Courses: {len(courses)}")
    print(f"  SGPA: {calculate_sgpa(courses)}")


def demo_cgpa_calculator():
    print_header("Level 4: CGPA Calculator")
    semesters = [
        {'sgpa': 3.65, 'credits': 15},
        {'sgpa': 3.42, 'credits': 15},
        {'sgpa': 3.58, 'credits': 18},
    ]
    
    for i, sem in enumerate(semesters, 1):
        print(f"  Semester {i}: SGPA={sem['sgpa']}, Credits={sem['credits']}")
    
    cgpa = calculate_cgpa(semesters)
    print(f"\n  Current CGPA: {cgpa}")


def demo_predictor():
    print_header("Level 5: Performance Predictor")
    semesters = [
        {'sgpa': 3.65, 'credits': 15},
        {'sgpa': 3.42, 'credits': 15},
        {'sgpa': 3.58, 'credits': 18},
    ]
    
    report = generate_report(semesters, target_cgpa=3.75)
    
    print(f"  CGPA: {report['cgpa']}")
    print(f"  Standing: {report['standing']}")
    print(f"  On Track: {'Yes' if report['on_track'] else 'No'}")
    print(f"\n  Tips:")
    for tip in report['tips']:
        print(f"    • {tip}")
    
    # Required SGPA
    current_cgpa = report['cgpa']
    current_credits = sum(s['credits'] for s in semesters)
    required = calculate_required_sgpa(current_cgpa, current_credits, 3.75, 15)
    print(f"\n  Required SGPA next semester for 3.75 CGPA: {required}")


def main():
    print("\n" + "🎓 STUDENT PERFORMANCE PREDICTOR 🎓".center(50))
    print("Unit Testing Demonstration Project".center(50))
    
    demo_calculator()
    demo_ct_calculator()
    demo_sgpa_calculator()
    demo_cgpa_calculator()
    demo_predictor()
    
    print("\n" + "=" * 50)
    print("  Demo Complete!")
    print("=" * 50 + "\n")


if __name__ == '__main__':
    main()
