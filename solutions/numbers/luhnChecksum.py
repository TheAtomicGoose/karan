"""
Written by Jesse Evers

This program computes the Luhn checksum algorithm on a number entered
by the user.
"""

def luhn(num):

    numStr = ""
    numCopy = num

    everyOther = False
    for x in range(len(str(num)), 0, -1):

        if everyOther:
            numStr = str((numCopy % 10) * 2) + numStr
        else:
            numStr = str(numCopy % 10) + numStr

        everyOther = not everyOther

        numCopy //= 10
    modNum = int(numStr)

    digitSum = 0

    while modNum > 0:
        digitSum += modNum % 10
        modNum //= 10

    if digitSum % 10 == 0:
        print("Checksum passed!")
    else:
        print("Checksum failed.")


luhn(79927398713)