from NMMclasses import *
from boardGraphics import *


def main():
    a = game()
    b = boardGraphics()
    b.topText(a.message)
    while True:
        b.drawGame(a)
        if a.action == possibleActions.ADDSTONE or a.action == possibleActions.EATSTONE:
            field1 = b.clickedField()
            bool = a.progressGame(field1)
        if a.action == possibleActions.MOVESTONE or a.action == possibleActions.JUMPSTONE:
            field1 = b.clickedField()
            field2 = b.clickedField()
            bool = a.progressGame(field1,field2)
        if bool:
            
            if a.turn == gameTurn.WHITETURN:
                m1 = "white to play, "
            else:
                m1 = "black to play, "
            if a.action == possibleActions.ADDSTONE:
                m2 = "click on an empty field to add a stone"
            elif a.action == possibleActions.EATSTONE:
                m2 = "click on an opponent's stone to remove it"
            elif a.action == possibleActions.MOVESTONE:
                m2 = "click on a stone and an adjacent field to move it"
            elif a.action == possibleActions.JUMPSTONE:
                m2 = "click on a stone and any free field to jump"
            b.topText(m1+m2)
        else:
            b.topText(a.message)


main()
