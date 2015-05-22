"""
Written by Jesse Evers

Finds the factorial of a number.
"""

def factorial(num):

    if num > 1:
        return num * factorial(num - 1)
    return num


print(factorial(10))