# Quick Start Guide - Unit Testing Project

## ⚡ Quick Commands

### Run Everything (Recommended First Time)
```bash
python main.py
```

### Run Individual Test Files
```bash
# Test Level 1 only (Basic Operations)
python test_basic_operations.py

# Test Level 2 only (Calculator)
python test_calculator.py

# Test Level 3 only (Statistics)
python test_statistics.py
```

### Run Specific Test Class
```bash
python -m unittest test_basic_operations.TestBasicOperations
python -m unittest test_calculator.TestCalculator
python -m unittest test_statistics.TestStatistics
```

### Run Specific Test Method
```bash
python -m unittest test_basic_operations.TestBasicOperations.test_add_positive_numbers
python -m unittest test_calculator.TestCalculator.test_power_positive_numbers
python -m unittest test_statistics.TestStatistics.test_mean_positive_numbers
```

## 📊 What Each File Does

| File | Purpose | Dependencies |
|------|---------|--------------|
| `basic_operations.py` | Level 1 - Basic math | None |
| `calculator.py` | Level 2 - Advanced calc | basic_operations |
| `statistics.py` | Level 3 - Stats analysis | calculator, basic_operations |
| `test_basic_operations.py` | Tests for Level 1 | basic_operations |
| `test_calculator.py` | Tests for Level 2 | calculator |
| `test_statistics.py` | Tests for Level 3 | statistics |
| `main.py` | Demo + Run all tests | All modules |

## 🎯 Learning Path

### Day 1: Understand the Basics
1. Read [basic_operations.py](basic_operations.py)
2. Read [test_basic_operations.py](test_basic_operations.py)
3. Run: `python test_basic_operations.py`
4. **Exercise**: Add a `modulo(a, b)` function and test it

### Day 2: Build on Top
1. Read [calculator.py](calculator.py)
2. Read [test_calculator.py](test_calculator.py)
3. Run: `python test_calculator.py`
4. **Exercise**: Add a `factorial(n)` function using multiply

### Day 3: Advanced Integration
1. Read [statistics.py](statistics.py)
2. Read [test_statistics.py](test_statistics.py)
3. Run: `python test_statistics.py`
4. **Exercise**: Add a `mode(numbers)` function

### Day 4: Full Integration
1. Run: `python main.py`
2. Study how all modules work together
3. **Exercise**: Create your own real-world example

## 🔍 Common Test Patterns

### Testing Normal Cases
```python
def test_add_positive_numbers(self):
    self.assertEqual(add(2, 3), 5)
```

### Testing Edge Cases
```python
def test_add_zero(self):
    self.assertEqual(add(5, 0), 5)
```

### Testing Errors
```python
def test_divide_by_zero_raises_error(self):
    with self.assertRaises(ValueError):
        divide(10, 0)
```

### Testing Floats
```python
def test_standard_deviation(self):
    result = standard_deviation([1, 2, 3, 4, 5])
    self.assertAlmostEqual(result, 1.414, places=3)
```

## 💡 Tips

1. **Always run tests after making changes**
2. **Write tests before fixing bugs** (reproduce the bug in a test first)
3. **Keep tests simple and focused** (one thing per test)
4. **Use descriptive test names** (explain what you're testing)
5. **Test both success and failure paths**

## 🐛 Troubleshooting

### Import Error?
Make sure you're in the correct directory:
```bash
cd "e:\3-2\CSE 3206"
```

### Test Failed?
Read the error message carefully. It tells you:
- Which test failed
- What was expected
- What was received

### Want More Details?
Add verbosity to any test:
```bash
python test_basic_operations.py -v
```

## 📈 Next Steps

After mastering this project:
1. Learn about **mocking** and **patching**
2. Explore **pytest** (alternative to unittest)
3. Study **test coverage** tools
4. Practice **Test-Driven Development (TDD)**
5. Learn about **integration** vs **unit** testing

## 🎓 Key Takeaways

- ✅ Each level builds on the previous one
- ✅ Tests verify both functionality and error handling
- ✅ Good tests make refactoring safe
- ✅ Test names should describe what they test
- ✅ 100% test coverage doesn't mean bug-free, but it helps!

---

**Start with:** `python main.py`

**Practice with:** Individual test files

**Master by:** Adding your own features and tests
