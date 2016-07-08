"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.

"""

from arithmetic import *


while True:
    user_input = raw_input(">> ")
    tokens = user_input.split(" ")
    action = tokens[0]

    if len(tokens) == 3:
        num1 = tokens[1]
        num2 = tokens[2]
    else:
        num1 = tokens[1]
        num2 = 0

    if action == 'q':
        break
    elif action == "/":
        result = divide(num1, num2)
    else:
        num1 = int(num1)
        num2 = int(num2)
        if action == "+":
            result = add(num1, num2)
        elif action == "-":
            result = subtract(num1, num2)
        elif action == "*":
            result = multiply(num1, num2)
        elif action == "square":
            result = square(num1)
        elif action == "cube":
            result = cube(num1)
        elif action == "pow":
            result = power(num1, num2)
        elif action == "mod":
            result = mod(num1, num2)
    print result


