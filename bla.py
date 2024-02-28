from enum import Enum

class Circle(Enum):
    INNER = 0
    MIDDLE = 1
    OUTER = 2


a = Circle(1)
b = 3
print (a.value+b)
print(a)