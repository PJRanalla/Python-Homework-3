# This function takes in user input for length and with, calculates the square footage of a home,
# and returns the result back to the user.

def homeArea(L, W):
    area = (L * W)
    return area

length = float(input("Please enter the length(in feet) of your home: "))
width = float(input("Please enter the width(in feet) of you home: "))

print(f"The square footage of your home is {homeArea(length, width)} square feet.")


# This function takes in user input to calculate the circumference of a circle

def circleCircumference(R):
    from math import pi
    circumference = 2 * pi * R
    return round(circumference, 5)

radius = float(input("Please enter the radius of the circle: "))

print(f"The circumference of the circle is {circleCircumference(radius)}")
