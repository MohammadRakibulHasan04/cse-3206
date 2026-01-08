"""
Level 2: Calculator Module
This module provides advanced calculations by using basic_operations.
Demonstrates building on top of simpler modules.
"""

from basic_operations import add, subtract, multiply, divide


def power(base, exponent):
    """
    Calculate base raised to the power of exponent.
    Uses repeated multiplication from basic_operations.
    
    Args:
        base: The base number
        exponent: The exponent (must be non-negative integer)
    
    Returns:
        base raised to the power of exponent
    
    Raises:
        ValueError: If exponent is negative or not an integer
    
    Examples:
        >>> power(2, 3)
        8
        >>> power(5, 0)
        1
    """
    if not isinstance(exponent, int) or exponent < 0:
        raise ValueError("Exponent must be a non-negative integer")
    
    if exponent == 0:
        return 1
    
    result = base
    for _ in range(exponent - 1):
        result = multiply(result, base)
    
    return result


def average(numbers):
    """
    Calculate the average of a list of numbers.
    Uses add and divide from basic_operations.
    
    Args:
        numbers: List of numbers
    
    Returns:
        The average of the numbers
    
    Raises:
        ValueError: If the list is empty
    
    Examples:
        >>> average([1, 2, 3, 4, 5])
        3.0
        >>> average([10, 20])
        15.0
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    
    total = numbers[0]
    for num in numbers[1:]:
        total = add(total, num)
    
    return divide(total, len(numbers))


def percentage(part, whole):
    """
    Calculate what percentage 'part' is of 'whole'.
    Uses divide and multiply from basic_operations.
    
    Args:
        part: The part value
        whole: The whole value
    
    Returns:
        The percentage (0-100)
    
    Raises:
        ValueError: If whole is zero
    
    Examples:
        >>> percentage(25, 100)
        25.0
        >>> percentage(1, 4)
        25.0
    """
    if whole == 0:
        raise ValueError("Whole cannot be zero")
    
    ratio = divide(part, whole)
    return multiply(ratio, 100)


def sum_range(start, end):
    """
    Calculate the sum of all integers from start to end (inclusive).
    Uses add from basic_operations.
    
    Args:
        start: Starting number (inclusive)
        end: Ending number (inclusive)
    
    Returns:
        Sum of all numbers in range
    
    Examples:
        >>> sum_range(1, 5)
        15
        >>> sum_range(0, 3)
        6
    """
    if start > end:
        return 0
    
    result = start
    for num in range(start + 1, end + 1):
        result = add(result, num)
    
    return result
