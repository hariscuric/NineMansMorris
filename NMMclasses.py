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

class possibleActions(Enum):
    ADDSTONE = 0
    MOVESTONE = 1
    JUMPSTONE = 2
    EATSTONE = 3




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
    

        
    
class board:
    def __init__(self) -> None:
        self.fields = []
        for i in Circle:
            for j in Angle:
                self.fields.append(field(i,j))

        self.message = ""
        #list of 16 possible mills: 3 indexes represent field indexes from self.fields:
        self.possibleMillIndexes = [[23,16,17],[17,18,19],[19,20,21],[21,22,23],[15,8,9],[9,10,11],[11,12,13],
                              [13,14,15],[7,0,1],[1,2,3],[3,4,5],[5,6,7],[0,8,16],[2,10,18],[4,12,20],[6,14,22]]

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
    
    def removeWhite(self, i, j) -> bool:
        if self.fields[i*8 + j].occupancy == fieldOccupancy(0) or self.fields[i*8 + j].occupancy == fieldOccupancy(2):
            self.message = "Field empty or black, couldn't remove white"
            return False

        self.fields[i*8 + j].occupancy = fieldOccupancy(0)
        return True
    
    def removeBlack(self, i, j) -> bool:
        if self.fields[i*8 + j].occupancy == fieldOccupancy(0) or self.fields[i*8 + j].occupancy == fieldOccupancy(1):
            self.message = "Field empty or white, couldn't remove black"
            return False

        self.fields[i*8 + j].occupancy = fieldOccupancy(0)
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
    
    def WhiteMills(self):
        #returns list of 16 booleans for existenace of 16 mills form self.possibleMillIndexes
        boolList = []
        for i in self.possibleMillIndexes:
            bool = True
            for j in range(3):
                if not self.fields[i[j]].occupancy.name == "WHITE":
                    bool = False
            boolList.append(bool)
        return boolList
    
    def BlackMills(self):
        #returns list of 16 booleans for existenace of 16 mills form self.possibleMillIndexes
        boolList = []
        for i in self.possibleMillIndexes:
            bool = True
            for j in range(3):
                if not self.fields[i[j]].occupancy.name == "BLACK":
                    bool = False
            boolList.append(bool)
        return boolList
    
    def WhiteCount(self) -> int:
        m = 0
        for i in self.fields:
            if i.occupancy.name == "WHITE":
                m = m+1
        return m
    
    def BlackCount(self) -> int:
        m = 0
        for i in self.fields:
            if i.occupancy.name == "BLACK":
                m = m+1
        return m








class game:
    def __init__(self) -> None:
        self.board = board()
        self.stage = gameStage(0)
        self.initialStageCounter = 9
        self.turn = gameTurn(0)
        self.action = possibleActions(0)
        self.CurrentWhiteMills = self.board.WhiteMills()
        self.CurrentBlackMills = self.board.BlackMills()
        self.DoubleMill = False
        self.message = "Initial stage, white to add stone."


    def progressGame(self,field1 : field, field2=field(Circle(0),Angle(0))) -> bool:
        a = self.CurrentWhiteMills
        b = self.CurrentBlackMills

        if self.stage.name == "FIRSTSTAGE":
            if self.turn.name == "WHITETURN":
                if self.action.name == "ADDSTONE":
                    bool = self.board.addWhite(field1.circle.value, field1.angle.value)
                    if bool == True:
                        self.CurrentWhiteMills = self.board.WhiteMills()
                        m = 0
                        for i in range(16):
                            if self.CurrentWhiteMills[i] == True and a[i] == False:
                                m = m+1
                        if m > 0:
                            self.action = possibleActions(3)
                        if m == 2:
                            self.DoubleMill = True
                        if m == 0:
                            self.turn = gameTurn(1)
                        return bool
                    return bool
                if self.action.name == "EATSTONE":
                    bool = self.board.removeBlack(field1.circle.value, field1.angle.value)
                    if bool == True:
                        if self.DoubleMill == True:
                            self.DoubleMill = False
                            return bool
                        self.turn = gameTurn(1)
                        self.action = possibleActions(0)
                        return bool
                    return bool
            if self.turn.name == "BLACKTURN":
                if self.action.name == "ADDSTONE":
                    bool = self.board.addBlack(field1.circle.value, field1.angle.value)
                    if bool == True:
                        self.initialStageCounter = self.initialStageCounter - 1
                        if self.initialStageCounter == 0:
                            self.stage = gameStage(1)
                            self.action = possibleActions(1)
                        self.CurrentBlackMills = self.board.BlackMills()
                        m = 0
                        for i in range(16):
                            if self.CurrentBlackMills[i] == True and b[i] == False:
                                m = m+1
                        if m > 0:
                            self.action = possibleActions(3)
                        if m == 2:
                            self.DoubleMill = True
                        if m == 0:
                            self.turn = gameTurn(0)
                        return bool
                    return bool
                if self.action.name == "EATSTONE":
                    bool = self.board.removeWhite(field1.circle.value, field1.angle.value)
                    if bool == True:
                        if self.DoubleMill == True:
                            self.DoubleMill = False
                            return bool
                        self.turn = gameTurn(0)
                        self.action = possibleActions(0)
                        return bool
                    return bool
                
        if self.stage.name == "SECONDSTAGE":
            if self.turn.name == "WHITETURN":
                if self.action.name == "MOVESTONE":
                    bool = self.board.moveWhite(field1.circle.value, field1.angle.value,field2.circle.value, field2.angle.value)
                    if bool == True:
                        self.CurrentWhiteMills = self.board.WhiteMills()
                        m = 0
                        for i in range(16):
                            if self.CurrentWhiteMills[i] == True and a[i] == False:
                                m = m+1
                        if m > 0:
                            self.action = possibleActions(3)
                        if m == 2:
                            self.DoubleMill = True
                        if m == 0:
                            self.turn = gameTurn(1)
                        return bool
                    return bool
                if self.action.name == "EATSTONE":
                    bool = self.board.removeBlack(field1.circle.value, field1.angle.value)
                    if bool == True:
                        if self.DoubleMill == True:
                            self.DoubleMill = False
                            return bool
                        if self.board.BlackCount()<3:
                            self.stage = gameStage(2)
                        self.turn = gameTurn(1)
                        self.action = possibleActions(1)
                        return bool
                    return bool
                        



                







        return True

        

            
        







