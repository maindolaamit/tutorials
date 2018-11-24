"""
    Given the List/Array of Co-Ordinates/Points, have to find out the K closest neighbours from the Origin
    The list of Co-Ordinates can be taken as input or generated randomly.
    Based on the location the distance of Point will be calculated from the Origin.

    For e.g. if we have the below list of Tuples as Input
    [(3, -3) ,(15, -10) ,(4, -1) ,(8, -13) ,(-4, -12) ,(12, -2) ,(-19, 12) ,(-13, -12) ,(-4, 18) ,(-20, 0)]
    Below is the expected output
    3 Closest Points are (4, -1),(3, -3),(12, -2)
"""
from random import randint
import math

MIN_POINT, MAX_POINT = -20, 20
ORIGIN = (0, 0)


# Function will return a cordinates(X,Y) in the form of Tuples
def get_rand_cordinate():
    return (randint(MIN_POINT, MAX_POINT), randint(MIN_POINT, MAX_POINT))


# Function to return the distance between point and the Origin
def get_distance(cordinates):
    return round(math.sqrt((cordinates[0] - ORIGIN[0]) ** 2 + (cordinates[1] - ORIGIN[1]) ** 2), 2)


# Function to print K nearest neighbours from the given list of Points
def closest(points, k):
    # Calculate the distance for each point
    points_d = [(point, get_distance(point)) for point in points]
    for i in range(len(points_d)):
        print("{:0>5.2f} - Distance from Origin for Point {}".format(points_d[i][1], points_d[i][0]))

    # Sort the results and print the closest point
    points_d.sort(key=lambda x: x[1])

    # View the Nearest K points and Distance
    print("\n{} Closest Points are {}".format(k, ','.join(map(str, [x[0] for x in points_d[0:k]]))))


# Get the List of Co-Ordinates
points = [get_rand_cordinate() for i in range(10)]

# Call the method to view results
closest(points, 3)
