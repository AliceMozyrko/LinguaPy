from math import pi

def circle_area(radius: float) -> float:
    area = pi * (radius ** 2)
    return round(area, 2)

def circle_length(radius: float) -> float:
    length = 2 * pi * radius
    return round(length, 2)

def sector_area(
        central_angle: int,
        radius: int
) -> float:
    if 0 < central_angle <= 360:
        area = (central_angle / 360) * 2 * pi * radius
        result = round(area, 2)
    else:
        raise ValueError(f"Angle {central_angle} not in range from 1 to 360.")
    return result

def arc_length(
        central_angle: int,
        radius: float
) -> float:
    length = (central_angle / 360) * 2 * pi * radius
    return round(length, 2)

def is_point_inside(
        radius: float, 
        x: float, 
        y: float,
        x0: float = 0, 
        y0: float = 0
) -> bool:
    formula = ((x - x0) ** 2) + ((y - y0) ** 2)
    if formula <= radius ** 2:
        return True
    else:
        return False