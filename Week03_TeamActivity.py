import math
import time

#Square — length of a side squared. = l ** 2
#Rectangle — length multiplied by the width. = l * w
#Circle— The area is Pi (you can use 3.14) multiplied by the radius squared. = (Pi * (r **2))
#Triangle - b . h / 2
#Sphere - 4. p. r³/3

print('-' * 40)
print("""Shapes:
[1] Square
[2] Rectangle
[3] Circle
[4] Triangle
[5] All-in-one""")
print('-' * 40)
1
user = int(input("What shape would you like to calculate the area? "))

time.sleep(1)

#answer = input("Would you like to calculate the area of another shape? (y/n)").lower().strip()

if user == 1:
    square = float(input('What is the length of a side of the square? '))
    math_square = (square ** 2)
    print('The area of the square of the length side of {} would be: {}cm²'.format(square, math_square))
    print('The area of the square of the length side of {} would be: {}m²'.format(square, math_square / 1000))
elif user == 2:
    length_rectangle = float(input('What is the length of the rectangle? '))
    width_rectangle = float(input('What is the width of the rectangle? '))
    math_rectangle = (length_rectangle * width_rectangle)
    print('The area of a rectangle with length size of {} and width size of {} is: {}'.format(length_rectangle, width_rectangle, math_rectangle))
elif user == 3:
    circle = float(input('What is the radius of the circle? '))
    PI = math.pi
    math_circle = (PI * (circle ** 2)) 
    print('The area of a circle with radius {} is: {}'.format(circle, math_circle))
elif user == 4:
    triangle_base = float(input('What is the length of the base of the triangle? '))
    triangle_height = float(input('What is the length of the height of the triangle? '))
    math_triangle = ((triangle_base * triangle_height)/ 2)
    print('The are of a triangle with base {} and height {} is: {}'.format(triangle_base, triangle_height, math_triangle))
elif user == 5:
    general = float(input("What's the length value? "))
    math_square = (general ** 2)
    PI = math.pi
    math_circle = (PI * (general ** 2)) 
    math_sphere = ((4 * PI * (general ** 3)) / 3)
    print('The area of the square of the length side of {} would be: {}cm²'.format(general, math_square))
    print('The area of a circle with radius {} is: {:.2f}'.format(general, math_circle))
    print('The volume of a cube with the length size of {} is: {}'.format(general, general ** 3))
    print('The volume of a sphere with the radius of {} is: {:.2f}'.format(general, math_sphere))
