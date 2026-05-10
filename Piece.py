import numpy as np

class Piece:
    def Transpose(self):
        return np.transpose(self.matrix)

    def Rotate(self):
        transposed = self.Transpose()

        self.matrix = np.fliplr(transposed)
    
    def getMatrix(self):
        return self.matrix

class I(Piece):
    def __init__(self):
        self.matrix = np.array([
            [1, 1, 1, 1]
        ])

class O(Piece):
    def __init__(self):
        self.matrix = np.array([
            [1, 1], 
            [1, 1]
        ])

class T(Piece):
    def __init__(self):
        self.matrix = np.array([
            [0, 1, 0], 
            [1, 1, 1]
        ])

class S(Piece):
    def __init__(self):
        self.matrix = np.array([
            [0, 1, 1], 
            [1, 1, 0]
        ])

class Z(Piece):
    def __init__(self):
        self.matrix = np.array([
            [1, 1, 0], 
            [0, 1, 1]
        ])

class J(Piece):
    def __init__(self):
        self.matrix = np.array([
            [1, 0, 0], 
            [1, 1, 1]
        ])

class L(Piece):
    def __init__(self):
        self.matrix = np.array([
            [0, 0, 1], 
            [1, 1, 1]
        ])