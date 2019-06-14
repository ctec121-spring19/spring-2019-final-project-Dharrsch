# View.py
# 
# For TicTacToe
from graphics import *


class View:

    def __init__(self):
        self.win=GraphWin()
        self.win.setCoords(0,0,3,4)
        Line(Point(1,0), Point(1,3)).draw(self.win)
        Line(Point(2,0), Point(2,3)).draw(self.win)
        Line(Point(0,1), Point(3,1)).draw(self.win)
        Line(Point(0,2), Point(3,2)).draw(self.win)
        p=self.win.getMouse()
        self.cellNum=int(p.getY())*3+int(p.getX())
        self.objectList=[]
        
    def dobjects(self):
        for obj in objectList:
            obj.undraw()
        objectList.clear()


    def drawO(self):
        x=(self.cellNum%3)+.5
        y=(self.cellNum//3)+.5
        h=Point(x,y)
        circ=Circle(h,.3).draw(self.win)
        circ.setFill("red")
    
    def drawX(self):
        x=(self.cellNum%3)+.5
        y=(self.cellNum//3)+.5
        h=Point(x,y)
        circ=Circle(h,.3).draw(self.win)
        circ.setFill("black")
        
    def message(self,words):
        mess=Text(Point(1.5,3.5),words).draw(self.win)
def ViewTest():
    v=View()
    v.drawO()
    v.drawX()
    v.Cell()

if __name__ == "__main__":
    ViewTest()
