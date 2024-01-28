#This function asks the user for a radius, and uses it as an argument to calculate both the area and perimeter of the circle.   



import math

user_radius = float(input("Enter radius of circle: "))

class circle():
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius**2)
    def perimeter(self):
        return 2 * math.pi * self.radius
 

obj=circle(user_radius)
print("Area of circle:",round(obj.area(),2))
print("Perimeter of circle:",round(obj.perimeter(),2))
