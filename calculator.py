"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.

"""

from arithmetic import divide, add, subtract, multiply, square, cube, power, mod


while True:
    user_input = raw_input(">> ")
    tokens = user_input.split(" ")
    action = tokens[0]
    num_list = tokens[1:]

    if action == 'q':
        break
    elif action == "+":
        result = add(num_list)
    elif action == "-":
        result = subtract(num_list)
    elif action == "*":
        result = multiply(num_list)
    elif action == "/":
        result = divide(num_list)
    elif action == "square":
        result = square(num_list)
    elif action == "cube":
        result = cube(num_list)
    elif action == "pow":
        result = power(num_list)
    elif action == "mod":
        result = mod(num_list)
    print result


