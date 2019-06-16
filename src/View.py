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
        
        

    def cellnumber(self):
        p=self.win.getMouse()
        xcoord=p.getX()
        ycoord=p.getY()
        cellNum=int(p.getY())*3+int(p.getX())
        return cellNum


    def drawO(self,cellNum):
        x=(cellNum%3)+.5
        y=(cellNum//3)+.5
        Text(Point(x,y),"O").draw(self.win)
    
    def drawX(self,cellNum):
        x=(cellNum%3)+.5
        y=(cellNum//3)+.5
        Text(Point(x,y),"X").draw(self.win)
        
    def message(self,words):
        mess=Text(Point(1.5,3.5),words).draw(self.win)

def ViewTest():
    v=View()
    c=v.cellnumber()
    v.drawO(c)
    v.message('')
    
    
    

if __name__ == "__main__":
    ViewTest()
