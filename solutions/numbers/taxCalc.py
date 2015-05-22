"""
Written by Jesse Evers

This program finds the cost of something, given a price and a tax.
I think that I'm doing this challenge wrong, because it seems too easy.
"""

def tax():
    price = float(input("Enter a price: "))
    tax = float(input("Enter the tax percentage as a decimal: "))

    print("With tax, the price is $" + str.format("{0:.2f}", price * (1 + tax)))

tax()