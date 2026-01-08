"""
Level 1: Basic Operations Module
This module provides fundamental arithmetic operations.
These are the building blocks for more complex calculations.
"""

def add(a, b):
    """
    Add two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    
    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
    """
    return a + b


def subtract(a, b):
    """
    Subtract second number from first number.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The difference of a and b
    
    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(0, 5)
        -5
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The product of a and b
    
    Examples:
        >>> multiply(3, 4)
        12
        >>> multiply(-2, 3)
        -6
    """
    return a * b


def divide(a, b):
    """
    Divide first number by second number.
    
    Args:
        a: Numerator
        b: Denominator
    
    Returns:
        The quotient of a and b
    
    Raises:
        ValueError: If b is zero
    
    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
