# Model.py
#
# For TicTacToe

from View import View

class Model:

    def __init__(self):
        self.v=View()
        self.validity=[0,0,0,0,0,0,0,0,0,1,1,1]
        self.Cplayer='X'
        

    def valid(self):
        cpos=self.v.cellnumber()


        if self.validity[cpos] == 1:
            print("invalid")

        elif self.validity[cpos] == 0:
            self.validity[cpos]=1
            
            if self.Cplayer == 'X':
                self.v.drawX(cpos)
                self.Cplayer = 'O'
            else:
                self.v.drawO(cpos)
                self.Cplayer = 'X'
            
            print(self.validity)
            print("valid")
        else:
            print("something is wrong")


    def Lobjects(self):
        objectList=[]
        cellnum=self.v.cellnumber()
        objectList.insert(cellnum,self.Cplayer)
        print(objectList)
        '''
        for obj in objectList:
            obj.undraw()
        objectList.clear()
        '''
def ModelTest():
    m=Model()
    m.valid()
    input()
if __name__ == "__main__":
    ModelTest()
