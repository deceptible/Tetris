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

        for c in Piece.getRelCoordinates():
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

    def canRotate(self, Piece):
        coord = Piece.getRelCoordinates()

        for coords in range(len(coord)):
            r = coord[coords][0]
            c = coord[coords][1]
            coord[coords] = (c,r)
        
        maxcol = 0
        mincol = 0

        for coords in range(len(coord)):
            if coord[coords][1] > maxcol:
                maxcol = coord[coords][1]
            if coord[coords][1] < mincol:
                mincol = coord[coords][1]

        columns = maxcol - mincol

        for coords in range(len(coord)):
            r = coord[coords][0]
            c = coord[coords][1]
            coord[coords] = (r,(columns - 1) - c)

        for coords in coord:
            if self.currentBoard[(coords)] == (1):
                return False
            
        return True

    def rotatePiece(self, Piece):
        if not self.canRotate(Piece):
            return

        for c in Piece.getCoordinates():
            self.currentBoard[(c)] = (0)

        coords = Piece.getCoordinates()
        relCoords = Piece.getRelCoordinates()
        adjustment = []

        for c in range(len(coords)):
            row = coords[c][0]
            col = coords[c][1]

            relRow = relCoords[c][0]
            relCol = relCoords[c][1]

            adjustment.append((row - relRow, col - relCol))

        Piece.Rotate()
        newRelCoords = Piece.getRelCoordinates()
        newCoords = []

        for c in range(len(newRelCoords)):
            row = newRelCoords[c][0]
            col = newRelCoords[c][1]

            adjRow = adjustment[c][0]
            adjCol = adjustment[c][1]

            newCoords.append((row + adjRow, col + adjCol))

        for c in newCoords:
            self.currentBoard[c] = (2)

        Piece.setCoordinates(newCoords)

b = GameBoard()
i = Piece.I()
b.addPiece(i)
b.rotatePiece(i)
print(i.getCoordinates())
print(b.getBoard())
# The coordinates for both are messed up. The canRotate is using relative coords without converting to the actual position on the gameBoard. The Rotate has messed up the conversion.