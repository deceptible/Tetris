import numpy as np

class Piece:
    isLocked = False

    def Transpose(self):
        for coords in range(len(self.coordinates)):
            r = self.coordinates[coords][0]
            c = self.coordinates[coords][1]
            self.coordinates[coords] = (c,r)

        return np.transpose(self.matrix)

    def Rotate(self):
        transposed = self.Transpose()

        columns = transposed.shape[1]

        for coords in range(len(self.coordinates)):
            r = self.coordinates[coords][0]
            c = self.coordinates[coords][1]
            self.coordinates[coords] = (r,(columns - 1) - c)

        self.matrix = np.fliplr(transposed)
    
    def getMatrix(self):
        return self.matrix
    
    def getCoordinates(self):
        return self.coordinates
    
    def setCoordinates(self, coords):
        self.coordinates = coords

    def setLockStatus(self, state):
        self.isLocked = state

    def getLockStatus(self):
        return self.isLocked

class I(Piece):
    def __init__(self):
        self.matrix = np.array([
            [1, 1, 1, 1]
        ])
        self.coordinates = [(0,0), (0,1), (0,2), (0,3)]

class O(Piece):
    def __init__(self):
        self.matrix = np.array([
            [1, 1], 
            [1, 1]
        ])
        self.coordinates = [(0,0), (0,1), (1,0), (1,1)]

class T(Piece):
    def __init__(self):
        self.matrix = np.array([
            [0, 1, 0], 
            [1, 1, 1]
        ])
        self.coordinates = [(0,1), (1,0), (1,1), (1,2)]

class S(Piece):
    def __init__(self):
        self.matrix = np.array([
            [0, 1, 1], 
            [1, 1, 0]
        ])
        self.coordinates = [(0,1), (0,2), (1,0), (1,1)]

class Z(Piece):
    def __init__(self):
        self.matrix = np.array([
            [1, 1, 0], 
            [0, 1, 1]
        ])
        self.coordinates = [(0,0), (0,1), (1,1), (1,2)]

class J(Piece):
    def __init__(self):
        self.matrix = np.array([
            [1, 0, 0], 
            [1, 1, 1]
        ])
        self.coordinates = [(0,0), (1,0), (1,1), (1,2)]

class L(Piece):
    def __init__(self):
        self.matrix = np.array([
            [0, 0, 1], 
            [1, 1, 1]
        ])
        self.coordinates = [(0,2), (1,0), (1,1), (1,2)]