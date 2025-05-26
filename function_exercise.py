""" 1.Write a function called calculate_area that takes base and height
as an input and returns and area of a triangle. Equation of an area of a triangle is,"""

def calculate_area(a,b):
    area = (1 / 2) * a * b
    return area

base=int(input("Enter the base: "))
height=int(input("Enter the height: "))
area = calculate_area(base,height)
print("Area of the triangle is ",area)

"""2.Modify above function to take third parameter shape type. It can be either "triangle" or
"rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,"""

def calculate_area(a,b,c="triangle"):
    if(c=="rectangle"):
        area = (a * b)
        return area
    if(c=="triangle"):
        area = (1 / 2) * a * b
        return area



area = calculate_area(2,5,"rectangle")
print(f"Area of the rectangle is {area} ")

area = calculate_area(2,5)
print(f"Area of the triangle is {area} ")


"""3.Write a function called print_pattern that takes integer number as an
argument and prints following pattern if input number is 3,"""

def print_pattern(n):
    for i in range(n+1):
        print(i*"*")

print_pattern(3)









