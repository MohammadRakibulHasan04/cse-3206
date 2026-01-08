"""
Level 3: Statistics Module
This module provides statistical analysis by using calculator functions.
Demonstrates building complex functionality on top of simpler modules.
"""

from calculator import average, power, sum_range
from basic_operations import subtract, divide, add, multiply


def mean(numbers):
    """
    Calculate the arithmetic mean of a dataset.
    Uses the average function from calculator module.
    
    Args:
        numbers: List of numbers
    
    Returns:
        The mean of the numbers
    
    Raises:
        ValueError: If the list is empty
    
    Examples:
        >>> mean([1, 2, 3, 4, 5])
        3.0
        >>> mean([10, 20, 30])
        20.0
    """
    return average(numbers)


def variance(numbers):
    """
    Calculate the variance of a dataset.
    Uses mean from this module and power from calculator module.
    Variance = average of squared differences from the mean.
    
    Args:
        numbers: List of numbers
    
    Returns:
        The variance of the numbers
    
    Raises:
        ValueError: If the list is empty
    
    Examples:
        >>> variance([1, 2, 3, 4, 5])
        2.0
    """
    if not numbers:
        raise ValueError("Cannot calculate variance of empty list")
    
    data_mean = mean(numbers)
    
    # Calculate sum of squared differences
    squared_diff_sum = 0
    for num in numbers:
        diff = subtract(num, data_mean)
        squared_diff = multiply(diff, diff)  # Using multiply instead of power for decimals
        squared_diff_sum = add(squared_diff_sum, squared_diff)
    
    # Return average of squared differences
    return divide(squared_diff_sum, len(numbers))


def standard_deviation(numbers):
    """
    Calculate the standard deviation of a dataset.
    Uses variance from this module.
    Standard deviation = square root of variance.
    
    Args:
        numbers: List of numbers
    
    Returns:
        The standard deviation of the numbers
    
    Raises:
        ValueError: If the list is empty
    
    Examples:
        >>> standard_deviation([1, 2, 3, 4, 5])
        1.4142135623730951
    """
    var = variance(numbers)
    # Calculate square root manually
    return var ** 0.5


def median(numbers):
    """
    Calculate the median of a dataset.
    Uses average from calculator module for even-length lists.
    
    Args:
        numbers: List of numbers
    
    Returns:
        The median of the numbers
    
    Raises:
        ValueError: If the list is empty
    
    Examples:
        >>> median([1, 2, 3, 4, 5])
        3
        >>> median([1, 2, 3, 4])
        2.5
    """
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 1:
        # Odd number of elements - return middle element
        return sorted_numbers[n // 2]
    else:
        # Even number of elements - return average of two middle elements
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return average([mid1, mid2])


def range_stat(numbers):
    """
    Calculate the range (difference between max and min) of a dataset.
    Uses subtract from basic_operations.
    
    Args:
        numbers: List of numbers
    
    Returns:
        The range of the numbers
    
    Raises:
        ValueError: If the list is empty
    
    Examples:
        >>> range_stat([1, 2, 3, 4, 5])
        4
        >>> range_stat([10, 50, 30])
        40
    """
    if not numbers:
        raise ValueError("Cannot calculate range of empty list")
    
    return subtract(max(numbers), min(numbers))


def coefficient_of_variation(numbers):
    """
    Calculate the coefficient of variation (CV) of a dataset.
    CV = (standard_deviation / mean) * 100
    Uses standard_deviation and mean from this module, multiply from basic_operations.
    
    Args:
        numbers: List of numbers
    
    Returns:
        The coefficient of variation as a percentage
    
    Raises:
        ValueError: If the list is empty or mean is zero
    
    Examples:
        >>> round(coefficient_of_variation([2, 4, 6, 8]), 2)
        44.72
    """
    if not numbers:
        raise ValueError("Cannot calculate CV of empty list")
    
    data_mean = mean(numbers)
    if data_mean == 0:
        raise ValueError("Cannot calculate CV when mean is zero")
    
    std_dev = standard_deviation(numbers)
    cv = divide(std_dev, data_mean)
    return multiply(cv, 100)
