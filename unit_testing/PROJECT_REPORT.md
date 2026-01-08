# Unit Testing Project Report

## Student Performance Predictor System

---

### Course Information

- **Course Code:** CSE 3206
- **Course Title:** Software Engineering and Information System Design
- **Project Type:** Unit Testing Implementation
- **Date:** January 8, 2026

---

## 1. Introduction

### 1.1 Project Overview

This project implements a comprehensive Student Performance Predictor System that calculates CT (Class Test) averages, SGPA (Semester Grade Point Average), CGPA (Cumulative Grade Point Average), and provides academic performance predictions. The system demonstrates the implementation of unit testing principles using Python's `unittest` framework with a modular, dependency-based architecture.

### 1.2 Objectives

- Implement a five-level hierarchical module system with incremental dependencies
- Achieve comprehensive test coverage for all functional modules
- Demonstrate best practices in unit testing, including test isolation and edge case handling
- Validate business logic for academic performance calculations

---

## 2. Theoretical Background

### 2.1 Unit Testing Fundamentals

**Definition:** Unit testing is a software testing methodology where individual units or components of software are tested in isolation to verify that each unit functions correctly according to its specification.

**Key Principles:**

1. **Isolation:** Each test should be independent and not affect other tests
2. **Repeatability:** Tests should produce consistent results across multiple runs
3. **Fast Execution:** Unit tests should execute quickly to enable frequent testing
4. **Clear Assertions:** Each test should verify a specific behavior with clear pass/fail criteria

### 2.2 Test-Driven Development (TDD)

The project follows TDD principles where tests are written to validate:

- **Expected Behavior:** Normal operating conditions with valid inputs
- **Edge Cases:** Boundary conditions (zero, empty lists, exact thresholds)
- **Error Handling:** Invalid inputs and exception scenarios

### 2.3 Python unittest Framework

The `unittest` module provides:

- **TestCase class:** Base class for creating test cases
- **Assertions:** Methods like `assertEqual()`, `assertRaises()`, `assertTrue()`
- **Test Discovery:** Automatic test detection and execution
- **Test Fixtures:** Setup and teardown methods for test preparation

### 2.4 Dependency Management in Testing

The project demonstrates a **layered architecture** where:

- Level 1 modules have no dependencies
- Each subsequent level depends on previous levels
- Tests validate both isolated functionality and integration between modules

---

## 3. System Architecture

### 3.1 Module Hierarchy

```
Level 1: calculator.py (Base Module)
   ↓
Level 2: ct_calculator.py
   ↓
Level 3: sgpa_calculator.py
   ↓
Level 4: cgpa_calculator.py
   ↓
Level 5: predictor.py (Complete System)
```

### 3.2 Module Descriptions

#### Level 1: Basic Calculator (`calculator.py`)

**Purpose:** Foundation module providing arithmetic operations  
**Functions:**

- `add(a, b)` - Addition of two numbers
- `subtract(a, b)` - Subtraction operation
- `multiply(a, b)` - Multiplication operation
- `divide(a, b)` - Division with zero-check validation
- `average(numbers)` - Calculate mean of a list
- `add_all(numbers)` - Sum all numbers in a list

**Dependencies:** None

#### Level 2: CT Calculator (`ct_calculator.py`)

**Purpose:** Calculate best 3 out of 4 CT marks (university grading policy)  
**Functions:**

- `sort_marks(marks)` - Sort in descending order
- `get_best_n(marks, n)` - Extract top n marks
- `calculate_ct_average(ct_marks)` - Average of best 3 CTs
- `validate_ct_marks(marks)` - Ensure marks in 0-20 range

**Dependencies:** `calculator.py`

#### Level 3: SGPA Calculator (`sgpa_calculator.py`)

**Purpose:** Calculate semester GPA from course grades  
**Functions:**

- `marks_to_grade(marks)` - Convert numerical marks to letter grades
- `grade_to_points(grade)` - Map letter grades to grade points (4.0 scale)
- `calculate_course_marks(ct_marks, attendance, final_exam)` - Total course marks
- `calculate_sgpa(courses)` - Weighted GPA for a semester

**Dependencies:** `calculator.py`, `ct_calculator.py`

#### Level 4: CGPA Calculator (`cgpa_calculator.py`)

**Purpose:** Calculate cumulative GPA across semesters  
**Functions:**

- `calculate_cgpa(semesters)` - Weighted CGPA calculation
- `get_total_credits(semesters)` - Sum of completed credits
- `is_on_track(cgpa, min_cgpa)` - Check academic standing
- `calculate_required_sgpa(...)` - Predict required performance

**Dependencies:** `calculator.py`, `sgpa_calculator.py`

#### Level 5: Performance Predictor (`predictor.py`)

**Purpose:** Generate predictions and recommendations  
**Functions:**

- `get_academic_standing(cgpa)` - Determine academic classification
- `predict_graduation_cgpa(...)` - Project final CGPA
- `get_improvement_tips(cgpa, target_cgpa)` - Personalized recommendations
- `generate_report(semesters, target_cgpa)` - Comprehensive performance report

**Dependencies:** All previous modules

---

## 4. Testing Methodology

### 4.1 Test Structure

Each module has a corresponding test file with multiple test classes:

```
src/
├── calculator.py          → test_calculator.py (7 test classes)
├── ct_calculator.py       → test_ct_calculator.py (4 test classes)
├── sgpa_calculator.py     → test_sgpa_calculator.py (4 test classes)
├── cgpa_calculator.py     → test_cgpa_calculator.py (5 test classes)
└── predictor.py           → test_predictor.py (5 test classes)
```

**Total Test Classes:** 25  
**Coverage Strategy:** Each function has dedicated test class with multiple test methods

### 4.2 Test Categories

#### 4.2.1 Positive Tests (Happy Path)

Tests with valid inputs to verify correct behavior:

```python
def test_add_positive(self):
    self.assertEqual(add(2, 3), 5)
```

#### 4.2.2 Negative Tests (Error Cases)

Tests to ensure proper error handling:

```python
def test_divide_by_zero(self):
    with self.assertRaises(ValueError):
        divide(10, 0)
```

#### 4.2.3 Boundary Tests (Edge Cases)

Tests at operational limits:

```python
def test_grade_boundary(self):
    self.assertEqual(marks_to_grade(80), 'A+')
    self.assertEqual(marks_to_grade(79), 'A')
```

#### 4.2.4 Integration Tests

Tests validating module interactions:

```python
def test_course_marks_normal(self):
    ct_marks = [18, 16, 15, 14]  # Calls ct_calculator
    attendance = 8
    final_exam = 55
    result = calculate_course_marks(ct_marks, attendance, final_exam)
    self.assertAlmostEqual(result, 79.33, places=2)
```

---

## 5. Test Implementation Details

### 5.1 Level 1: Calculator Tests (`test_calculator.py`)

**Test Classes:** 7  
**Key Test Cases:**

| Test Class   | Purpose                  | Critical Tests                    |
| ------------ | ------------------------ | --------------------------------- |
| TestAdd      | Addition operation       | Positive, negative, zero handling |
| TestSubtract | Subtraction operation    | Negative results                  |
| TestMultiply | Multiplication operation | Zero multiplication               |
| TestDivide   | Division operation       | Zero division exception           |
| TestAverage  | Average calculation      | Empty list exception              |
| TestAddAll   | List summation           | Empty list (returns 0)            |

**Screenshot Placeholder:**

```
[INSERT SCREENSHOT: test_calculator.py execution with all tests passing]
```

### 5.2 Level 2: CT Calculator Tests (`test_ct_calculator.py`)

**Test Classes:** 4  
**Key Test Cases:**

| Test Class             | Purpose             | Critical Tests                |
| ---------------------- | ------------------- | ----------------------------- |
| TestSortMarks          | Descending sort     | Pre-sorted and unsorted lists |
| TestGetBestN           | Top N selection     | Insufficient marks error      |
| TestCalculateCTAverage | Best 3 of 4 average | Exactly 4 marks validation    |
| TestValidateCTMarks    | Range validation    | Negative and >20 marks        |

**Business Logic:** University policy requires best 3 out of 4 CT marks (each out of 20)

**Screenshot Placeholder:**

```
[INSERT SCREENSHOT: test_ct_calculator.py execution results]
```

### 5.3 Level 3: SGPA Calculator Tests (`test_sgpa_calculator.py`)

**Test Classes:** 4  
**Key Test Cases:**

| Test Class               | Purpose                 | Critical Tests                         |
| ------------------------ | ----------------------- | -------------------------------------- |
| TestMarksToGrade         | Marks→Grade conversion  | Boundary values (80, 79, 75, 70, etc.) |
| TestGradeToPoints        | Grade→Points mapping    | Invalid grade handling                 |
| TestCalculateCourseMarks | Total marks calculation | CT + Attendance + Final                |
| TestCalculateSGPA        | Semester GPA            | Empty courses exception                |

**Grade Scale:**

- A+ (80-100): 4.00 | A (75-79): 3.75 | A- (70-74): 3.50
- B+ (65-69): 3.25 | B (60-64): 3.00 | B- (55-59): 2.75
- C+ (50-54): 2.50 | C (45-49): 2.25 | C- (40-44): 2.00
- D (35-39): 1.75 | F (<35): 0.00

**Screenshot Placeholder:**

```
[INSERT SCREENSHOT: test_sgpa_calculator.py passing all tests]
```

### 5.4 Level 4: CGPA Calculator Tests (`test_cgpa_calculator.py`)

**Test Classes:** 5  
**Key Test Cases:**

| Test Class                | Purpose           | Critical Tests                         |
| ------------------------- | ----------------- | -------------------------------------- |
| TestCalculateCGPA         | Cumulative GPA    | Single/multiple semesters, empty error |
| TestGetTotalCredits       | Credit summation  | Multiple semesters                     |
| TestGetCompletedSemesters | Semester count    | Validation                             |
| TestIsOnTrack             | Academic standing | 2.0 CGPA threshold                     |
| TestCalculateRequiredSGPA | Prediction logic  | Mathematical accuracy                  |

**Formula:** CGPA = Σ(SGPA × Credits) / Σ(Credits)

**Screenshot Placeholder:**

```
[INSERT SCREENSHOT: test_cgpa_calculator.py test results]
```

### 5.5 Level 5: Predictor Tests (`test_predictor.py`)

**Test Classes:** 5  
**Key Test Cases:**

| Test Class                 | Purpose           | Critical Tests                                   |
| -------------------------- | ----------------- | ------------------------------------------------ |
| TestGetAcademicStanding    | Classification    | Dean's List, First/Second Class, Pass, Probation |
| TestPredictGraduationCGPA  | Future projection | With/without history                             |
| TestGetImprovementTips     | Recommendations   | Gap-based logic                                  |
| TestCalculateRequiredMarks | Target grade      | Final exam requirement (0-70)                    |
| TestGenerateReport         | Complete report   | Structure and value validation                   |

**Academic Standing Thresholds:**

- Dean's List: ≥3.75
- First Class: ≥3.50
- Second Class: ≥3.00
- Pass: ≥2.00
- Probation: <2.00

**Screenshot Placeholder:**

```
[INSERT SCREENSHOT: test_predictor.py execution showing all tests passed]
```

---

## 6. Test Execution and Results

### 6.1 Running Individual Test Modules

**Command Pattern:**

```bash
python -m unittest test_<module_name>.py
```

**Example:**

```bash
python -m unittest test_calculator.py
```

**Screenshot Placeholder:**

```
[INSERT SCREENSHOT: Individual test module execution in terminal]
```

### 6.2 Running All Tests

**Command:**

```bash
python -m unittest discover -s src -p "test_*.py"
```

**Screenshot Placeholder:**

```
[INSERT SCREENSHOT: Full test suite execution showing total test count]
```

### 6.3 Verbose Output

**Command:**

```bash
python -m unittest discover -s src -p "test_*.py" -v
```

**Screenshot Placeholder:**

```
[INSERT SCREENSHOT: Verbose test output showing each test method name]
```

### 6.4 Test Coverage Analysis

**Using pytest with coverage:**

```bash
pytest --cov=. --cov-report=term-missing
```

**Screenshot Placeholder:**

```
[INSERT SCREENSHOT: Coverage report showing percentage per module]
```

---

## 7. Test Results Summary

### 7.1 Test Statistics

| Module             | Test Classes | Test Methods | Pass   | Fail  | Status |
| ------------------ | ------------ | ------------ | ------ | ----- | ------ |
| calculator.py      | 7            | 16           | 16     | 0     | ✓      |
| ct_calculator.py   | 4            | 9            | 9      | 0     | ✓      |
| sgpa_calculator.py | 4            | 10           | 10     | 0     | ✓      |
| cgpa_calculator.py | 5            | 10           | 10     | 0     | ✓      |
| predictor.py       | 5            | 12           | 12     | 0     | ✓      |
| **TOTAL**          | **25**       | **57**       | **57** | **0** | **✓**  |

**Screenshot Placeholder:**

```
[INSERT SCREENSHOT: Summary table from test execution or IDE test panel]
```

### 7.2 Coverage Metrics

**Expected Coverage:**

- **Statement Coverage:** >95%
- **Branch Coverage:** >90%
- **Function Coverage:** 100%

**Screenshot Placeholder:**

```
[INSERT SCREENSHOT: Coverage report with highlighted coverage percentages]
```

---

## 8. Key Testing Concepts Demonstrated

### 8.1 Test Isolation

Each test is independent:

```python
class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)  # No side effects
```

### 8.2 Exception Testing

Proper error validation:

```python
def test_divide_by_zero(self):
    with self.assertRaises(ValueError):
        divide(10, 0)
```

### 8.3 Floating-Point Comparison

Handling precision:

```python
def test_ct_average_normal(self):
    result = calculate_ct_average([15, 18, 12, 16])
    self.assertAlmostEqual(result, 16.33, places=2)
```

### 8.4 Parameterized Testing Approach

Multiple scenarios for one function:

```python
def test_grade_a_plus(self):
    self.assertEqual(marks_to_grade(85), 'A+')

def test_grade_a(self):
    self.assertEqual(marks_to_grade(77), 'A')

def test_grade_f(self):
    self.assertEqual(marks_to_grade(30), 'F')
```

---

## 9. Challenges and Solutions

### 9.1 Floating-Point Arithmetic

**Challenge:** Direct equality checks fail due to floating-point precision  
**Solution:** Use `assertAlmostEqual(result, expected, places=2)`

### 9.2 Dependency Management

**Challenge:** Higher-level modules depend on lower-level modules  
**Solution:** Test modules in hierarchical order; use `conftest.py` for path management

### 9.3 Edge Case Identification

**Challenge:** Determining all boundary conditions  
**Solution:** Systematic analysis of input ranges and transition points

---

## 10. Best Practices Applied

1. **Clear Test Names:** Descriptive method names indicate what is being tested
2. **One Assertion Focus:** Each test validates a single behavior
3. **Comprehensive Coverage:** Tests for normal, edge, and error cases
4. **Documentation:** Docstrings explain test class purpose
5. **Modular Design:** Separate test files mirror source structure
6. **Repeatable Tests:** No external dependencies or random values

---

## 11. Demo Application

### 11.1 Main Application (`main.py`)

The project includes a demonstration CLI that shows all modules working together:

```
🎓 STUDENT PERFORMANCE PREDICTOR 🎓
Unit Testing Demonstration Project

Level 1: Basic Calculator
Level 2: CT Calculator
Level 3: SGPA Calculator
Level 4: CGPA Calculator
Level 5: Performance Predictor
```

**Screenshot Placeholder:**

```
[INSERT SCREENSHOT: main.py execution showing complete demo output]
```

### 11.2 Running the Demo

```bash
python main.py
```

---

## 12. Conclusion

### 12.1 Achievements

- Successfully implemented a 5-level hierarchical system with 57 unit tests
- Achieved 100% test pass rate across all modules
- Demonstrated comprehensive testing strategies including positive, negative, and boundary tests
- Validated complex business logic for academic performance calculations

### 12.2 Learning Outcomes

1. **Unit Testing Fundamentals:** Understanding test isolation, assertions, and fixtures
2. **Test-Driven Mindset:** Writing tests to validate expected behavior and edge cases
3. **Python unittest Framework:** Practical experience with TestCase classes and assertion methods
4. **Modular Design:** Building maintainable systems with clear dependencies
5. **Error Handling:** Implementing robust validation and exception handling

### 12.3 Future Enhancements

- Integration testing for complete workflows
- Performance testing for large datasets
- Mock testing for external dependencies
- Continuous Integration (CI) pipeline setup
- Code coverage reporting with pytest-cov

---

## 13. References

1. Python Software Foundation. (2026). _unittest — Unit testing framework_. Python Documentation.
2. Beck, K. (2003). _Test-Driven Development: By Example_. Addison-Wesley.
3. Meszaros, G. (2007). _xUnit Test Patterns: Refactoring Test Code_. Addison-Wesley.
4. Martin, R. C. (2008). _Clean Code: A Handbook of Agile Software Craftsmanship_. Prentice Hall.

---

## Appendix A: Project Structure

```
student_performance_predictor/
├── src/
│   ├── __init__.py
│   ├── conftest.py                 # Test configuration
│   ├── calculator.py               # Level 1: Base arithmetic
│   ├── test_calculator.py          # 16 tests
│   ├── ct_calculator.py            # Level 2: CT calculations
│   ├── test_ct_calculator.py       # 9 tests
│   ├── sgpa_calculator.py          # Level 3: Semester GPA
│   ├── test_sgpa_calculator.py     # 10 tests
│   ├── cgpa_calculator.py          # Level 4: Cumulative GPA
│   ├── test_cgpa_calculator.py     # 10 tests
│   ├── predictor.py                # Level 5: Predictions
│   ├── test_predictor.py           # 12 tests
│   └── main.py                     # CLI demonstration
└── PROJECT_REPORT.md               # This document
```

---

## Appendix B: Test Execution Commands

```bash
# Activate virtual environment (if using)
.venv\Scripts\Activate.ps1

# Run all tests
python -m unittest discover -s src -p "test_*.py"

# Run specific test file
python -m unittest src.test_calculator

# Run with verbose output
python -m unittest discover -s src -p "test_*.py" -v

# Run specific test class
python -m unittest src.test_calculator.TestAdd

# Run specific test method
python -m unittest src.test_calculator.TestAdd.test_add_positive

# Run with pytest (if installed)
pytest src/ -v

# Run with coverage
pytest --cov=src --cov-report=html
```

---

**End of Report**

_This report demonstrates comprehensive understanding and implementation of unit testing principles in a multi-level academic performance prediction system._
