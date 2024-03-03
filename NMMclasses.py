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

class gameOutcome(Enum):
    GAMEONGOING = 0
    WHITEWINS = 1
    BLACKWINS = 2




class fieldOccupancy(Enum):
    EMPTY = 0
    WHITE = 1
    BLACK = 2

class field:
    def __init__(self, circle : Circle, angle : Angle) -> None:
        self.circle = circle
        self.angle = angle
        self.occupancy = fieldOccupancy.EMPTY

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
        if self.fields[i*8 + j].occupancy == fieldOccupancy.WHITE or self.fields[i*8 + j].occupancy == fieldOccupancy.BLACK:
            self.message = "Field occupied, couldn't add white"
            return False

        self.fields[i*8 + j].occupancy = fieldOccupancy.WHITE
        return True

    def addBlack(self, i, j) -> bool:
        if self.fields[i*8 + j].occupancy == fieldOccupancy.WHITE or self.fields[i*8 + j].occupancy == fieldOccupancy.BLACK:
            self.message = "Field occupied, couldn't add black"
            return False

        self.fields[i*8 + j].occupancy = fieldOccupancy.BLACK
        return True
    
    def removeWhite(self, i, j) -> bool:
        if self.fields[i*8 + j].occupancy == fieldOccupancy.EMPTY or self.fields[i*8 + j].occupancy == fieldOccupancy.BLACK:
            self.message = "Field empty or black, couldn't remove white"
            return False
        
        #check if all white stones are in mills:
        a = self.WhiteMills()
        millIndexes = []
        for m in range(16):
            if a[m] == True:
                mill = self.possibleMillIndexes[m]
                for n in mill:
                    if not n in millIndexes:
                        millIndexes.append(n)

        if not i*8+j in millIndexes:
            self.fields[i*8 + j].occupancy = fieldOccupancy.EMPTY
            return True
        else:
            #checking if all the white stones are in mills:
            for m in range(24):
                if self.fields[m].occupancy.name == "WHITE" and (not m in millIndexes):
                    self.message = "Cannot remove white stone within a mill when other out-of-mill white stones are available"
                    return False
            self.fields[i*8 + j].occupancy = fieldOccupancy.EMPTY
            return True
            

    
    def removeBlack(self, i, j) -> bool:
        if self.fields[i*8 + j].occupancy == fieldOccupancy.EMPTY or self.fields[i*8 + j].occupancy == fieldOccupancy.WHITE:
            self.message = "Field empty or white, couldn't remove black"
            return False
        
        #check if all black stones are in mills:
        a = self.BlackMills()
        millIndexes = []
        for m in range(16):
            if a[m] == True:
                mill = self.possibleMillIndexes[m]
                for n in mill:
                    if not n in millIndexes:
                        millIndexes.append(n)

        if not i*8+j in millIndexes:
            self.fields[i*8 + j].occupancy = fieldOccupancy.EMPTY
            return True
        else:
            #checking if all the black stones are in mills:
            for m in range(24):
                if self.fields[m].occupancy.name == "BLACK" and (not m in millIndexes):
                    self.message = "Cannot remove black stone within a mill when other out-of-mill black stones are available"
                    return False
            self.fields[i*8 + j].occupancy = fieldOccupancy.EMPTY
            return True

    

    def moveWhite(self, i1,j1,i2,j2) -> bool:
        a = self.fields[i1*8+j1].occupancy == fieldOccupancy.WHITE
        b = self.fields[i2*8+j2].occupancy == fieldOccupancy.EMPTY
        if not (a and b):
            self.message = "Unsuccessful white move, start field not white or destination not empty"
            return False
        if not field.isAdjacentField(self.fields[i1*8+j1], self.fields[i2*8+j2]):
            self.message = "Unsuccessful white move, start and destination fields are not adjacent"
            return False
        self.fields[i1*8+j1].occupancy = fieldOccupancy.EMPTY
        self.fields[i2*8+j2].occupancy = fieldOccupancy.WHITE
        return True
    
    def moveBlack(self, i1,j1,i2,j2) -> bool:
        a = self.fields[i1*8+j1].occupancy == fieldOccupancy.BLACK
        b = self.fields[i2*8+j2].occupancy == fieldOccupancy.EMPTY
        if not (a and b):
            self.message = "Unsuccessful black move, start field not black or destination not empty"
            return False
        if not field.isAdjacentField(self.fields[i1*8+j1], self.fields[i2*8+j2]):
            self.message = "Unsuccessful black move, start and destination fields are not adjacent"
            return False
        self.fields[i1*8+j1].occupancy = fieldOccupancy.EMPTY
        self.fields[i2*8+j2].occupancy = fieldOccupancy.BLACK
        return True
    
    def jumpWhite(self, i1,j1,i2,j2) -> bool:
        a = self.fields[i1*8+j1].occupancy == fieldOccupancy.WHITE
        b = self.fields[i2*8+j2].occupancy == fieldOccupancy.EMPTY
        if not (a and b):
            self.message = "Unsuccessful white jump, start field not white or destination not empty"
            return False
        self.fields[i1*8+j1].occupancy = fieldOccupancy.EMPTY
        self.fields[i2*8+j2].occupancy = fieldOccupancy.WHITE
        return True
    
    def jumpBlack(self, i1,j1,i2,j2) -> bool:
        a = self.fields[i1*8+j1].occupancy == fieldOccupancy.BLACK
        b = self.fields[i2*8+j2].occupancy == fieldOccupancy.EMPTY
        if not (a and b):
            self.message = "Unsuccessful black jump, start field not black or destination not empty"
            return False
        self.fields[i1*8+j1].occupancy = fieldOccupancy.EMPTY
        self.fields[i2*8+j2].occupancy = fieldOccupancy.BLACK
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
    
    def isWhiteStuck(self) -> bool:
        for i in range(24):
            if self.fields[i].occupancy == fieldOccupancy.WHITE:
                for j in range(24):
                    if field.isAdjacentField(self.fields[i],self.fields[j]) == True:
                        if self.fields[j].occupancy == fieldOccupancy.EMPTY:
                            return False
        return True
    
    def isBlackStuck(self) -> bool:
        for i in range(24):
            if self.fields[i].occupancy == fieldOccupancy.BLACK:
                for j in range(24):
                    if field.isAdjacentField(self.fields[i],self.fields[j]) == True:
                        if self.fields[j].occupancy == fieldOccupancy.EMPTY:
                            return False
        return True
                    









class game:
    def __init__(self) -> None:
        self.board = board()
        self.stage = gameStage.FIRSTSTAGE
        self.initialStageCounter = 9
        self.turn = gameTurn.WHITETURN
        self.action = possibleActions.ADDSTONE
        self.outcome = gameOutcome.GAMEONGOING
        self.CurrentWhiteMills = self.board.WhiteMills()
        self.CurrentBlackMills = self.board.BlackMills()
        self.DoubleMill = False
        self.message = "Initial stage, white to add stone. Click on field"


    def progressGame(self,field1 : field, field2=field(Circle(0),Angle(0))) -> bool:
        a = self.CurrentWhiteMills
        b = self.CurrentBlackMills

        if self.outcome == gameOutcome.WHITEWINS:
            self.message = "Game finished, white has won"
            return False
        if self.outcome == gameOutcome.BLACKWINS:
            self.message = "Game finished, black has won"
            return False

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
                            self.action = possibleActions.EATSTONE
                        if m == 2:
                            self.DoubleMill = True
                        if m == 0:
                            self.turn = gameTurn.BLACKTURN
                        return bool
                    self.message = self.board.message
                    return bool
                if self.action.name == "EATSTONE":
                    bool = self.board.removeBlack(field1.circle.value, field1.angle.value)
                    if bool == True:
                        if self.DoubleMill == True:
                            self.DoubleMill = False
                            return bool
                        self.turn = gameTurn.BLACKTURN
                        self.action = possibleActions.ADDSTONE
                        return bool
                    self.message = self.board.message
                    return bool
            if self.turn.name == "BLACKTURN":
                if self.action.name == "ADDSTONE":
                    bool = self.board.addBlack(field1.circle.value, field1.angle.value)
                    if bool == True:
                        self.initialStageCounter = self.initialStageCounter - 1
                        if self.initialStageCounter == 0:
                            self.stage = gameStage.SECONDSTAGE
                            self.action = possibleActions.MOVESTONE
                        self.CurrentBlackMills = self.board.BlackMills()
                        m = 0
                        for i in range(16):
                            if self.CurrentBlackMills[i] == True and b[i] == False:
                                m = m+1
                        if m > 0:
                            self.action = possibleActions.EATSTONE
                        if m == 2:
                            self.DoubleMill = True
                        if m == 0:
                            self.turn = gameTurn.WHITETURN
                            if self.initialStageCounter==0 and self.board.isWhiteStuck():
                                self.outcome = gameOutcome.BLACKWINS
                                self.message = "White stuck, black wins"
                        return bool
                    self.message = self.board.message
                    return bool
                if self.action.name == "EATSTONE":
                    bool = self.board.removeWhite(field1.circle.value, field1.angle.value)
                    if bool == True:
                        if self.DoubleMill == True:
                            self.DoubleMill = False
                            return bool
                        self.turn = gameTurn.WHITETURN
                        self.action = possibleActions.ADDSTONE
                        return bool
                    self.message = self.board.message
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
                            self.action = possibleActions.EATSTONE
                        if m == 2:
                            self.DoubleMill = True
                        if m == 0:
                            self.turn = gameTurn.BLACKTURN
                            if self.board.isBlackStuck():
                                self.outcome = gameOutcome.WHITEWINS
                                self.message = "Black is Stuck, White wins"
                        return bool
                    self.message = self.board.message
                    return bool
                if self.action.name == "EATSTONE":
                    bool = self.board.removeBlack(field1.circle.value, field1.angle.value)
                    if bool == True:
                        if self.DoubleMill == True:
                            self.DoubleMill = False
                            return bool
                        if self.board.BlackCount()<4:
                            self.stage = gameStage.FINALSTAGE
                            self.action = possibleActions.JUMPSTONE
                        else:
                            self.action = possibleActions.MOVESTONE
                        self.turn = gameTurn.BLACKTURN
                        if self.board.BlackCount()>3 and self.board.isBlackStuck():
                            self.outcome = gameOutcome.WHITEWINS
                            self.message = "Black is Stuck, White wins"
                        return bool
                    self.message = self.board.message
                    return bool
            if self.turn.name == "BLACKTURN":
                if self.action.name == "MOVESTONE":
                    bool = self.board.moveBlack(field1.circle.value, field1.angle.value,field2.circle.value, field2.angle.value)
                    if bool == True:
                        self.CurrentBlackMills = self.board.BlackMills()
                        m = 0
                        for i in range(16):
                            if self.CurrentBlackMills[i] == True and b[i] == False:
                                m = m+1
                        if m > 0:
                            self.action = possibleActions.EATSTONE
                        if m == 2:
                            self.DoubleMill = True
                        if m == 0:
                            self.turn = gameTurn.WHITETURN
                            if self.board.isWhiteStuck():
                                self.outcome = gameOutcome.BLACKWINS
                                self.message = "White is Stuck, Black wins"
                        return bool
                    self.message = self.board.message
                    return bool
                if self.action.name == "EATSTONE":
                    bool = self.board.removeWhite(field1.circle.value, field1.angle.value)
                    if bool == True:
                        if self.DoubleMill == True:
                            self.DoubleMill = False
                            return bool
                        if self.board.WhiteCount()<4:
                            self.stage = gameStage.FINALSTAGE
                            self.action = possibleActions.JUMPSTONE
                        else:
                            self.action = possibleActions.MOVESTONE
                        self.turn = gameTurn.WHITETURN
                        if self.board.WhiteCount()>3 and self.board.isWhiteStuck():
                            self.outcome = gameOutcome.BLACKWINS
                            self.message = "White is Stuck, Black wins"
                        return bool
                    self.message = self.board.message
                    return bool
                
        if self.stage == gameStage.FINALSTAGE:
            if self.turn == gameTurn.WHITETURN:
                if self.action == possibleActions.MOVESTONE:
                    bool = self.board.moveWhite(field1.circle.value, field1.angle.value,field2.circle.value, field2.angle.value)
                    if bool == True:
                        self.CurrentWhiteMills = self.board.WhiteMills()
                        m = 0
                        for i in range(16):
                            if self.CurrentWhiteMills[i] == True and a[i] == False:
                                m = m+1
                        if m > 0:
                            self.action = possibleActions.EATSTONE
                        if m == 2:
                            self.DoubleMill = True
                        if m == 0:
                            self.turn = gameTurn.BLACKTURN
                            if self.board.BlackCount()<4:
                                self.action = possibleActions.JUMPSTONE
                        return bool
                    self.message = self.board.message
                    return bool
                if self.action == possibleActions.JUMPSTONE:
                    bool = self.board.jumpWhite(field1.circle.value, field1.angle.value,field2.circle.value, field2.angle.value)
                    if bool == True:
                        self.CurrentWhiteMills = self.board.WhiteMills()
                        m = 0
                        for i in range(16):
                            if self.CurrentWhiteMills[i] == True and a[i] == False:
                                m = m+1
                        if m > 0:
                            self.action = possibleActions.EATSTONE
                        if m == 2:
                            self.DoubleMill = True
                        if m == 0:
                            self.turn = gameTurn.BLACKTURN
                            if self.board.BlackCount()>3:
                                self.action = possibleActions.MOVESTONE
                        return bool
                    self.message = self.board.message
                    return bool
                if self.action == possibleActions.EATSTONE:
                    bool = self.board.removeBlack(field1.circle.value, field1.angle.value)
                    if bool == True:
                        if self.DoubleMill == True:
                            self.DoubleMill = False
                            return bool
                        self.action = possibleActions.MOVESTONE
                        if self.board.BlackCount()<4:
                            self.action = possibleActions.JUMPSTONE
                        self.turn = gameTurn.BLACKTURN
                        if self.board.BlackCount()<3:
                            self.outcome = gameOutcome.WHITEWINS
                            self.message = "Black has less than 3 stones left, White wins"
                        return bool
                    self.message = self.board.message
                    return bool
            if self.turn == gameTurn.BLACKTURN:
                if self.action == possibleActions.MOVESTONE:
                    bool = self.board.moveBlack(field1.circle.value, field1.angle.value,field2.circle.value, field2.angle.value)
                    if bool == True:
                        self.CurrentBlackMills = self.board.BlackMills()
                        m = 0
                        for i in range(16):
                            if self.CurrentBlackMills[i] == True and b[i] == False:
                                m = m+1
                        if m > 0:
                            self.action = possibleActions.EATSTONE
                        if m == 2:
                            self.DoubleMill = True
                        if m == 0:
                            self.turn = gameTurn.WHITETURN
                            if self.board.WhiteCount()<4:
                                self.action = possibleActions.JUMPSTONE
                        return bool
                    self.message = self.board.message
                    return bool
                if self.action == possibleActions.JUMPSTONE:
                    bool = self.board.jumpBlack(field1.circle.value, field1.angle.value,field2.circle.value, field2.angle.value)
                    if bool == True:
                        self.CurrentBlackMills = self.board.BlackMills()
                        m = 0
                        for i in range(16):
                            if self.CurrentBlackMills[i] == True and b[i] == False:
                                m = m+1
                        if m > 0:
                            self.action = possibleActions.EATSTONE
                        if m == 2:
                            self.DoubleMill = True
                        if m == 0:
                            self.turn = gameTurn.WHITETURN
                            if self.board.WhiteCount()>3:
                                self.action = possibleActions.MOVESTONE
                        return bool
                    self.message = self.board.message
                    return bool
                if self.action == possibleActions.EATSTONE:
                    bool = self.board.removeWhite(field1.circle.value, field1.angle.value)
                    if bool == True:
                        if self.DoubleMill == True:
                            self.DoubleMill = False
                            return bool
                        self.action = possibleActions.MOVESTONE
                        if self.board.BlackCount()<4:
                            self.action = possibleActions.JUMPSTONE
                        self.turn = gameTurn.WHITETURN
                        if self.board.WhiteCount()<3:
                            self.outcome = gameOutcome.BLACKWINS
                            self.message = "White has less than 3 stones left, Black wins"
                        return bool
                    self.message = self.board.message
                    return bool

        return True

        

            
        







