def add(num_list):
    """Return the sum of list of numbers"""
    results = 0
    for number in num_list:
        results = results + float(number)
    return results

def subtract(num_list):
    """Return the num1 minus num2."""

    results = float(num_list[0])
    for i in range(1,len(num_list)):
        results = results - float(num_list[i])
    return results

def multiply(num1, num2):
    """Return num1 multiplied by num2."""

    return num1 * num2

def divide(num1, num2):
    """Return num1 divided by num2."""

    return float(num1) / float(num2)

def square(num1):
    """Return square root."""

    return num1**2

def cube(num1):
    """Return cube root."""

    return num1**3

def power(num1, num2):
    """Return num1 raised to the power of num2."""

    return num1**num2

def mod(num1, num2):
    """Return the remainder of num1 divided by num2."""

    return num1 % num2
