"""
Written by Jesse Evers
Completed on 05-03-2015

This program finds the nth Fibonacci number, assuming the 
first two Fibonacci numbers are 0 and 1.
"""

def nthFib(num):
	first = 0
	second = 1
	count = 2

	if num == 1:
		return first
	elif num == 2:
		return second

	while count <= num:
		nextNum = first + second
		count += 1
		temp = first
		first = nextNum
		second = temp

	return nextNum

print(nthFib(13))