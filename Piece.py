import numpy as np

class Piece:
    def Rotate(self):
        pass

class I:
    def __init__(self):
        self.grid = np.array([
            [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [1, 1, 1, 1]
            ])

class O:
    def __init__(self):
        self.grid = np.array([
            [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 1, 1, 0], 
            [0, 1, 1, 0]
            ])
class T:
    def __init__(self):
        self.grid = np.array([
            [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 1, 0], 
            [0, 1, 1, 1]
            ])
class S:
    def __init__(self):
        self.grid = np.array([
            [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 1, 1], 
            [0, 1, 1, 0]
            ])
class Z:
    def __init__(self):
        self.grid = np.array([
            [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 1, 1, 0], 
            [0, 0, 1, 1]
            ])
class J:
    def __init__(self):
        self.grid = np.array([
            [0, 0, 0, 0], 
            [0, 0, 1, 0], 
            [0, 0, 1, 0], 
            [0, 1, 1, 0]
            ])
class L:
    def __init__(self):
        self.grid = np.array([
            [0, 0, 0, 0], 
            [0, 1, 0, 0], 
            [0, 1, 0, 0], 
            [0, 1, 1, 0]
            ])