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

    def __repr__(self):
        result = "" 
        for row in self.board:  
            result+= "|" + row + "|" +"\n"

        return result

    def fill(self,values):
        if  values.shape != self.board.shape: return False
        self.board = values
        return True

    def isFilled(self):
        for cell in np.nditer(self.board):
            if cell!=-1: return True
        return False

    def enter(self,x,y,value):
        result = self.isEnterValid(x,y,value)
        if result: self.board[x,y]=value
        return result

    def isEnterValid(self,x,y,value):
        if self.isCellFilled(x,y): return False
        if self.isColOfCellConatining(x,y,value): return False
        if self.isRowOfCellConatining(x,y,value): return False
        if self.isGridOfCellContaining(x,y,value): return False
        return True
    
    def get(self,x,y):
        return self.board[x,y]
        
    def isCellFilled(self,x,y):
        return not (self.board[x,y]==-1)

    def isRowOfCellConatining(self,x,y,value):
        return self.isRowContaining(x,value)

    def isRowContaining(self,row_index,value):
        row=self.board[row_index]
        for cell in row:
            if cell==value: return True
        return False

    def isColOfCellConatining(self,x,y,value):
        return self.isColContaining(y,value)

    def isColContaining(self,col_index,value):
        col=self.board[:,col_index]
        for cell in col:
            if cell==value: return True
        return False
 
    def gridCoordToCell(self,x,y):
        gridx = x//self.gridSize
        gridy = y//self.gridSize
        return (gridx,gridy)

    def isGridOfCellContaining(self,x,y,value):
        grid = self.gridCoordToCell(x,y)
        check = self.isGridContaining(grid[0],grid[1],value)
        return check

    def isGridContaining(self,gridx,gridy,value):
        
        n1 = np.arange(gridx*self.gridSize,gridx*self.gridSize+3)
        n2 = np.arange(gridy*self.gridSize,gridy*self.gridSize+3)

        for i, j in zip(n1, n2):
            if self.isCellFilled(i,j):
                if self.get(i,j)==value: return True

        return False   
    




   

    











