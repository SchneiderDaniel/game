import numpy as np
import math


class SudokuBoard:
    def __init__(self, size = 9):
        self.size = size
        self.cellAmount = size*size

        self.gridSize= int(math.sqrt(size))
        self.gridAmount = self.gridSize*self.gridSize

        self.board = np.zeros((size,size),dtype=int,)
        self.board.fill(-1)

    def set(self,x,y,value):
        if self.isCellFilled(x,y): return False
        self.board[x,y]=value
        return True
    
    def get(self,x,y):
        return self.board[x,y]
        
    def isCellFilled(self,x,y):
        return not (self.board[x,y]==-1)

    def isRowContaining(self,row_index,value):
        row=self.board[row_index]
        for cell in row:
            if cell==value: return True
        return False

    def isColContaining(self,col_index,value):
        col=self.board[:,col_index]
        for cell in col:
            if cell==value: return True
        return False

    def gridCoordToCell(self,x,y):
        gridx = x//self.gridSize
        gridy = y//self.gridSize
        return (x,y)

    def isGridContaining(self,gridx,gridy,value):
        
        n1 = np.arange(gridx*self.gridSize,gridx*self.gridSize+3)
        n2 = np.arange(gridy*self.gridSize,gridy*self.gridSize+3)

        for i, j in zip(n1, n2):
            if self.isCellFilled(i,j):
                if self.get(i,j)==value: return True

        return False










