"""
Written by Jesse Evers
Completed on 05-03-2015

This program can be used to find the mathematical constant else
up to n decimal places, as long as n is less than 51.
"""

import math

def eDigits(digits):
	if digits > 51:
		print("Enter a lower number, the program doesn't go that high.")
	else:
		print(str.format('{0:.' + str(digits) + 'f}', math.e))