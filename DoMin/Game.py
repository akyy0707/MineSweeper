import pygame
import os

class Game():
    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        self.pieceSize = self.screenSize[0] // self.board.getSize()[0], self.screenSize[1] // self.board.getSize()[1]
        self.loadImages()
    
    def run(self):
        pygame.init()   
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw()
            pygame.display.flip()
        pygame.quit()
        
    def draw(self):
        topLeft = (0, 0)
        for row in self.board.getBoard():
            for piece in row:
                image = self.images[self.getImageString(piece)]
                self.screen.blit(image, topLeft)
                topLeft = (topLeft[0] + self.pieceSize[0], topLeft[1])
            topLeft = (0, topLeft[1] + self.pieceSize[1])
            
    def loadImages(self):
        self.images = {}
        for fileName in os.listdir("DoMin/images"):
            if not fileName.endswith(".png"):
                continue
            image = pygame.image.load(os.path.join("DoMin/images/", fileName))
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image
    
    def getImageString(self, piece):
        if piece.hasBomb:
            return 'bomb-at-clicked-block'
        elif piece.getNumAround != 0:
            return str(piece.getNumAround())
        # if (self.board.getLost()):
        #     if (piece.getHasBomb()):
        #         return 'unclicked-bomb'
        #     return 'wrong-flag' if piece.getFlagged() else 'empty-block'
        # return 'flag' if piece.getFlagged() else 'empty-block'
        return 'empty-block'