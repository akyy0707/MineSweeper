import random
from piece import Piece

class board():
    def __init__(self, size, prob):
        self.size = size
        self.prob = prob
        self.setboard()
        self.setNeighbors()
        for row in self.board:
            for piece in row:
                piece.setNumAround()
        
    def setboard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                bomb = random.random() < self.prob
                piece = Piece(bomb)
                row.append(piece)
            self.board.append(row)

    def setNeighbors(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                piece = self.board[row][col]
                neighbors = []
                self.addToNeighborsList(neighbors, row, col)
                piece.setNeighbors(neighbors)

    def addToNeighborsList(self, neighbors, row, col):
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r == row and c == col:
                    continue
                if r < 0 or r >= self.size[0] or c < 0 or c >= self.size[1]:
                    continue
                neighbors.append(self.board[r][c])
        
    def getSize(self):
        return self.size

    def getBoard(self):
        return self.board
                
        