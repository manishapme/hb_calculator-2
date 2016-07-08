def add(num_list):
    """Return the sum of list of numbers"""
    results = 0
    for number in num_list:
        results = results + float(number)
    return results

def subtract(num_list):
    """Return the difference from a list of numbers."""

    results = float(num_list[0])
    for i in range(1,len(num_list)):
        results = results - float(num_list[i])
    return results

def multiply(num_list):
    """Return total from multiplying a series of numbers."""

    results = float(num_list[0])
    for i in range(1,len(num_list)):
        results = results * float(num_list[i])
    return results

def divide(num_list):
    """Return num1 divided by num2."""
    results = float(num_list[0])
    for i in range(1,len(num_list)):
        results = results / float(num_list[i])
    return results


def square(num_list):
    """Return square root."""

    return float(num_list[0])**2

def cube(num_list):
    """Return cube root."""

    return float(num_list[0])**3

def power(num_list):
    """Return num1 raised to the power of num2."""

    return float(num_list[0])**float(num_list[1])

def mod(num_list):
    """Return the remainder of num1 divided by num2."""

    return float(num_list[0]) % float(num_list[1])
