# Create a function that takes the radius and height of a cone and return the volume.

import math

def volume_cone(radius, height):
    volume_of_cone = 1/3 * math.pi * radius**2 * height
    return  volume_of_cone

radius = float(input("Enter the radius of cone: "))
height = float(input("Enter the height of cone: "))

cone_volume = volume_cone(radius, height)
print(f"Volume of cone with radius {radius} and height {height} equals {cone_volume:.3f}")


"""Output:
Enter the radius of cone: 25.69
Enter the height of cone: 46.73
Volume of cone with radius 25.69 and height 46.73 equals 32296.288"""