# function to print the board
import random
class board():
    data = [' ']*10
    symbol = ['X','0']
    userlist = ['user','computer']
    gameinplay = 0
    iscomputermove = 0
    usermove = 0
    def printBoard(self,data):
        board = data[7] + ' | ' + data[8] + ' | ' +data[9] + "\n" + \
            '----------' + "\n" + \
            data[4] + ' | ' + data[5] + ' | ' + data[6] + "\n" + \
            '----------' + "\n" + \
            data[1] + ' | ' + data[2] + ' | ' + data[3]
        print(board)

    def startgame(self):
        print('Game started')
        data = [' ']*10
        self.gameinplay = 1
        while self.gameinplay:
            if self.iscomputermove:
                #get computer move
                move = self.getcomputermove(data)
                data = self.makemove(data,move,self.symbol[1])
                self.printBoard(data)
                self.gameinplay = not self.iswinner(data,self.symbol[1])
                if not self.gameinplay:
                    winner = 1
                self.iscomputermove = 0

            else:
                #get user move
                print('Enter users move in 1-9')
                move = input()
                data = self.makemove(data,move,self.symbol[0])
                self.printBoard(data)
                self.gameinplay = not self.iswinner(data,self.symbol[0])
                if not self.gameinplay:
                    winner = 0
                self.iscomputermove = 1


        if not self.gameinplay:
            if winner == 0:
                print('Hurray! You won the game')
            else:
                print('Computer won the game')
            print('Restart game, press y or n?')
            userinput = input()

            if userinput == 'y' or userinput == 'Y':
                newgame = 1
            else:
                newgame = 0

        return newgame






    def getcomputermove(self,data):
        movelist = self.getmoveslist(data)
        computermove = random.choice(movelist)
        return computermove

    def getmoveslist(self,data):
        emptyindex = self.getemptyindex(data)
        return emptyindex

    def getemptyindex(self,data):
        emptyindex = []
        for i in range(1,len(data)):
            if data[i] == ' ':
                emptyindex.append(i)
        return emptyindex

    def makemove(self,data,move,symbol):
        data[int(move)] = symbol
        return data

    def iswinner(self,d,s):
        gameover = ((d[7] == s and d[8] ==s and d[9] == s) or \
                   (d[4] == s and d[5] ==s and d[6] == s) or \
                   (d[1] == s and d[2] == s and d[3] == s) or \
                   (d[7] == s and d[4] ==s and d[1] == s) or \
                   (d[8] == s and d[5] ==s and d[2] == s) or \
                   (d[9] == s and d[6] ==s and d[3] == s) or \
                   (d[7] == s and d[5] ==s and d[3] == s) or \
                   (d[9] == s and d[5] ==s and d[1] == s))
        return gameover








if __name__ == "__main__":
    print('Welcome to tictactoe game')
    #instantiate board
    b = board()

    #chose the user symbol
    print('Chose your symbol')
    symbol = input()
    if symbol == 'x' or symbol == 'X':
        b.symbol = ['X','0']
    else:
        b.symbol = ['0','X']

    #decide who gets to play first
    firstplayer = random.choice(b.userlist)
    print(str(firstplayer) + ' gets to play first')
    if firstplayer == 'computer':
        b.iscomputermove = 1
    else:
        b.iscomputermove = 0
    newgame = b.startgame()
    while newgame:
        newgame = b.startgame()
    print('Thank you for playing tictactoe')


