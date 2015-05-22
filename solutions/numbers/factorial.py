"""
Written by Jesse Evers

Finds the factorial of a number.
"""

def factorial(num):

    # While num > 1, multiply num by num - 1
    if num > 1:
        return num * factorial(num - 1)
    return num


print(factorial(10))