#!/usr/bin/env python

import random
## models.py
class Game():
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


    def go_first(self):
        self.man      += 1    
        self.machine  += 1    
        return 
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
            self.turn
            return self.man
        else:
            return self.machine
    
    # Display Board
    def print_board(self):
        print "--A-TicTacToe-Game--"
        for i in xrange(3):
            print ' ',
            for j in xrange(3):
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

if __name__ == '__main__':
    #print __name__
    
    g.print_board()

########################

##othwr
import collections
class InvalidLocationError(Exception): pass
import copy
class Board(object):
    def __init__(self, board=None):
        if board is None:
            self.clear()
        else:
            self._board = board[:]

    def place(self, i, row, column):
        if not ((0 <= row <= 2) and (0 <= column <= 2)):
            raise InvalidLocationError("Invalid Location.")
        if self._board[row][column]:
            raise InvalidLocationError("There's already a piece there")
        self._board[row][column] = i
        return self.checkVictory()

    def check(self, row, column):
        return self._board[row][column]

    def checkVictory(self, board=None):
        if board is None:
            board = self._board
        draw = True
        for i in xrange(3):
            r = self.rowcount(i)
            c = self.colcount(i)
            if i < 3:
                d = self.diagcount(i)
            else:
                d = {0: 0, 1: 0, 2: 0}

            for j in xrange(1, 3):
                if d[j] == 3 or r[j] == 3 or c[j] == 3:
                    return j
            if r[0] > 0 or c[0] > 0:
                draw = False
        if draw:
            return -1
        return 0

    def rowcount(self, row):
        return collections.Counter(self._board[row])

    def colcount(self, col):
        return collections.Counter([self._board[i][col] for i in xrange(3)])

    def diagcount(self, left=True):
        if left:
            a = [self._board[0][0], self._board[1][1], self._board[2][2]]
        else:
            a = [self._board[0][2], self._board[1][1], self._board[2][0]]

        return collections.Counter(a)

    def clear(self):
        self._board = ([0, 0, 0], [0, 0, 0], [0, 0, 0])

    def __str__(self):
        return "\n".join(map(lambda x: " ".join(map(lambda y : str(y), x)), self._board))

    @staticmethod
    def flipPiece(p):
        return int(not (p - 1)) + 1

class AI(object):
    class Node(object):
        def __init__(self, board, nextMove):
            self.board = board
            self.nextMove = nextMove
            self.paths = []
            self.score = None

            template = self.board._board[:]
            for r, row in enumerate(template):
                for c, val in enumerate(row):
                    if val == 0:
                        template[r][c] = nextMove
                        self.paths.append(copy.deepcopy(template))
                        template[r][c] = 0

    def __init__(self, mypiece, depth=8):
        self.mypiece = mypiece
        self.enemypiece = Board.flipPiece(mypiece)
        self.depth = depth

    def decide(self, board):
        startNode = self.Node(board, self.mypiece)
        best = self.minimax(startNode, self.depth)
        for node in startNode.paths:
            if node.value == best:
                break
        found = False
        for row in xrange(3):
            for col in xrange(3):
                if board.check(row, col) != node.board.check(row, col):
                    found = True
                    break
            if found:
                break
        print row, col
        return row, col

    def minimax(self, node, depth):
        victory = node.board.checkVictory()
        if victory:
            if victory == self.mypiece:
                h = 1
            elif victory == -1:
                h = 0
            else:
                h = -1
            node.value = h
            return h

        if depth <= 0:
            # h = self.heuristic(node.board, node.nextMove) # This is to the heuristic, which uses nextMove to evalate.
            node.value = 0
            return 0

        h = -1
        flip = Board.flipPiece(node.nextMove)
        for i, board in enumerate(node.paths):
            node.paths[i] = self.Node(Board(board), flip) # This is to the Node, which takes the nextMove of itself (which translates to the next next move from the current node)
            score = self.minimax(node.paths[i], depth-1)
            h = max(h, score) if node.nextMove == self.mypiece else min(h, score)

        node.value = h
        return h