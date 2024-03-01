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

class gameStage(Enum):
    FIRSTSTAGE = 0
    SECONDSTAGE = 1
    FINALSTAGE = 2

class gameTurn(Enum):
    WHITETURN = 0
    BLACKTURN = 1
    WHITEEATBLACK = 3
    BLACKEATWHITE = 4



class fieldOccupancy(Enum):
    EMPTY = 0
    WHITE = 1
    BLACK = 2

class field:
    def __init__(self, circle : Circle, angle : Angle) -> None:
        self.circle = circle
        self.angle = angle
        self.occupancy = fieldOccupancy(0)

    def isAdjacentField(self,other : 'field') -> bool:
        if self.circle == other.circle:
            if abs(self.angle.value - other.angle.value) == 1 or abs(self.angle.value - other.angle.value) == 7:
                return True
        if self.angle.name in ['NORTH', 'EAST', 'SOUTH', 'WEST']:
            if self.angle == other.angle:
                if abs(self.circle.value-other.circle.value) == 1:
                    return True
        return False
    
    def isMill(self, other1 : 'field', other2 : 'field') -> bool:
        sameAngles = (self.angle == other1.angle and self.angle == other2.angle)
        sameCircles = (self.circle == other1.circle and self.circle == other2.circle)
        sameAngle01 = self.angle == other1.angle
        sameAngle02 = self.angle == other2.angle
        sameAngle12 = other1.angle == other2.angle
        sameCircle01 = self.circle == other1.circle
        sameCircle02 = self.circle == other2.circle
        sameCircle12 = other1.circle == other2.circle
        if (sameAngle01 and sameCircle01) or (sameAngle02 and sameCircle02) or (sameAngle12 and sameCircle12):
            return False 
        if sameAngles:
            if self.angle in [0,2,4,6]:
                return True
        if sameCircles:
            a = self.angle in [7,0,1] and other1.angle in [7,0,1] and other2.angle in [7,0,1]
            b = self.angle in [1,2,3] and other1.angle in [1,2,3] and other2.angle in [1,2,3]
            c = self.angle in [3,4,5] and other1.angle in [3,4,5] and other2.angle in [3,4,5]
            d = self.angle in [5,6,7] and other1.angle in [5,6,7] and other2.angle in [5,6,7]
            if a or b or c or d:
                return True
        return False

        
    
class board:
    def __init__(self) -> None:
        self.fields = []
        for i in Circle:
            for j in Angle:
                self.fields.append(field(i,j))

        self.message = ""

    def addWhite(self, i, j) -> bool:
        if self.fields[i*8 + j].occupancy == fieldOccupancy(1) or self.fields[i*8 + j].occupancy == fieldOccupancy(2):
            self.message = "Field occupied, couldn't add white"
            return False

        self.fields[i*8 + j].occupancy = fieldOccupancy(1)
        return True

    def addBlack(self, i, j) -> bool:
        if self.fields[i*8 + j].occupancy == fieldOccupancy(1) or self.fields[i*8 + j].occupancy == fieldOccupancy(2):
            self.message = "Field occupied, couldn't add black"
            return False

        self.fields[i*8 + j].occupancy = fieldOccupancy(2)
        return True
    

    def moveWhite(self, i1,j1,i2,j2) -> bool:
        a = self.fields[i1*8+j1].occupancy == fieldOccupancy(1)
        b = self.fields[i2*8+j2].occupancy == fieldOccupancy(0)
        if not (a and b):
            self.message = "Unsuccessful white move, start field not white or destination not empty"
            return False
        if not field.isAdjacentField(self.fields[i1*8+j1], self.fields[i2*8+j2]):
            self.message = "Unsuccessful white move, start and destination fields are not adjacent"
            return False
        self.fields[i1*8+j1].occupancy = fieldOccupancy(0)
        self.fields[i2*8+j2].occupancy = fieldOccupancy(1)
        return True
    
    def moveBlack(self, i1,j1,i2,j2) -> bool:
        a = self.fields[i1*8+j1].occupancy == fieldOccupancy(2)
        b = self.fields[i2*8+j2].occupancy == fieldOccupancy(0)
        if not (a and b):
            self.message = "Unsuccessful black move, start field not black or destination not empty"
            return False
        if not field.isAdjacentField(self.fields[i1*8+j1], self.fields[i2*8+j2]):
            self.message = "Unsuccessful black move, start and destination fields are not adjacent"
            return False
        self.fields[i1*8+j1].occupancy = fieldOccupancy(0)
        self.fields[i2*8+j2].occupancy = fieldOccupancy(2)
        return True
    
    def jumpWhite(self, i1,j1,i2,j2) -> bool:
        a = self.fields[i1*8+j1].occupancy == fieldOccupancy(1)
        b = self.fields[i2*8+j2].occupancy == fieldOccupancy(0)
        if not (a and b):
            self.message = "Unsuccessful white jump, start field not white or destination not empty"
            return False
        self.fields[i1*8+j1].occupancy = fieldOccupancy(0)
        self.fields[i2*8+j2].occupancy = fieldOccupancy(1)
        return True
    
    def jumpBlack(self, i1,j1,i2,j2) -> bool:
        a = self.fields[i1*8+j1].occupancy == fieldOccupancy(2)
        b = self.fields[i2*8+j2].occupancy == fieldOccupancy(0)
        if not (a and b):
            self.message = "Unsuccessful black jump, start field not black or destination not empty"
            return False
        self.fields[i1*8+j1].occupancy = fieldOccupancy(0)
        self.fields[i2*8+j2].occupancy = fieldOccupancy(2)
        return True





class game:
    def __init__(self) -> None:
        self.board = board()
        self.stage = gameStage(0)
        self.turn = gameTurn(0)
        self.message = "Initial stage, white to play"

    def progressGame(self) -> bool:
        return True

        

            
        







