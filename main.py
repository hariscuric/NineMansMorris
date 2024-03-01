from NMMclasses import *
from boardGraphics import *


def main():
    a = game()
    a.board.addWhite(0,0)
    a.board.addBlack(1,0)
    b = boardGraphics()
    b.drawGame(a)
    a.board.addWhite(2,0)
    b.drawGame(a)
    a.board.moveWhite(2,0,2,1)
    b.drawGame(a)
    b.getMouse()


main()
