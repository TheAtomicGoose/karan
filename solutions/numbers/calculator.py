"""
Written by Jesse Evers

A basic calculator.
"""

# Adds x and y
def add(x, y):
    return x + y


# Subtracts y from x
def subtract(x, y):
    return x - y


# Multiplies x by y
def multiply(x, y):
    return x * y


# Divides x by y
def divide(x, y):
    return x / y


# Raises x to the y
def exponent(x, y):
    return pow(x, y)


def calc():
    print("Welcome to Jesse's calculator!")
    while True:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter your operator: ")
        num2 = float(input("Enter the second number: "))

        return {
            '+': add(num1, num2),
            '-': subtract(num1, num2),
            '*': multiply(num1, num2),
            '/': divide(num1, num2),
            '^': exponent(num1, num2),
            '**': exponent(num1, num2),
        }[operator]

print(calc())