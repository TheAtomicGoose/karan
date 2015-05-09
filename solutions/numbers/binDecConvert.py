"""
Written by Jesse Evers

This program converts binary numbers to base 10 and vice versa.
"""

# Gets the user to choose between binary -> decimal or decimal -> binary
# "b" gets binary -> decimal, "bt" gets decimal -> binary
# Anything else gets new user input
def binOrDec():
    print("Would you like to convert binary to base 10 or base 10 to binary?")
    choice = input("Enter b for binary to base 10, bt for base 10 for binary: ")
    if choice.lower() == "b":
        binToDec();
    elif choice.lower() == "bt":
        decToBin();
    else:
        print("That was not a valid option.")
        binOrDec()


# Converts binary to base 10
def binToDec():

    binNum = int(input("Enter a number in binary: "))
    binTemp = binNum
    decNum = 0

    i = 0

    while binTemp > 0:

        # If that digit of the binary number is 1, add 2^(number of iterations) to the base 10 number
        if binTemp % 2 == 1:
            decNum += 2 ** i

        # Go to the next digit of the binary number
        binTemp = int(binTemp / 10)
        i += 1

    print("{0} in binary is {1} in base 10.".format(binNum, decNum))


# Converts base 10 to binary
def decToBin():

    decNum = int(input("Enter a number in base 10: "))
    decTemp = decNum
    binNum = 0
    largestPow = largestPowerOfTwo(decNum)

    # If decNum is a power of 2
    if largestPow == decNum:
        print("{0} in base 10 is {1} in binary.".format(decNum, 10 ** powerOfTwo(decNum)))
        return

    while decTemp > 0:

        # If the next smallest power of two is smaller than decTemp, add another 1 to the binary number
        if decTemp - largestPow >= 0:
            decTemp -= largestPow
            binNum = binNum * 10 + 1
        # Otherwise, add a 0
        else:
            binNum *= 10

        largestPow /= 2

    print("{0} in base 10 is {1} in binary.".format(decNum, binNum))


# Finds the largest power of 2 smaller than num
def largestPowerOfTwo(num):

    return 2 ** powerOfTwo(num)


# Finds the number of times 2 can be multiplied by itself and still be smaller than num
def powerOfTwo(num):

    numTemp = num
    power = 0

    while numTemp > 1:
        numTemp = int(numTemp / 2)
        power += 1

    return power