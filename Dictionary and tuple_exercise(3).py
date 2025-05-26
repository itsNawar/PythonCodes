"""Write circle_calc() function that takes radius of a circle as an input from user 
and then it calculates and returns area, circumference and diameter. You should get 
these values in your main program by calling circle_calc function and then print them"""

import math
def circle_calc(r):
    area=math.pi*r**2
    circumference=2*math.pi*r
    diameter=2*r
    return area,circumference,diameter

radius=float(input("Enter the radius of the circle:"))
area,circumference,diameter=circle_calc(radius)
print("Area:",round(area,2),"Circumference:",round(circumference,2),"Diameter:",diameter)

