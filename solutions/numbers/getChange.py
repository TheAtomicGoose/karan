"""
Written by Jesse Evers

This program finds the number of quarters, dimes, nickels, and pennies
owed, given the price of something and the amount paid.
"""

def getChange():
    price = float(input("How much is owed? $"))
    paid = float(input("How much was paid? $"))

    change = paid - price
    changeTemp = change

    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    while changeTemp - .25 >= .25:
        changeTemp -= .25
        quarters += 1

    while changeTemp - .1 >= .1:
        changeTemp -= .1
        dimes += 1

    while changeTemp - .05 >= .05:
        changeTemp -= .05
        nickels += 1

    pennies = int(changeTemp * 100 + 0.5)

    if pennies >= 5:
        while pennies >= 5:
            pennies -= 5
            nickels += 1

    if nickels >= 2:
        while nickels >= 2:
            nickels -= 2
            dimes += 1

    if dimes >= 2 and nickels >= 1:
        while dimes >= 2 and nickels >= 1:
            dimes -= 2
            nickels -= 1
            quarters += 1

    response = ""
    if paid - price < 0:
        response = "You don't need change, but you do need to pay another ${0}!".format(str.format('{0:.2f}', price - paid))
    else:
        response = "You should receive ${0}, or {1} quarters, {2} dimes, {3} nickels, and {4} pennies in change.".format(str.format('{0:.2f}', change), quarters, dimes, nickels, pennies)

    print(response)

getChange()