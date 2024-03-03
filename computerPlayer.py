from NMMclasses import *

class stoneColor(Enum):
    WHITE = 0
    BLACK = 1

class player:
    def __init__(self, game: game, stoneColor : stoneColor) -> None:
        self.game = game
        self.stoneColor = stoneColor

    def computeHeuristicFunction(self) -> int:
        if self.stoneColor == stoneColor.WHITE:
            heuristicMeasure = self.game.board.WhiteCount()-self.game.board.BlackCount()
            if self.game.board.WhiteCount() < 3:
                heuristicMeasure = -7
            if self.game.board.BlackCount() < 3:
                heuristicMeasure = 7
            if self.game.board.isWhiteStuck():
                heuristicMeasure = -7
            if self.game.board.isBlackStuck():
                heuristicMeasure = 7
            
        if self.stoneColor == stoneColor.BLACK:
            heuristicMeasure = self.game.board.BlackCount()-self.game.board.WhiteCount()
            if self.game.board.WhiteCount() < 3:
                heuristicMeasure = 7
            if self.game.board.BlackCount() < 3:
                heuristicMeasure = -7
            if self.game.board.isWhiteStuck():
                heuristicMeasure = 7
            if self.game.board.isBlackStuck():
                heuristicMeasure = -7
        
        return heuristicMeasure
    
    def computeOptimalAction(self, movesAhead):
        #stopped here for the night
        #to be continued
        return True
        

        
        

