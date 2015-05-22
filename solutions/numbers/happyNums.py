"""
Written by Jesse Evers

This program finds the first n happy numbers.
Happy numbers are numbers who, when you replace them with the sum of the
squares of their digits, and continue to do that, end up being one.
"""

# Finds the first x happy numbres
def findHappyNums(x):

    i = 0
    happyNums = []
    currentNum = 1

    # While fewer than x happy numbers have been found
    while i < x:
        
        copyNum = currentNum

        for y in range(20):
            copyNum = happyIterate(copyNum)

        if copyNum == 1:
            happyNums.append(currentNum)
            i += 1

        currentNum += 1

    return happyNums


# Finds the sum of squares of the digits of num
# E.g., 81 -> 8^2 + 1^2 -> 65
def happyIterate(num):

    numDigits = len(str(num))
    sumSquares = 0

    # For each digit in num, square it and add it to sumSquares
    for x in range(numDigits):
        sumSquares += (num % 10) ** 2
        num //= 10

    return sumSquares