"""
Written by Jesse Evers


This converts between the following things.

Temperature:    Fahrenheit (F), Celsius (C), Kelvin (K)

Currency:       US Dollars ($), Pounds (£), Euros (€), Shekel (₪), Yen (¥)

Volume:         Kiloliters (kL), liters (L), milliliters (mL), 
                teaspoons (tsp), tablespoons (tbsp), fluid ounces (floz),
                cups (c), pints (pt), quarts (qt), gallons (gal)

Mass:           Tonnes (t), kilograms (kg), grams (g), milligrams (mg)

Length:         Kilometers (km), meters (m), centimeters (cm),
                millimeters (mm), miles (mi), yards (y), feet (ft), 
                inches (in)

Time:           Years (y), months (mth), days (d), hours (hr),
                minutes (min), seconds (sec)
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import lxml

def chooseType():

    print("Choose the type of measurement you would like to use.")
    print("1. Temperature")
    print("2. Currency")
    print("3. Volume")
    print("4. Mass")
    print("5. Length")
    print("6: Time")
    choice = int(input("Enter a number: "))

    if choice == 1:
        tempConverter()
    elif choice == 2:
        moneyConverter()
    elif choice == 3:
        volConverter()
    elif choice == 4:
        massConverter()
    elif choice == 5:
        lengthConverter()
    elif choice == 6:
        timeConverter()
    else:
        print("Not a valid choice.")
        chooseType()


def converter(unitString, unitArray, conversionArray):

    print("You can convert between any of the following units:")
    print(unitString)
    start = input("Enter the abbreviation of the units you're starting with: ")
    startNum = float(input("Enter the number of units to start with: "))
    end = input("Enter the abbreviation of the units you'd like to convert to: ")

    if start.upper() in unitArray and end.upper() in unitArray:
        endNum = startNum * conversionArray[unitArray.index(start.upper())]
        endNum *= (1 / conversionArray[unitArray.index(end.upper())])
        print("{0} {1} in {2} is {3}.".format(startNum, start, end, endNum))

    else:
        print("One or both of your units were not valid.")



def tempConverter():

    tempString = "Fahrenheit (F), Celsius (C), Kelvin (K)"
    tempArray = ["F", "C", "K"]
    print("You can convert between any of the following units: ")
    print(tempString)
    start = input("Enter the abbreviation of the units you're starting with: ")
    startNum = float(input("Enter the number of units to start with: "))
    end = input("Enter the abbreviation of the units you'd like to convert to: ")

    if start.upper() in tempArray and end.upper() in tempArray:

        if start.upper() == "f" and end.upper() == "c":
            endNum = (startNum - 32) * (5/9)
        elif start.upper() == "f" and end.upper() == "k":
            endNum = (5/9) * (startNum - 32) + 273
        elif start.upper() == "c" and end.upper() == "f":
            endNum = (9/5) * startNum + 32
        elif start.upper() == "c" and end.upper() == "k":
            endNum = startNum + 273
        elif start.upper() == "k" and end.upper() == "f":
            endNum = (startNum - 273) * (9/5) + 32
        elif start.upper() == "k" and end.upper() == "c":
            endNum = startNum - 273
    else:
        print("You did not enter valid units")
        return

    print("{0} degrees {1} is {2} degrees {3}.".format(startNum, start, ("%.2f" % endNum), end))


def moneyConverter():  

    moneyString = "US Dollars (USD), Pounds (GBP), Euros (EUR), Shekel (ILS), Yen (JPY)"
    moneyArray = ["USD", "GBP", "EUR", "ILS", "JPY"]
    moneyConversionArray = [1, 1.56, 1.12, .26, .0084]
    converter(moneyString, moneyArray, moneyConversionArray)


def volConverter():

    volString = "Kiloliters (kL), liters (L), milliliters (mL),\nteaspoons (tsp), tablespoons (tbsp), fluid ounces (floz),\n cups (c), pints (pts), quarts (qts), gallons (gals)"
    volArray = ["L", "KL", "ML", "TSP", "TBSP", "FLOZ", "C", "PTS", "QTS", "GALS"]
    volConversionArray = [1, 1000, .001, .0049, .0148, .2366, .4732, .9464, 3.7854]
    converter(volString, volArray, volConversionArray)


def massConverter():

    volString = "Tonnes (t), kilograms (kg), grams (g), milligrams (mg)"
    volArray = ["G", "T", "KG", "MG"]
    volConversionArray = [1, 1000000, 1000, .001]
    converter(volString, volArray, volConversionArray)


def lengthConverter():

    volString = "Kilometers (km), meters (m), centimeters (cm),\n millimeters (mm), miles (mi), yards (yds), feet (ft), \n inches (in)"
    volArray = ["M", "KM", "CM", "MM", "MI", "YDS", "FT", "IN"]
    volConversionArray = [1, 1000, .01, .001, 1609.34, .9144, .3048, .0254]
    converter(volString, volArray, volConversionArray)


def timeConverter():

    volString = "Years (yrs), months (mths), days (d), hours (hrs),\n minutes (mins), seconds (secs)"
    volArray = ["HRS", "YRS", "MTHS", "D", "MINS", "SECS"]
    volConversionArray = [1, 8766, 730, 24, .0167, .000278]
    converter(volString, volArray, volConversionArray)


chooseType()