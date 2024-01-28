#This function calculates the hypotenuse of a triangle. 



import math

def squarefunction(length):
    square = length * length
    print("The square of a side is: ", square)
    return square

def pythagorean(aside, bside):
    Hypotenuse_squared  = aside + bside
    hypotenuse = math.sqrt(Hypotenuse_squared)
    print("The hypotenuse of you triangle is exactly:", str(hypotenuse) + "cm.")

firstside = float(input("Enter the length of the first side of your right-angled triangle (in cm): "))
secondside = float(input("Enter the length of the second side of your right-angled triangle (in cm): "))

firstsidesquared = squarefunction(firstside)
secondsidesquared = squarefunction(secondside)
pythagorean(firstsidesquared, secondsidesquared)
