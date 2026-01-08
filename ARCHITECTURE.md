# Project Architecture Visualization

## 🏗️ Module Dependency Tree

```
                    ┌─────────────────────┐
                    │   statistics.py     │
                    │   (Level 3)         │
                    │                     │
                    │  - mean()           │
                    │  - variance()       │
                    │  - std_deviation()  │
                    │  - median()         │
                    │  - range_stat()     │
                    │  - coeff_var()      │
                    └──────────┬──────────┘
                               │ uses
                               ▼
                    ┌─────────────────────┐
                    │   calculator.py     │
                    │   (Level 2)         │
                    │                     │
                    │  - power()          │
                    │  - average()        │
                    │  - percentage()     │
                    │  - sum_range()      │
                    └──────────┬──────────┘
                               │ uses
                               ▼
                    ┌─────────────────────┐
                    │ basic_operations.py │
                    │   (Level 1)         │
                    │                     │
                    │  - add()            │
                    │  - subtract()       │
                    │  - multiply()       │
                    │  - divide()         │
                    └─────────────────────┘
```

## 🧪 Test Coverage Tree

```
┌────────────────────────────────────────────────────────────┐
│                      main.py                               │
│              (Runs all tests + demos)                      │
└────────────────────┬───────────────────────────────────────┘
                     │
         ┌───────────┼───────────┐
         │           │           │
         ▼           ▼           ▼
┌────────────┐ ┌────────────┐ ┌────────────┐
│test_basic_ │ │test_calc   │ │test_stats  │
│operations  │ │            │ │            │
│            │ │            │ │            │
│ 13 tests   │ │ 21 tests   │ │ 32 tests   │
└─────┬──────┘ └─────┬──────┘ └─────┬──────┘
      │              │              │
      │ tests        │ tests        │ tests
      ▼              ▼              ▼
┌────────────┐ ┌────────────┐ ┌────────────┐
│basic_ops   │ │calculator  │ │statistics  │
│  Level 1   │ │  Level 2   │ │  Level 3   │
└────────────┘ └────────────┘ └────────────┘
```

## 📊 Function Call Flow Example

### Example: Calculating Coefficient of Variation

```
User Code:
    coefficient_of_variation([2, 4, 6, 8])
                    │
                    ▼
    ┌───────────────────────────────────┐
    │ statistics.py: coefficient_of_var()│
    └───────────────┬───────────────────┘
                    │
        ┌───────────┴────────────┐
        │                        │
        ▼                        ▼
    mean([2,4,6,8])        standard_deviation([2,4,6,8])
        │                        │
        │                        ├──► variance([2,4,6,8])
        │                        │         │
        ▼                        │         └──► mean() again
    average([2,4,6,8])          │
        │                        │
        ▼                        │
    ┌───────────────────────────┼────────┐
    │   calculator.py: average() │        │
    └───────────────┬────────────┘        │
                    │                     │
        ┌───────────┴────────────┐       │
        │                        │       │
        ▼                        ▼       │
    add(2, 4)              divide(sum, 4)│
    add(6, 6)                    │       │
    add(12, 8)                   │       │
        │                        │       │
        ▼                        ▼       ▼
    ┌───────────────────────────────────┐
    │ basic_operations.py               │
    │   - add()                         │
    │   - subtract()                    │
    │   - multiply()                    │
    │   - divide()                      │
    └───────────────────────────────────┘
```

## 🎯 Data Flow Example: Student Grades

```
Input: student_scores = [78, 82, 75, 90, 88]

┌─────────────────────────────────────────┐
│         Level 3: Statistics             │
│                                         │
│  mean(scores) ──────────► 82.6         │
│  std_dev(scores) ───────► 5.7          │
│  median(scores) ─────────► 82          │
└────────────┬────────────────────────────┘
             │ calls
             ▼
┌─────────────────────────────────────────┐
│         Level 2: Calculator             │
│                                         │
│  average([78,82,75,90,88])             │
│    └──► sum using add()                │
│    └──► divide by count                │
│                                         │
│  percentage(82.6, 100) ───► 82.6%     │
└────────────┬────────────────────────────┘
             │ calls
             ▼
┌─────────────────────────────────────────┐
│      Level 1: Basic Operations          │
│                                         │
│  add(78, 82) = 160                     │
│  add(160, 75) = 235                    │
│  add(235, 90) = 325                    │
│  add(325, 88) = 413                    │
│  divide(413, 5) = 82.6                 │
└─────────────────────────────────────────┘
```

## 🧪 Test Dependency Matrix

| Test File | Tests Module | Uses Modules | Test Count |
|-----------|--------------|--------------|------------|
| test_basic_operations.py | basic_operations.py | None | 13 |
| test_calculator.py | calculator.py | basic_operations.py | 21 |
| test_statistics.py | statistics.py | calculator.py, basic_operations.py | 32 |

## 📈 Coverage Map

```
Module: basic_operations.py
├── add()          ✅ 3 tests
├── subtract()     ✅ 2 tests
├── multiply()     ✅ 3 tests
└── divide()       ✅ 4 tests + error handling

Module: calculator.py
├── power()        ✅ 5 tests + error handling
├── average()      ✅ 5 tests + error handling
├── percentage()   ✅ 4 tests + error handling
└── sum_range()    ✅ 4 tests

Module: statistics.py
├── mean()         ✅ 4 tests + error handling
├── variance()     ✅ 4 tests + error handling
├── std_deviation()✅ 4 tests + error handling
├── median()       ✅ 6 tests + error handling
├── range_stat()   ✅ 6 tests + error handling
└── coeff_var()    ✅ 4 tests + error handling
```

## 🔄 Integration Points

```
┌─────────────────────────────────────────────────┐
│                                                 │
│  Integration Point 1: Calculator uses Basic Ops │
│  ────────────────────────────────────────────  │
│                                                 │
│  calculator.power() ──┐                        │
│  calculator.average() │                        │
│  calculator.percentage()─► basic_operations.*  │
│  calculator.sum_range()─┘                      │
│                                                 │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│                                                 │
│  Integration Point 2: Statistics uses Calculator│
│  ────────────────────────────────────────────  │
│                                                 │
│  statistics.mean() ──┐                         │
│  statistics.variance()─► calculator.average()  │
│  statistics.median() ─┘                        │
│                                                 │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│                                                 │
│  Integration Point 3: Statistics uses Basic Ops │
│  ────────────────────────────────────────────  │
│                                                 │
│  statistics.variance() ──┐                     │
│  statistics.std_dev()     │                    │
│  statistics.range_stat()  ├─► basic_operations.*│
│  statistics.coeff_var()  ─┘                    │
│                                                 │
└─────────────────────────────────────────────────┘
```

## 🎓 Key Principles Demonstrated

1. **Separation of Concerns**: Each level has a specific purpose
2. **Dependency Management**: Higher levels depend on lower levels only
3. **Testability**: Each module can be tested independently
4. **Reusability**: Lower level functions are reused extensively
5. **Maintainability**: Changes to Level 1 propagate upward
6. **Extensibility**: Easy to add new functions at any level

## 📝 Adding New Features

To add a new feature at any level:

```
Level 1 (Basic Operations)
    │
    ├─ Add function
    ├─ Add tests
    └─ Can be used by Levels 2 & 3

Level 2 (Calculator)
    │
    ├─ Add function (using Level 1)
    ├─ Add tests
    └─ Can be used by Level 3

Level 3 (Statistics)
    │
    ├─ Add function (using Levels 1 & 2)
    └─ Add tests
```

Each level builds on the stability of the level below it!
