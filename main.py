from NMMclasses import *
from boardGraphics import *
from computerPlayer import *


def inputNumOfPlayers():
    a = int(input("Input number of players (1 for single-player, 2 for multiplayer game): "))
    if not (a==1 or a==2):
        print("Input 1 or 2")
        return inputNumOfPlayers()
    return a

def inputStoneColor():
    a = int(input("Choose the color of the stone, 1 for white and 2 for black "))
    if not (a==1 or a==2):
        print("Input 1 or 2")
        return inputStoneColor()
    return a
    


def main():

    numOfPlayers = inputNumOfPlayers()

    if numOfPlayers == 1:
        stoneColorIndex = inputStoneColor()

    #FOR MULTIPLAYER GAME (TWO PLAYERS):
    if numOfPlayers == 2:
        a = game()
        b = boardGraphics()
        b.topText(a.message)
        loop_condition = 1
        while loop_condition:
            b.drawGame(a)
            currentAction = a.action
            if a.outcome == gameOutcome.GAMEONGOING:
                if currentAction == possibleActions.ADDSTONE or currentAction == possibleActions.EATSTONE:
                    field1 = b.clickedField()
                    bool = a.progressGame(field1)
                if currentAction == possibleActions.MOVESTONE or currentAction == possibleActions.JUMPSTONE:
                    field1 = b.clickedField()
                    field2 = b.clickedField()
                    bool = a.progressGame(field1,field2)
                if bool:

                    
                    if a.turn == gameTurn.WHITETURN:
                        m1 = "WHITE TO PLAY, "
                    else:
                        m1 = "BLACK TO PLAY, "
                    if a.action == possibleActions.ADDSTONE:
                        m2 = "CLICK ON AN EMPTY FIELD TO ADD A STONE"
                    elif a.action == possibleActions.EATSTONE:
                        m2 = "CLICK ON AN OPPONENT'S STONE TO REMOVE IT"
                    elif a.action == possibleActions.MOVESTONE:
                        m2 = "CLICK ON A STONE AND AN ADJACENT FIELD TO MOVE IT TO"
                    elif a.action == possibleActions.JUMPSTONE:
                        m2 = "CLICK ON A STONE AND ANY FREE FIELD TO JUMP TO"
                    b.topText(m1+m2)
                else:
                    b.topText(a.message)


            elif a.outcome==gameOutcome.WHITEWINS:
                b.topText("WHITE WON. Press Esc to exit game")
                key = b.window.getKey()
                if key == "Escape":
                    loop_condition = 0
                    b.window.close()
            elif a.outcome == gameOutcome.BLACKWINS:
                b.topText("BLACK WON. Press Esc to exit game")
                key = b.window.getKey()
                if key == "Escape":
                    loop_condition = 0
                    b.window.close()



    #FOR SINGLE PLAYER GAME:
    # if numOfPlayers == 1:
    #     if stoneColorIndex == 1:
    #         computerColor = stoneColor.BLACK
    #     if stoneColorIndex ==2:
    #         computerColor = stoneColor.WHITE
    #     a = game()
    #     b = boardGraphics()
    #     b.topText(a.message)
    #     loop_condition = 1
    #     while loop_condition:
    #         b.drawGame(a)
    #         currentAction = a.action
    #         if a.outcome == gameOutcome.GAMEONGOING:
    #             if currentAction == possibleActions.ADDSTONE or currentAction == possibleActions.EATSTONE:
    #                 if (a.turn == gameTurn.WHITETURN and computerColor == stoneColor.WHITE) or \
    #                 (a.turn == gameTurn.BLACKTURN and computerColor == stoneColor.BLACK):
    #                     b.topText("COMPUTER IS THINKING...")
    #                     computerDecision = computeOptimalAction(a, computerColor, 3)
    #                     computerFieldClick = computerDecision[1]
    #                     field1 = computerFieldClick[0]
    #                 else:
    #                     field1 = b.clickedField()
    #                 bool = a.progressGame(field1)
    #             if currentAction == possibleActions.MOVESTONE or currentAction == possibleActions.JUMPSTONE:
    #                 if (a.turn == gameTurn.WHITETURN and computerColor == stoneColor.WHITE) or \
    #                 (a.turn == gameTurn.BLACKTURN and computerColor == stoneColor.BLACK):
    #                     b.topText("COMPUTER IS THINKING...")
    #                     computerDecision = computeOptimalAction(a, computerColor, 3)
    #                     computerFieldClick = computerDecision[1]
    #                     field1 = computerFieldClick[0]
    #                     field2 = computerFieldClick[1]
    #                 else:
    #                     field1 = b.clickedField()
    #                     field2 = b.clickedField()
    #                 bool = a.progressGame(field1,field2)
    #             if bool:

                    
    #                 if a.turn == gameTurn.WHITETURN:
    #                     m1 = "WHITE TO PLAY, "
    #                 else:
    #                     m1 = "BLACK TO PLAY, "
    #                 if a.action == possibleActions.ADDSTONE:
    #                     m2 = "CLICK ON AN EMPTY FIELD TO ADD A STONE"
    #                 elif a.action == possibleActions.EATSTONE:
    #                     m2 = "CLICK ON AN OPPONENT'S STONE TO REMOVE IT"
    #                 elif a.action == possibleActions.MOVESTONE:
    #                     m2 = "CLICK ON A STONE AND AN ADJACENT FIELD TO MOVE IT TO"
    #                 elif a.action == possibleActions.JUMPSTONE:
    #                     m2 = "CLICK ON A STONE AND ANY FREE FIELD TO JUMP TO"
    #                 b.topText(m1+m2)
    #             else:
    #                 b.topText(a.message)


    #         elif a.outcome==gameOutcome.WHITEWINS:
    #             b.topText("WHITE WON. Press Esc to exit game")
    #             key = b.window.getKey()
    #             if key == "Escape":
    #                 loop_condition = 0
    #                 b.window.close()
    #         elif a.outcome == gameOutcome.BLACKWINS:
    #             b.topText("BLACK WON. Press Esc to exit game")
    #             key = b.window.getKey()
    #             if key == "Escape":
    #                 loop_condition = 0
    #                 b.window.close()

    if numOfPlayers == 1:
        if stoneColorIndex == 1:
            computerColor = stoneColor.BLACK
        if stoneColorIndex ==2:
            computerColor = stoneColor.WHITE
        a = game()
        b = boardGraphics()
        b.topText(a.message)
        loop_condition = True
        while loop_condition:
            b.drawGame(a)
            currentAction = a.action
            if a.outcome == gameOutcome.GAMEONGOING:
                if currentAction == possibleActions.ADDSTONE or currentAction == possibleActions.EATSTONE:
                    if (a.turn == gameTurn.WHITETURN and computerColor == stoneColor.WHITE) or \
                    (a.turn == gameTurn.BLACKTURN and computerColor == stoneColor.BLACK):
                        b.topText("COMPUTER IS THINKING...")
                        computerDecision = computeOptimalActionOptimized(a, computerColor, 6, 4)
                        computerFieldClick = computerDecision[1]
                        field1 = computerFieldClick[0]
                    else:
                        field1 = b.clickedField()
                    bool = a.progressGame(field1)
                if currentAction == possibleActions.MOVESTONE or currentAction == possibleActions.JUMPSTONE:
                    if (a.turn == gameTurn.WHITETURN and computerColor == stoneColor.WHITE) or \
                    (a.turn == gameTurn.BLACKTURN and computerColor == stoneColor.BLACK):
                        b.topText("COMPUTER IS THINKING...")
                        computerDecision = computeOptimalActionOptimized(a, computerColor, 6, 4)
                        computerFieldClick = computerDecision[1]
                        field1 = computerFieldClick[0]
                        field2 = computerFieldClick[1]
                    else:
                        field1 = b.clickedField()
                        field2 = b.clickedField()
                    bool = a.progressGame(field1,field2)
                if bool:

                    
                    if a.turn == gameTurn.WHITETURN:
                        m1 = "WHITE TO PLAY, "
                    else:
                        m1 = "BLACK TO PLAY, "
                    if a.action == possibleActions.ADDSTONE:
                        m2 = "CLICK ON AN EMPTY FIELD TO ADD A STONE"
                    elif a.action == possibleActions.EATSTONE:
                        m2 = "CLICK ON AN OPPONENT'S STONE TO REMOVE IT"
                    elif a.action == possibleActions.MOVESTONE:
                        m2 = "CLICK ON A STONE AND AN ADJACENT FIELD TO MOVE IT TO"
                    elif a.action == possibleActions.JUMPSTONE:
                        m2 = "CLICK ON A STONE AND ANY FREE FIELD TO JUMP TO"
                    b.topText(m1+m2)
                else:
                    b.topText(a.message)


            elif a.outcome==gameOutcome.WHITEWINS:
                b.topText("WHITE WON. Press Esc to exit game")
                key = b.window.getKey()
                if key == "Escape":
                    loop_condition = False
                    b.window.close()
            elif a.outcome == gameOutcome.BLACKWINS:
                b.topText("BLACK WON. Press Esc to exit game")
                key = b.window.getKey()
                if key == "Escape":
                    loop_condition = False
                    b.window.close()




main()
