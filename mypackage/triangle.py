import math

def triangle_area(leg1, leg2):
  area = 0.5 * leg1 * leg2
  return round(area, 2)

def find_hypotenuse(leg1, leg2):
  sqrt_legs_sum = (leg1 ** 2) + (leg2 ** 2)
  hypotenuse = math.sqrt(sqrt_legs_sum)
  return round(hypotenuse, 2) 

def altitude_to_hypotenuse(leg1, leg2):
  hypotenuse = find_hypotenuse(2, 5)
  altitude = ((leg1 * leg2) / hypotenuse)
  return round(altitude, 2)

def triangle_circumradius():
  hypotenuse = find_hypotenuse(2, 5)
  cirradius = hypotenuse / 2
  return round(cirradius, 2)

def triangle_inradius(leg1, leg2):
  hypotenuse = find_hypotenuse(leg1, leg2)
  legs_sum = leg1 + leg2
  inradius = (legs_sum - hypotenuse) / 2
  return round(inradius, 2)
