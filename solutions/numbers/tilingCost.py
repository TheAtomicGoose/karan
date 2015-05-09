"""
Written by Jesse Evers
Completed on 05-03-2015

This program finds the cost of tiling a room of dimensions entered by the user, at
a cost per tile entered by the user. It assumes that tiles are 1 foot by 1 foot.
"""

def tilingCost():
    width = int(input("Please enter the width of the room in feet: "))
    length = int(input("Please enter the length of the room in feet: "))
    cost = float(input("Please enter the cost per tile in dollars: "))

    totalCost = width * length * cost

    widthString = str(width)
    lengthString = str(length)
    costString = str.format('{0:.2f}', cost)
    totalCostString = str.format('{0:.2f}', totalCost)

    print("The cost to tile a room of dimensions " + widthString + "x" + lengthString + " at $" + costString + " per tile is $" + totalCostString + ".")

tilingCost()