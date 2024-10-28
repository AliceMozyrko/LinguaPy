import math

def square_area(side_length):
    area = side_length ** 2
    return round(area, 2)
print(square_area(4))

def square_perimeter(side_length):
    perimeter = 4 * side_length
    return round(perimeter, 2)

def square_diagonal(side_length):
    diagonal = side_length * math.sqrt(2)
    return round(diagonal, 2)

def square_inradius(side_length):
    radius = side_length / 2
    return round(radius, 2)

def square_circumradius(side_length):
    radius = side_length * math.sqrt(2) / 2
    return round(radius, 2)
