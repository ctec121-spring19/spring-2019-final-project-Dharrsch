# Model.py
#
# For TicTacToe

from View import View

class Model:

    def __init__(self):
        self.v=View()
        self.validity=[0,0,0,0,0,0,0,0,0,1,1,1]
        self.Cplayer= 'X'
        self.objectList=['','','','','','','','','']
    #test to see if cell num is valid
    def valid(self,cpos):
        if  self.validity[cpos] == 0:
            self.validity[cpos]=1
            move= "valid"
            #if move is valid draw X or O
            if self.Cplayer == 'O':
                self.v.drawO(cpos)
                print("X's Turn")
                self.Cplayer = 'X'
            else:
                self.v.drawX(cpos)
                print("O's Turn")
                self.Cplayer = 'O'
        else:
            self.validity[cpos] == 1
            move = "invalid"
        return move

    #create object list with X and O at position on board
    def Lobjects(self,cpos):
        self.objectList[cpos]=self.Cplayer
        objlist=self.objectList
        return objlist

    #Win conditions for X
    def winX(self,olist):
        winner=""
        if olist[6] =='O' and olist[7]=='O' and olist[8]=='O':
            winner="X"
        elif olist[3] =='O' and olist[4]=='O' and olist[5]=='O':
            winner="X"
        elif olist[0] =='O' and olist[1]=='O' and olist[2]=='O':
            winner="X"
        elif olist[6] =='O' and olist[3]=='O' and olist[0]=='O':
            winner="X"
        elif olist[7] =='O' and olist[4]=='O' and olist[1]=='O':
            winner="X"
        elif olist[8] =='O' and olist[5]=='O' and olist[2]=='O':
            winner="X"
        elif olist[0] =='O' and olist[4]=='O' and olist[8]=='O':
            winner="X"
        elif olist[6] =='O' and olist[4]=='O' and olist[2]=='O':
            winner="X"
        else:
            pass
        return winner

    #win conditions for O
    def winO(self,olist):
        winner=""
        if olist[6] =='X' and olist[7]=='X' and olist[8]=='X':
            winner="O"
        if olist[3] =='X' and olist[4]=='X' and olist[5]=='X':
            winner="O"
        if olist[0] =='X' and olist[1]=='X' and olist[2]=='X':
            winner="O"
        if olist[0] =='X' and olist[3]=='X' and olist[6]=='X':
            winner="O"
        if olist[1] =='X' and olist[4]=='X' and olist[7]=='X':
            winner="O"
        if olist[2] =='X' and olist[5]=='X' and olist[8]=='X':
            winner="O"
        if olist[0] =='X' and olist[4]=='X' and olist[8]=='X':
            winner="O"
        if olist[2] =='X' and olist[4]=='X' and olist[6]=='X':
            winner="O"
        return winner
    
    # conditions for tiegame
    def tie(self,olist,w1,w2):
        winner=""
        winner=""
        if olist[0]!='' and olist[1]!='' and olist[2]!='' and olist[3]!='' and olist[4]!='' and olist[5]!= '' and olist[6]!='' and olist[7] != '' and olist[8]!='' and winner != "X" and winner != "O":
            self.v.message("Tie game")
            game="tie"
            return game
        else:
            pass

def ModelTest():
    m=Model()
    v=View()
    c=v.cellnumber()
    m.valid(c)
    g=m.Lobjects(c)
    m.winX(g)
    input()
if __name__ == "__main__":
    ModelTest()
