import math

def sqrt(x):
    """
    Calculate the square root of a given number.
    
    Args:
        x (int/float): The number to find the square root of
        
    Returns:
        float: The square root of x
        
    Example:
        >>> sqrt(16)
        4.0
    """
    return math.sqrt(x)

def square(x):
    """
    Calculate the square of a given number.
    
    Args:
        x (int/float): The number to square
        
    Returns:
        int/float: x raised to the power of 2
        
    Example:
        >>> square(4)
        16
    """
    return x**2

def increment(x):
    """
    Increment a number by 1.
    
    Args:
        x (int/float): The number to increment
        
    Returns:
        int/float: x increased by 1
        
    Example:
        >>> increment(5)
        6
    """
    return x + 1

def decrement(x):
    """
    Decrement a number by 1.
    
    Args:
        x (int/float): The number to decrement
        
    Returns:
        int/float: x decreased by 1
        
    Example:
        >>> decrement(5)
        4
    """
    return x - 1
