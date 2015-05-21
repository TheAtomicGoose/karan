"""
Written by Jesse Evers

Finds the distance between two cities.
Allows the user to specify whether they want miles or kilometers.
"""

import math

# Gets the latitude and longitude of the cities
def cities():

    city1 = input("Where would you like to start? ")
    city2 = input("Where would you like to end? ")

    lat1 = float(input("Enter the latitude of " + city1 + " in decimal format (negative for south): "))
    long1 = float(input("Enter the longitude of " + city1 + " in decimal format (negative for west: "))
    lat2 = float(input("Enter the latitude of " + city2 + " in decimal format (negative for south): "))
    long2 = float(input("Enter the longitude of " + city2 + " in decimal format (negative for west): "))
    calcDistance(lat1, long1, lat2, long2)


# Finds the distance between (lat1, long1) and (lat2, long2)
def calcDistance(lat1, long1, lat2, long2):

    radius = 3963  # Radius of the earth

    # Latitude and longitude measurements in radians
    lat1Rad = math.radians(lat1)
    lat2Rad = math.radians(lat2)
    long1Rad = math.radians(long1)
    long2Rad = math.radians(long2)
    
    # This is the haversin formula for calculating distances with latitude and longitude.
    # I don't really understand it, but it uses the haversine function, which is defined later.
    # See http://en.wikipedia.org/wiki/Haversine_formula for more details.
    distance = 2 * radius * math.asin(math.sqrt(haversin(lat2Rad - lat1Rad) + math.cos(lat1Rad) * math.cos(lat2Rad) * haversin(long2Rad - long1Rad)))

    # Decides on miles or kilometers
    units = int(input("Enter 1 for miles, 2 for kilometers: "))

    if units == 2:
        distance *= 1.60934
    elif units != 1:
        print("Not a valid choice, displaying in miles...")


    print(str.format("{0:.2f}", distance))


# Defines the haversine function
def haversin(theta):

    return pow(math.sin(theta / 2), 2)