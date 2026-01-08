"""
Main demonstration file showing the 3-level module structure.
This file demonstrates how each module builds on top of the previous one.
"""

# Level 1: Basic Operations
from basic_operations import add, subtract, multiply, divide

# Level 2: Calculator (uses Level 1)
from calculator import power, average, percentage, sum_range

# Level 3: Statistics (uses Level 2 and Level 1)
from statistics import mean, variance, standard_deviation, median, range_stat, coefficient_of_variation


def print_section(title):
    """Helper function to print section headers."""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)


def demonstrate_basic_operations():
    """Demonstrate Level 1: Basic Operations."""
    print_section("LEVEL 1: BASIC OPERATIONS")
    
    print(f"Addition: 15 + 7 = {add(15, 7)}")
    print(f"Subtraction: 15 - 7 = {subtract(15, 7)}")
    print(f"Multiplication: 15 * 7 = {multiply(15, 7)}")
    print(f"Division: 15 / 7 = {divide(15, 7):.2f}")
    
    # Demonstrate error handling
    print("\nError Handling:")
    try:
        divide(10, 0)
    except ValueError as e:
        print(f"  Attempting to divide by zero: {e}")


def demonstrate_calculator():
    """Demonstrate Level 2: Calculator (uses Basic Operations)."""
    print_section("LEVEL 2: CALCULATOR (builds on Level 1)")
    
    print(f"Power: 2^8 = {power(2, 8)}")
    print(f"Average of [10, 20, 30, 40, 50] = {average([10, 20, 30, 40, 50])}")
    print(f"Percentage: 75 out of 300 = {percentage(75, 300)}%")
    print(f"Sum of range 1 to 100 = {sum_range(1, 100)}")
    
    # Demonstrate error handling
    print("\nError Handling:")
    try:
        power(2, -3)
    except ValueError as e:
        print(f"  Attempting negative exponent: {e}")


def demonstrate_statistics():
    """Demonstrate Level 3: Statistics (uses Calculator and Basic Operations)."""
    print_section("LEVEL 3: STATISTICS (builds on Level 2 & Level 1)")
    
    # Sample dataset
    data = [12, 15, 18, 20, 22, 25, 28, 30, 32, 35]
    
    print(f"Dataset: {data}")
    print(f"\nMean: {mean(data):.2f}")
    print(f"Median: {median(data):.2f}")
    print(f"Variance: {variance(data):.2f}")
    print(f"Standard Deviation: {standard_deviation(data):.2f}")
    print(f"Range: {range_stat(data)}")
    print(f"Coefficient of Variation: {coefficient_of_variation(data):.2f}%")


def demonstrate_real_world_example():
    """Demonstrate a real-world example using all three levels."""
    print_section("REAL-WORLD EXAMPLE: Student Grade Analysis")
    
    # Student test scores
    student_scores = [78, 82, 75, 90, 88, 76, 85, 92, 79, 84]
    
    print(f"Test Scores: {student_scores}\n")
    
    # Using Level 3 (Statistics)
    avg_score = mean(student_scores)
    median_score = median(student_scores)
    std_dev = standard_deviation(student_scores)
    
    print(f"Class Average: {avg_score:.2f}")
    print(f"Median Score: {median_score:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")
    
    # Using Level 2 (Calculator) with Level 3 results
    print(f"\nGrade Distribution:")
    for score in sorted(set(student_scores)):
        pct = percentage(score, 100)
        print(f"  Score {score}: {pct:.0f}% of maximum")
    
    # Using Level 1 (Basic Operations) to calculate passing rate
    passing_threshold = 70
    passing_students = sum(1 for score in student_scores if score >= passing_threshold)
    passing_rate = percentage(passing_students, len(student_scores))
    print(f"\nPassing Rate (≥{passing_threshold}): {passing_rate:.1f}%")
    
    # Calculate grade boundaries
    print(f"\nGrade Boundaries:")
    a_grade = add(avg_score, std_dev)
    b_grade = avg_score
    c_grade = subtract(avg_score, std_dev)
    
    print(f"  A: {a_grade:.1f} and above")
    print(f"  B: {b_grade:.1f} to {a_grade:.1f}")
    print(f"  C: {c_grade:.1f} to {b_grade:.1f}")
    print(f"  Below C: below {c_grade:.1f}")


def run_all_tests():
    """Run all unit tests for the three modules."""
    print_section("RUNNING ALL UNIT TESTS")
    
    import unittest
    import test_basic_operations
    import test_calculator
    import test_statistics
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all tests
    suite.addTests(loader.loadTestsFromModule(test_basic_operations))
    suite.addTests(loader.loadTestsFromModule(test_calculator))
    suite.addTests(loader.loadTestsFromModule(test_statistics))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    return result.wasSuccessful()


def main():
    """Main function to demonstrate the entire project."""
    print("\n" + "█"*60)
    print("  MULTILEVEL PROJECT DEMONSTRATION")
    print("  Learning Unit Testing with 3-Level Module Architecture")
    print("█"*60)
    
    # Demonstrate each level
    demonstrate_basic_operations()
    demonstrate_calculator()
    demonstrate_statistics()
    demonstrate_real_world_example()
    
    # Run all tests
    print("\n" + "█"*60)
    run_all_tests()
    
    print("\n" + "█"*60)
    print("  DEMONSTRATION COMPLETE!")
    print("█"*60)
    print("\nProject Structure:")
    print("  Level 1: basic_operations.py (4 functions)")
    print("  Level 2: calculator.py (uses Level 1, adds 4 functions)")
    print("  Level 3: statistics.py (uses Level 2 & 1, adds 6 functions)")
    print("\nTest Coverage:")
    print("  test_basic_operations.py (13 test cases)")
    print("  test_calculator.py (21 test cases)")
    print("  test_statistics.py (32 test cases)")
    print("  Total: 66 test cases")
    print("\nTo run tests individually:")
    print("  python test_basic_operations.py")
    print("  python test_calculator.py")
    print("  python test_statistics.py")
    print("  python main.py  # Run all tests and demonstrations")


if __name__ == "__main__":
    main()
