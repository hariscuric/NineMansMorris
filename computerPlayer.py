from NMMclasses import *
import random
import copy

class stoneColor(Enum):
    WHITE = 0
    BLACK = 1



def computeHeuristicFunction(game : game, stoneColor : stoneColor) -> int:
    if stoneColor == stoneColor.WHITE:
        heuristicMeasure = game.board.WhiteCount()-game.board.BlackCount()
        if game.board.WhiteCount() < 3:
            heuristicMeasure = -7
        if game.board.BlackCount() < 3:
            heuristicMeasure = 7
        if game.board.isWhiteStuck():
            heuristicMeasure = -7
        if game.board.isBlackStuck():
            heuristicMeasure = 7
        
    if stoneColor == stoneColor.BLACK:
        heuristicMeasure = game.board.BlackCount()-game.board.WhiteCount()
        if game.board.WhiteCount() < 3:
            heuristicMeasure = 7
        if game.board.BlackCount() < 3:
            heuristicMeasure = -7
        if game.board.isWhiteStuck():
            heuristicMeasure = 7
        if game.board.isBlackStuck():
            heuristicMeasure = -7
    
    return heuristicMeasure



def oneMoveHeuristicFunction(game : game, action) -> float:
    gamecopy = copy.deepcopy(game)
    gamecopy.progressGame(action[0], action[1])
    points = 0
    if game.turn == gameTurn.WHITETURN:
        a = game.board.WhiteMills()
        b = gamecopy.board.WhiteMills()
        millsCreated = 0
        for i in range(16):
            if a[i] == False and b[i] == True:
                millsCreated = millsCreated+1
        points = points + millsCreated

        a = game.nextMoveWhiteMill()
        b = gamecopy.nextMoveWhiteMill()
        a = sum(a)
        if a > 2:
            a = 2
        b = sum(b)
        if b > 2:
            b = 2
        a = a/3
        b = b/3
        c = b-a
        points = points + c

        a = game.nextMoveBlackMill()
        b = gamecopy.nextMoveBlackMill()
        a = max(a)
        b = max(b)
        if a == 1 and b == 0:
            c = 2/3
        elif a == 0 and b == 1:
            c = -2/3
        else:
            c = 0
        points = points + c

    if game.turn == gameTurn.BLACKTURN:
        a = game.board.BlackMills()
        b = gamecopy.board.BlackMills()
        millsCreated = 0
        for i in range(16):
            if a[i] == False and b[i] == True:
                millsCreated = millsCreated+1
        points = points + millsCreated

        a = game.nextMoveBlackMill()
        b = gamecopy.nextMoveBlackMill()
        a = sum(a)
        if a > 2:
            a = 2
        b = sum(b)
        if b > 2:
            b = 2
        a = a/3
        b = b/3
        c = b-a
        points = points + c

        a = game.nextMoveWhiteMill()
        b = gamecopy.nextMoveWhiteMill()
        a = max(a)
        b = max(b)
        if a == 1 and b == 0:
            c = 2/3
        elif a == 0 and b == 1:
            c = -2/3
        else:
            c = 0
        points = points + c
        


    return points




def computeOptimalAction(game : game, stonecolor : stoneColor, movesAhead : int):
    
    if movesAhead == 0:
        return [computeHeuristicFunction(game,stonecolor), [field(Circle(0),Angle(0)),field(Circle(0),Angle(0))]]
    
    if game.outcome == gameOutcome.WHITEWINS:
        if stonecolor == stoneColor.WHITE:
            return [7 , [field(Circle(0),Angle(0)),field(Circle(0),Angle(0))]]
        if stonecolor == stoneColor.BLACK:
            return [-7 , [field(Circle(0),Angle(0)),field(Circle(0),Angle(0))]]
        
    if game.outcome == gameOutcome.BLACKWINS:
        if stonecolor == stoneColor.BLACK:
            return [7 , [field(Circle(0),Angle(0)),field(Circle(0),Angle(0))]]
        if stonecolor == stoneColor.WHITE:
            return [-7 , [field(Circle(0),Angle(0)),field(Circle(0),Angle(0))]]
        
    gamecopy = copy.deepcopy(game)
    actions = []
    utilities = []


    if gamecopy.action == possibleActions.ADDSTONE or gamecopy.action == possibleActions.EATSTONE:
        for i in gamecopy.board.fields:
            bool = gamecopy.progressGame(i)
            gamecopy = copy.deepcopy(game)
            if bool:
                actions.append([i,field(Circle.INNER,Angle.NORTH)])

    if gamecopy.action == possibleActions.MOVESTONE or gamecopy.action == possibleActions.JUMPSTONE:
        for i in gamecopy.board.fields:
            for j in gamecopy.board.fields:
                bool = gamecopy.progressGame(i,j)
                gamecopy = copy.deepcopy(game)
                if bool:
                    actions.append([i,j])

    for i in actions:
        gamecopy.progressGame(i[0],i[1])
        a = computeOptimalAction(gamecopy,stonecolor,movesAhead-1)
        utility = a[0]
        utilities.append(utility)
        gamecopy = copy.deepcopy(game)

    if (game.turn == gameTurn.WHITETURN and stonecolor == stoneColor.WHITE) or \
    (game.turn == gameTurn.BLACKTURN and stonecolor == stoneColor.BLACK):
        a = max(utilities)
        indices = [i for i, x in enumerate(utilities) if x == a]
        b = random.choice(indices)
        return [a, actions[b]]
    
    if (game.turn == gameTurn.WHITETURN and stonecolor == stoneColor.BLACK) or \
    (game.turn == gameTurn.BLACKTURN and stonecolor == stoneColor.WHITE):
        a = min(utilities)
        indices = [i for i, x in enumerate(utilities) if x == a]
        b = random.choice(indices)
        return [a, actions[b]]
    



def computeOptimalActionOptimized(game : game, stonecolor : stoneColor, movesAhead : int, searchTreeWidth : int):
    
    if movesAhead == 0:
        return [computeHeuristicFunction(game,stonecolor), [field(Circle(0),Angle(0)),field(Circle(0),Angle(0))]]
    
    if game.outcome == gameOutcome.WHITEWINS:
        if stonecolor == stoneColor.WHITE:
            return [7 , [field(Circle(0),Angle(0)),field(Circle(0),Angle(0))]]
        if stonecolor == stoneColor.BLACK:
            return [-7 , [field(Circle(0),Angle(0)),field(Circle(0),Angle(0))]]
        
    if game.outcome == gameOutcome.BLACKWINS:
        if stonecolor == stoneColor.BLACK:
            return [7 , [field(Circle(0),Angle(0)),field(Circle(0),Angle(0))]]
        if stonecolor == stoneColor.WHITE:
            return [-7 , [field(Circle(0),Angle(0)),field(Circle(0),Angle(0))]]
        
    gamecopy = copy.deepcopy(game)
    actions = []
    utilities = []


    if gamecopy.action == possibleActions.ADDSTONE or gamecopy.action == possibleActions.EATSTONE:
        for i in gamecopy.board.fields:
            bool = gamecopy.progressGame(i)
            gamecopy = copy.deepcopy(game)
            if bool:
                actions.append([i,field(Circle.INNER,Angle.NORTH)])

    if gamecopy.action == possibleActions.MOVESTONE or gamecopy.action == possibleActions.JUMPSTONE:
        for i in gamecopy.board.fields:
            for j in gamecopy.board.fields:
                bool = gamecopy.progressGame(i,j)
                gamecopy = copy.deepcopy(game)
                if bool:
                    actions.append([i,j])

    filteredActions = []
    oneMoveUtilities = []
    for i in actions:
        a = oneMoveHeuristicFunction(gamecopy,i)
        oneMoveUtilities.append(a)

    for i in range(searchTreeWidth):
        if len(oneMoveUtilities)>0:
            a = max(oneMoveUtilities)
            index = random.choice([ii for ii, iii in enumerate(oneMoveUtilities) if iii == a])
            filteredActions.append(actions.pop(index))
            oneMoveUtilities.pop(index)

    actions = filteredActions


    for i in actions:
        gamecopy.progressGame(i[0],i[1])
        a = computeOptimalActionOptimized(gamecopy,stonecolor,movesAhead-1, searchTreeWidth)
        utility = a[0]
        utilities.append(utility)
        gamecopy = copy.deepcopy(game)

    if (game.turn == gameTurn.WHITETURN and stonecolor == stoneColor.WHITE) or \
    (game.turn == gameTurn.BLACKTURN and stonecolor == stoneColor.BLACK):
        a = max(utilities)
        indices = [i for i, x in enumerate(utilities) if x == a]
        b = random.choice(indices)
        return [a, actions[b]]
    
    if (game.turn == gameTurn.WHITETURN and stonecolor == stoneColor.BLACK) or \
    (game.turn == gameTurn.BLACKTURN and stonecolor == stoneColor.WHITE):
        a = min(utilities)
        indices = [i for i, x in enumerate(utilities) if x == a]
        b = random.choice(indices)
        return [a, actions[b]]

    

        
        

