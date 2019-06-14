# Model.py
#
# For TicTacToe

from View import View

class Model:

    def __init__(self):
        v=View()
        self.validity=[0,0,0,0,0,0,0,0,0,1,1,1]
'''
valid move at 0 invalid at 1
'''
    def valid(self):
        self.validity[self.View.Cell()]=1
        print(self.validity)

def ModelTest():
    m=Model()
    m.valid()

if __name__ == "__main__":
    ModelTest()
