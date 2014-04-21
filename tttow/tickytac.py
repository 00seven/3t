#!/usr/bin/env python


import random
## models.py
class Game:
    def __init__(self):
        self.board    = [[0],[1],[2],
                         [3],[4],[5],
                         [6],[7],[8],]
        self.player   = ''  
        self.man      = 0
        self.machine  = 0
        self.goes_first = True
        self.turn     = 0
        self.winner   = (
                 # Horizontal Winning Sets
                 [0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8],
                 # Verticle Winning Sets
                 [0, 3, 6],
                 [1, 4, 7],
                 [2, 5, 8],
                 # Diagonal Winning Sets
                 [0, 4, 8],
                 [2, 4, 6]
                )

    
    # Number Turns Taken
    def turn_incr(self):
        self.turn += 1
        return self.turn


    def is_winner(self,winner=0):
        player = self.player
        if player:
            winner = player
        return winner

    
    def whos_turn(self):
        if self.man:
            return self.man
        else:
            return self.machine
    

    # Display Board
    def print_board(self):
        print "--A-TicTacToe-Game--"
        for i in xrange(3):
            print ' ',
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



g = Game()

print g.board[:]
print len(g.board)

g.print_board()

