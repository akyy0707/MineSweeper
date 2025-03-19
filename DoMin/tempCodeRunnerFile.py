from Game import Game
from board import board

size = (10, 10)
board = board(size)
screenSize = (800, 800)
game = Game(board, screenSize)
game.run()