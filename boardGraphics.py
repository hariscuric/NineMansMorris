import graphics as gr
import NMMclasses as nmmc


class boardGraphics:
    def __init__(self) -> None:
        windowWidth = 1100
        windowHeight = 700
        self.window = gr.GraphWin("Nine Man's Morris", windowWidth, windowHeight)
        self.window.setBackground(gr.color_rgb(200,200,200))
        self.window.setCoords(0,windowHeight,windowWidth,0)
        pointsX = []
        for i in range(1,8,1):
            pointsX.append(int(windowWidth/8*i))
        pointsY = []
        for i in range(1,8,1):
            pointsY.append(int(windowHeight/8*i))
        self.points = []
        a = []
        for i in pointsX:
            for j in pointsY:
                a.append(gr.Point(i,j))
        for i in [23,30,31,32,25,18,17,16,22,36,38,40,26,12,10,8,21,42,45,48,27,6,3,0]:
            self.points.append(a[i])
        self.circles = []
        for i in self.points:
            self.circles.append(gr.Circle(i,15))
        for i in self.circles:
            i.setFill("blue")
            i.setOutline("blue")
            i.draw(self.window)

        a = []
        a.append(gr.Line(self.points[23],self.points[17]))
        a.append(gr.Line(self.points[17],self.points[19]))
        a.append(gr.Line(self.points[19],self.points[21]))
        a.append(gr.Line(self.points[21],self.points[23]))
        a.append(gr.Line(self.points[15],self.points[9]))
        a.append(gr.Line(self.points[9],self.points[11]))
        a.append(gr.Line(self.points[11],self.points[13]))
        a.append(gr.Line(self.points[13],self.points[15]))
        a.append(gr.Line(self.points[7],self.points[1]))
        a.append(gr.Line(self.points[1],self.points[3]))
        a.append(gr.Line(self.points[3],self.points[5]))
        a.append(gr.Line(self.points[5],self.points[7]))
        a.append(gr.Line(self.points[0],self.points[16]))
        a.append(gr.Line(self.points[2],self.points[18]))
        a.append(gr.Line(self.points[4],self.points[20]))
        a.append(gr.Line(self.points[6],self.points[22]))

        self.lines = a
        for i in self.lines:
            i.setFill("blue")
            i.setOutline("blue")
            i.setWidth(3)
            i.draw(self.window)

        self.whitePieces = []
        self.blackPieces = []
        


    def getMouse(self):
        self.window.getMouse()
        self.getMouse()
    
    def drawGame(self, game : nmmc.game):
        for i in self.whitePieces:
            i.undraw()
        for i in self.blackPieces:
            i.undraw()
        self.whitePieces = []
        self.blackPieces = []
        for i in game.board.fields:
            if i.occupancy.name == 'WHITE':
                self.whitePieces.append(gr.Circle(self.points[i.circle.value*8+i.angle.value],20))
                self.whitePieces[-1].setFill("white")
                self.whitePieces[-1].setOutline("gray")
                self.whitePieces[-1].draw(self.window)
            if i.occupancy.name == 'BLACK':
                self.blackPieces.append(gr.Circle(self.points[i.circle.value*8+i.angle.value],20))
                self.blackPieces[-1].setFill("black")
                self.blackPieces[-1].setOutline("gray")
                self.blackPieces[-1].draw(self.window)

    


