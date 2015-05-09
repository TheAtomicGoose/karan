"""
Written by Jesse Evers

This program calculates the monthly payments on a mortgage over a user-entered term 
at an interest rate given by the user. The user can also enter the compounding interval.

It can also calculate the maximum loan that can be taken, given monthly payment, interest
rate, and mortgage period.
"""

def typeOfCalculator():

    yesOrNo = input("Would you like to calculate monthly cost or maximum loan? ")
    costNotMax = False

    if yesOrNo.find("month") != -1 or yesOrNo.find("cost") != -1:
        costNotMax = True

    if costNotMax:
        monthlyCost()
    else:
        maxLoan()

def monthlyCost():
    amount = float(input("Enter the mortgage amount: $"))
    interestRate = float(input("Enter the interest rate in decimal form: "))
    monthlyInterest = interestRate / 12
    period = int(input("Enter the mortgage period, rounded to the nearest year: ")) * 12

    monthly = (amount * monthlyInterest * (1 + monthlyInterest) ** period) / (((1 + monthlyInterest) ** period) - 1)

    amountString = str.format('{0:.2f}', amount)
    monthlyString = str.format('{0:.2f}', monthly)

    print("Your monthly payment on a {0} year, ${1} loan at {2}% interest will be ${4}.".format(period / 12, amountString, interestRate * 100, compound, monthlyString))

def maxLoan():
    monthly = float(input("Enter your preferred monthly payment: $"))
    interestRate = float(input("Enter the interest rate in decimal form: "))
    monthlyInterest = interestRate / 12
    period = float(input("Enter the period of the loan in years: ")) * 12

    maxLoan = (monthly * (1 - (1 + monthlyInterest) ** (-1.0 * period))) / monthlyInterest;

    monthlyString = str.format('{0:.2f}', monthly)
    maxLoanString = str.format('{0:.2f}', maxLoan)

    print("The maximum loan that you could take out at ${0}/month at {1}% interest, over a period of {2} years, is ${3}.".format(monthlyString, interestRate * 100, period / 12, maxLoanString))


typeOfCalculator()