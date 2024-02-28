from enum import Enum


class Circle(Enum):
    INNER = 0
    MIDD = 1
    OUTER = 2

class Angle(Enum):
    NORTH = 0
    NORTHEAST = 1
    EAST = 2
    SOUTHEAST = 3
    SOUTH = 4
    SOUTHWEST = 5
    WEST = 6
    NORTHWEST = 7


class VerticalCoordinate(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6


class HorizontalCoordinate(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6

class field:
    def __init__(self, circle : Circle, angle : Angle) -> None:
        self.circle = circle
        self.angle = angle

    def isAdjacentField(self,other : 'field') -> bool:
        if self.circle == other.circle:
            if abs(self.angle - other.angle) == 1 or abs(self.angle - other.angle) == 7:
                return True
        if self.angle in [0, 2, 4, 6]:
            if self.angle == other.angle:
                if abs(self.circle-other.circle) == 1:
                    return True
        return False
            
        







