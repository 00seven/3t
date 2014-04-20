#!/usr/bin/env python


import random
## models.py
class Game:
    def __init__(self):
        self.board   = [[0],[1],[2],[3],[4],[5],[6],[7],[8],]
        self.playerh = ''
        self.playerc = random.seed().randomint(0,8)

    def player_turn(self):
        self.playerc 
        return None

    def print_board(self):
        print "--A-TicTacToe-Game--"
        for i in range(3):
            print " ",
            for j in range(3):
                if self.board[i*3+j] == 1:
                    print 'X',
                elif self.board[i*3+j] == 0:
                    print 'O',
                else:
                    print ' ',
                if j != 2:
                    print " | ",
            print

            if i != 2:
                print "-----------------"
            else:
                print

    


class Game2:
    def __init__(self):
        self.board = [
                    ["X", "O", "X"],
                    ["O", "O", " "],
                    ["X", "O", "1"]
                    ]
        self.player = 1
        self.playerC = 0



g = Game()


print g.board[:]
print len(g.board)
fibi=fib()
print fibi.next()

g.print_board()
#print fibi.next()
## views.py









## urls.py ## Control






## templates

# base.html

#