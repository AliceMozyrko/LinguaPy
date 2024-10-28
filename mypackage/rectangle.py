import math

def rectangle_area(length, width):
    area = length * width
    return round(area, 2)

def rectangle_perimeter(length, width):
    perimeter = 2 * (length + width)
    return round(perimeter, 2)

def rectangle_diagonal(length, width):
    diagonal = math.sqrt(length**2 + width**2)
    return round(diagonal, 2)

def is_rectangle(angle1, angle2, angle3, angle4):
    if angle1 == angle2 == angle3 == angle4 == 90:
        return True
    return False

