# Multilevel Unit Testing Project

## 📚 Project Overview

This is a comprehensive Python project designed to demonstrate unit testing concepts through a **3-level module architecture**. Each level builds upon the previous one, showcasing how to test both isolated functions and integrated systems.

## 🏗️ Architecture

### Level 1: Basic Operations (`basic_operations.py`)
**Foundation Module** - Contains fundamental arithmetic operations
- `add(a, b)` - Addition
- `subtract(a, b)` - Subtraction  
- `multiply(a, b)` - Multiplication
- `divide(a, b)` - Division (with error handling)

**Tests:** `test_basic_operations.py` (13 test cases)
- Normal cases
- Edge cases (zero, negatives)
- Error handling (divide by zero)

### Level 2: Calculator (`calculator.py`)
**Intermediate Module** - Uses basic_operations to build advanced functions
- `power(base, exponent)` - Exponentiation using repeated multiplication
- `average(numbers)` - Calculate mean using add and divide
- `percentage(part, whole)` - Calculate percentage
- `sum_range(start, end)` - Sum of range using add

**Tests:** `test_calculator.py` (21 test cases)
- Integration testing (tests functions that depend on Level 1)
- Input validation
- Edge cases

### Level 3: Statistics (`statistics.py`)
**Advanced Module** - Uses calculator and basic_operations for statistical analysis
- `mean(numbers)` - Arithmetic mean
- `variance(numbers)` - Statistical variance
- `standard_deviation(numbers)` - Standard deviation
- `median(numbers)` - Median value
- `range_stat(numbers)` - Range (max - min)
- `coefficient_of_variation(numbers)` - CV percentage

**Tests:** `test_statistics.py` (32 test cases)
- Complex integration testing
- Float comparison with `assertAlmostEqual`
- Multiple edge cases

## 📂 Project Structure

```
CSE 3206/
├── basic_operations.py          # Level 1: Foundation
├── test_basic_operations.py     # Tests for Level 1
├── calculator.py                # Level 2: Intermediate
├── test_calculator.py           # Tests for Level 2
├── statistics.py                # Level 3: Advanced
├── test_statistics.py           # Tests for Level 3
├── main.py                      # Demo and test runner
└── README_UNIT_TESTING.md       # This file
```

## 🚀 How to Run

### Run All Demonstrations and Tests
```bash
python main.py
```

### Run Individual Test Suites
```bash
# Test Level 1
python test_basic_operations.py

# Test Level 2
python test_calculator.py

# Test Level 3
python test_statistics.py
```

### Run Tests with Coverage (optional)
```bash
pip install coverage
coverage run -m unittest discover
coverage report
coverage html
```

## 🎯 Learning Objectives

### 1. **Unit Testing Basics**
- Writing test cases with `unittest`
- Using assertions (`assertEqual`, `assertRaises`, `assertAlmostEqual`)
- Test organization with test classes

### 2. **Test-Driven Development (TDD) Concepts**
- Testing normal cases
- Testing edge cases
- Testing error conditions
- Organizing tests logically

### 3. **Integration Testing**
- Testing functions that depend on other modules
- Verifying interactions between components
- Testing the full stack (Level 3 → Level 2 → Level 1)

### 4. **Best Practices Demonstrated**
- ✅ Descriptive test names
- ✅ Comprehensive docstrings
- ✅ Error handling and validation
- ✅ Testing both success and failure paths
- ✅ Proper test isolation
- ✅ Float comparison for numerical tests

## 📊 Test Coverage Summary

| Module | Functions | Test Cases | Coverage |
|--------|-----------|------------|----------|
| basic_operations | 4 | 13 | 100% |
| calculator | 4 | 21 | 100% |
| statistics | 6 | 32 | 100% |
| **TOTAL** | **14** | **66** | **100%** |

## 💡 Key Concepts Demonstrated

### Error Handling
```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Test
def test_divide_by_zero_raises_error(self):
    with self.assertRaises(ValueError):
        divide(10, 0)
```

### Float Comparison
```python
def test_standard_deviation(self):
    result = standard_deviation([1, 2, 3, 4, 5])
    self.assertAlmostEqual(result, 1.4142135623730951, places=10)
```

### Testing Dependencies
```python
# Level 2 uses Level 1
from basic_operations import add, divide

def average(numbers):
    total = numbers[0]
    for num in numbers[1:]:
        total = add(total, num)  # Uses Level 1
    return divide(total, len(numbers))  # Uses Level 1
```

## 🎓 Real-World Example

The `main.py` includes a practical example: **Student Grade Analysis**
- Calculates class statistics
- Determines grade boundaries
- Shows how all three levels work together

## 🔍 Testing Strategies Shown

1. **Equivalence Partitioning**: Testing representative values from different ranges
2. **Boundary Value Analysis**: Testing edge cases (0, negative, single element)
3. **Error Guessing**: Testing known problematic inputs (divide by zero, empty lists)
4. **State Coverage**: Testing all possible states and paths

## 📝 Notes for Learning

- Start by understanding Level 1, then move up
- Each test file is self-contained and can run independently
- Tests are written to be readable and educational
- Comments explain the "why" behind each test
- Error messages are descriptive and helpful

## 🎨 Customization Ideas

Want to practice more? Try:
1. Add more statistical functions (mode, quartiles, z-scores)
2. Implement matrix operations in Level 2
3. Add data visualization using matplotlib
4. Create a CLI interface for the calculator
5. Add performance testing for large datasets
6. Implement mocking for advanced testing scenarios

## ✅ Success Criteria

After running `python main.py`, you should see:
- All demonstrations execute successfully
- All 66 tests pass
- Clear output showing the 3-level structure
- Real-world example with student grades

---

**Happy Testing! 🧪**

This project demonstrates that good software is built in layers, where each level is thoroughly tested before building the next.
