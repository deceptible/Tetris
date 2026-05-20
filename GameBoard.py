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
            row = c[0]
            col = c[1]

            if self.currentBoard[(row + 1,col + 4)] != (0):
                print("Error: Location Already in Use")

            else:
                self.currentBoard[(row + 1,col + 4)] = (2)

                newCoords.append((row + 1,col + 4))

        Piece.setCoordinates(newCoords)

    def isValidMove(self, Piece, direction):
        if direction == "Left":
            for c in Piece.getCoordinates():
                row = c[0]
                col = c[1]

                if col - 1 < 0:
                    return False
                
                if self.currentBoard[(row, col - 1)] == (1):
                    return False
        
        if direction == "Right":
            for c in Piece.getCoordinates():
                row = c[0]
                col = c[1]

                if col + 1 > 9:
                    return False
                
                if self.currentBoard[(row, col + 1)] == (1):
                    return False
                
        return True

    def shouldLock(self, Piece):
        for c in Piece.getCoordinates():
            row = c[0]
            col = c[1]

            if row + 1 > 24:
                return True
            
            if self.currentBoard[(row + 1, col)] == (1):
                return True
            
        return False

    def moveDown(self, Piece):
        if Piece.getLockStatus() == True:
            return
        
        if self.shouldLock(Piece):
            for c in Piece.getCoordinates():
                self.currentBoard[c] = (1)
            Piece.setLockStatus(True)
            return

        newCoords = []

        for c in Piece.getCoordinates():
            self.currentBoard[c] = (0)

        for c in Piece.getCoordinates():
            row = c[0]
            col = c[1]

            self.currentBoard[(row + 1, col)] = (2)
                
            newCoords.append((row + 1, col))

        Piece.setCoordinates(newCoords)

    def moveLeft(self, Piece):
        if Piece.getLockStatus() == True:
            return
        
        if not self.isValidMove(Piece, "Left"):
            print("Illegal Move")
            return
        
        newCoords = []

        for c in Piece.getCoordinates():
            self.currentBoard[c] = (0)

        for c in Piece.getCoordinates():
            row = c[0]
            col = c[1]

            self.currentBoard[(row, col - 1)] = (2)

            newCoords.append((row, col - 1))

        Piece.setCoordinates(newCoords)

    def moveRight(self, Piece):
        if Piece.getLockStatus() == True:
            return
        
        if not self.isValidMove(Piece, "Right"):
            print("Illegal Move")
            return
        
        newCoords = []

        for c in Piece.getCoordinates():
            self.currentBoard[c] = (0)

        for c in Piece.getCoordinates():
            row = c[0]
            col = c[1]

            self.currentBoard[(row, col + 1)] = (2)

            newCoords.append((row, col + 1))

        Piece.setCoordinates(newCoords)

    def clearLines(self):
        rowsCleared = []

        clearLine = True

        for row in range(24, -1, -1):
            for col in range(0, 10):
                if self.currentBoard[(row, col)] == (0):
                    clearLine = False
            if clearLine == True:
                rowsCleared.append(row)

                for col in range(0, 10):
                    self.currentBoard[(row, col)] = (0)

        if rowsCleared != []:
            for rows in rowsCleared:
                for row in range(rows - 1, -1, -1):
                    for col in range(0, 10):
                        if self.currentBoard[(row, col)] == (1):
                            self.currentBoard[(row, col)] = (0)
                            self.currentBoard[(row + 1, col)] = (1)