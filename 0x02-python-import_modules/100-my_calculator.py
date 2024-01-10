#!/usr/bin/python3
if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    from sys import argv

    num_args = len(argv)

    if num_args - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator == '+':
        print("{a} {operator} {b} = {result}".format(a=a, operator=operator, b=b, result=add(a, b)))
    elif operator == '-':
        print("{a} {operator} {b} = {result}".format(a=a, operator=operator, b=b, result=sub(a, b)))
    elif operator == '*':
        print("{a} {operator} {b} = {result}".format(a=a, operator=operator, b=b, result=mul(a, b)))
    elif operator == '/':
        if b == 0:
            print("Error: Division by zero")
            exit(1)
        print("{a} {operator} {b} = {result}".format(a=a, operator=operator, b=b, result=div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
