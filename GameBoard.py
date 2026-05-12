import numpy as np
import Piece

class GameBoard: 
    def __init__(self):
        self.currentBoard = np.zeros((25, 10))

    def resetBoard(self):
        self.currentBoard = np.zeros((25, 10))

    def getBoard(self):
        return self.currentBoard
    
    def addPiece(self, Piece):
        newCoords = []

        for c in Piece.getCoordinates():
            r = c[1]
            c = c[0]
            if self.currentBoard[(r + 1,c + 4)] == (2):
                print("Error: Location Already in Use")
            else:
                self.currentBoard[(r + 1,c + 4)] = (2)
                newCoords.append((r + 1,c + 4))

        Piece.setCoordinates(newCoords)