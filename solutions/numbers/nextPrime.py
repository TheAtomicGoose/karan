"""
Written by Jesse Evers
Completed on 05-03-2015

This program keeps finding the next prime number (starting at 2)
until the user stops asking for the next one.
"""

from math import sqrt


# Finds the numth prime
def nextPrime():
    numPrimes = 1
    currentPrime = 2
    currentNum = 3

    print("Prime #" + str(numPrimes) + ": " + str(currentPrime))
    cont = input("Would you like to see the next prime? [y/n] ")

    while cont.lower() == "y":

        if isPrime(currentNum):
            numPrimes += 1
            currentPrime = currentNum
            currentNum += 2
            print("Prime #" + str(numPrimes) + ": " + str(currentPrime))
            cont = input("Would you like to see the next prime? [y/n] ")
        else:
            currentNum += 2

    print("See you next time!")

# Returns true if num is prime, false otherwise
def isPrime(num):
    prime = True

    for x in range(2, num):
        if num % x == 0:
            prime = False

    return prime

nextPrime()