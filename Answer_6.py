# Create a return function that takes the radius and height of a cylinder and return the total surface area.

import math

def surface_area(radius, height):
    total_surface_area = 2 * math.pi * radius * (radius + height)
    return  total_surface_area

radius = float(input("Enter the radius of cylinder: "))
height = float(input("Enter the height of cylinder: "))

total_surface_area = surface_area(radius, height)
print(f"Total surface area of cylinder with radius {radius} and height {height} is {total_surface_area:.3f}")


"""Output:
Enter the radius of cylinder: 12.5
Enter the height of cylinder: 63.47
Total surface area of cylinder with radius 12.5 and height 63.47 is 5966.670"""