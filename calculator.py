"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.

"""

from arithmetic import *


while True:
    user_input = raw_input(">> ")
    tokens = user_input.split(" ")
    if tokens[0] == 'q':
        break
    elif tokens[0] == "+":
        result = add(int(tokens[1]), int(tokens[2]))
        print result
    elif tokens[0] == "-":
        result = subtract(int(tokens[1]), int(tokens[2]))
        print result
    elif tokens[0] == "*":
        result = multiply(int(tokens[1]), int(tokens[2]))
        print result
    elif tokens[0] == "/":
        result = divide(tokens[1], tokens[2])
        print result
    elif tokens[0] == "square":
        result = square(int(tokens[1]))
        print result
    elif tokens[0] == "cube":
        result = cube(int(tokens[1]))
        print result
    elif tokens[0] == "pow":
        result = power(int(tokens[1]), int(tokens[2]))
        print result
    elif tokens[0] == "mod":
        result = mod(int(tokens[1]), int(tokens[2]))
        print result
