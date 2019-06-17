# Controller.py
#
# For TicTacToe

from View import View
from Model import Model

class Controller:

    def __init__(self):
        self.m=Model()
        self.v=View()

    def playgame(self):
        #create a loop for playing the game over again
        while True:
            done = False
            #create a loop for running methods
            while not done:
                #test for valid and draw
                cell=self.v.cellnumber()
                ValMove=self.m.valid(cell)

                # if valid move place object in object list
                if ValMove == "valid":
                    olist=self.m.Lobjects(cell)
                else:
                    self.v.message("Invalid Move")

                #check to see if there is a winner
                winnerx=self.m.winX(olist)
                winnero=self.m.winO(olist)

                # if there is a winner tell players
                if winnero =="O":
                    self.v.message("")
                    self.v.message("O is the Winner")
                    done= True
                    
                if winnerx == "X":
                    self.v.message("")
                    self.v.message("X is the Winner")
                    done=True
                    
                #test for tie game
                t=self.m.tie(olist,winnero,winnerx)
                if t =="tie":
                    done=True
            # ask to play again
            GO=(input(print("Play again? (y/n): " )))
            if GO == "y":
                continue
            else:
                break

def ControllerTest():
    c=Controller()
    c.playgame()

if __name__ == "__main__":
    ControllerTest()
