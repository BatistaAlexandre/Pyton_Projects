# Area of a square
import math
s=int(input("What is the length of a side of the square ? : "))
area = s ** 2 
print("The area of area of square is: ",area)
print("")
2
# Area of a rectangle
import math
length = float(input("What is the length of rectangle? "))
width = float(input("What is the width of the rectangle? "))
area = length * width
print(f"The area of the rectangle is: {area}")
print("")

# Area of a circle
import math
radius = float(input("What is the radius of the circle? "))
area = math.pi * (radius ** 2)
print(f"The area of the circle is: {area}")
print("")


# Area of a square
import math
s=int(input("What is the length of a side of the square (in cm) ? : "))
area=s*s
print("The area of area of square is: {area} cm^2 ")
print(f"The area of the square is: {area / 10000} m^2")
print("")

# Area of a rectangle
length = float(input("What is the length of rectangle (in cm)? "))
width = float(input("What is the width of the rectangle (in cm)? "))
area = length * width
print(f"The area of the rectangle is: {area} cm^2")
print(f"The area of the rectangle is: {area / 10000} m^2")

# Area of a circle
import math
radius = float(input("What is the radius of the circle (in cm)? "))
area = math.pi * (radius ** 2)
print(f"The area of the circle is: {area} cm^2")
print(f"The area of the circle is: {area / 10000} m^2")