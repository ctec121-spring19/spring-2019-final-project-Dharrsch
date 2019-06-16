# Controller.py
#
# For TicTacToe

from View import View
from Model import Model
'''
example in canvas page
controller tells model to test or draw
v=view()-call view methods 
m=model(V)- call model methods able to see view
self.player="X"
v.message("x turn...")
ask model for empty cell
? list of drawn objects

'''
class Controller:

    def __init__(self):
        self.m=Model()

    def playgame(self):
        while True:
            self.m.valid()
            self.m.Lobjects()
            

def ControllerTest():
    c=Controller()
    c.playgame()

if __name__ == "__main__":
    ControllerTest()
