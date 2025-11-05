7# import math library to be used
import math

# Area of a circle
radius = int(input("Enter the radius of the circle: "))
area_circle = math.pi * radius ** 2
print(f"The area of the circle with radius {radius} is: {area_circle}")

# Area of a rectangle
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area_rectangle = length * width
print(f"The area of the rectangle with length {length} and width {width} is: {area_rectangle}")

# Area of a triangle
base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
area_triangle = 0.5 * base * height
print(f"The area of the triangle with base {base} and height {height} is: {area_triangle}")

# Area of a square
side = int(input("Enter the side length of the square: "))
area_square = side ** 2
print(f"The area of the square with side length {side} is: {area_square}")

# Area of a trapezoid
base1 = int(input("Enter the length of the first base of the trapezoid: "))
base2 = int(input("Enter the length of the second base of the trapezoid: "))
height_trapezoid = int(input("Enter the height of the trapezoid: "))
area_trapezoid = 0.5 * (base1 + base2) * height_trapezoid
print(f"The area of the trapezoid with bases {base1}, {base2} and height {height_trapezoid} is: {area_trapezoid}")