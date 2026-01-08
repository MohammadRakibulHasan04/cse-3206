"""
Level 1: Basic Calculator (No Dependencies)
Foundation module for all arithmetic operations.
"""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def average(numbers):
    """Calculate average of a list of numbers."""
    if not numbers:
        raise ValueError("List cannot be empty")
    return divide(add_all(numbers), len(numbers))


def add_all(numbers):
    """Sum all numbers in a list."""
    total = 0
    for num in numbers:
        total = add(total, num)
    return total
