from NMMclasses import *
from boardGraphics import *


def main():
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



main()
