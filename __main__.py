import math
print("WELCOME TO THE DISTANCE CALCULATOR")
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 -x1) ** 2 +(y2 - y1)** 2)
def calculate_triangle_properties(x1, y1, x2, y2, x3, y3):

    side1 = calculate_distance(x1, y1, x2, y2)
    side2 = calculate_distance(x2, y2, x3, y3)
    side3 = calculate_distance(x3, y3, x1, y1)

    perimeter = side1 + side2 + side3
    return {
        'AB': side1,
        'AC': side2,
        'BC': side3,
        'Perimeter':perimeter
    }

x1 = float(input('Enter x-coordinate for P1: '))
y1 = float(input('Enter y-coordinate for P1: '))
x2 = float(input('Enter x-coordinate for P2: '))
y2 = float(input('Enter y-coordinate for P2: '))
x3 = float(input('Enter x-coordinate for P3: '))
y3 = float(input('Enter y-coordinate for P3: '))

triangle_properties = calculate_triangle_properties(x1, y1, x1, y2, x3, y3)

for key, value in triangle_properties.items():
    print(f"{key}: {value}")
