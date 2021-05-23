import numpy as np
import math
import copy
from random import shuffle

class SudokuBoard:

    def __init__(self, size = 9):
        self.size = size
        self.cellAmount = size*size

        self.gridSize= int(math.sqrt(size))
        self.gridAmount = self.gridSize*self.gridSize

        self.board = np.zeros((size,size),dtype=int,)
        self.board.fill(0)

        self.allowedBitFields = np.array([
            0,
            1,
            1 << 1,
            1 << 2,
            1 << 3,
            1 << 4,
            1 << 5,
            1 << 6,
            1 << 7,
            1 << 8,], dtype=np.int32)

        self.allAllowed=self.allowedBitFields.sum()

        self.allowedValues = np.zeros((size, size), dtype = int)

        for ix,iy in np.ndindex(self.allowedValues.shape):
            self.allowedValues[ix][iy] = self.allAllowed

        self.placedNumberCount = 0


    def __repr__(self):
        return str(self.board)

    def __eq__(self, other):
        if isinstance(other, SudokuBoard):
            return np.array_equal(self.board,other.board)
        return False

    def getCopy(self):
        return copy.deepcopy(self)
        
    def fill(self,values):
        if  values.shape != self.board.shape: return False
        self.board = values

        for ix,iy in np.ndindex(self.board.shape):
            if(self.board[iy][ix])>0:
                self.allowedValues[iy][ix] = 0
                self.applyAllowedValuesMask(ix,iy)
                self.placedNumberCount+=1

        return True


    def applyAllowedValuesMask(self,x,y):

        if ((x==5) & (y==1)):
            print('Here')

        mask = ~self.allowedBitFields[self.board[y][x]]

        for maskApplyY in range(0,self.size):
            self.allowedValues[maskApplyY][x] &=mask

        allowedValuesRow = self.allowedValues[y]

        for maskApplyX in range(0,self.size):
            allowedValuesRow[maskApplyX] &=mask

        sectionX1 = 0
        sectionX2 = 0

        if x==0:
            sectionX1 = x + 1
            sectionX2 = x + 2
        elif x==1:
            sectionX1 = x - 1
            sectionX2 = x + 1
        elif x==2:
            sectionX1 = x - 2
            sectionX2 = x - 1
        elif x==3:
            sectionX1 = x + 1
            sectionX2 = x + 2
        elif x==4:
            sectionX1 = x - 1
            sectionX2 = x + 1
        elif x==5:
            sectionX1 = x - 2
            sectionX2 = x - 1
        elif x==6:
            sectionX1 = x + 1
            sectionX2 = x + 2
        elif x==7:
            sectionX1 = x - 1
            sectionX2 = x + 1
        elif x==8:
            sectionX1 = x - 2
            sectionX2 = x - 1
        else:
            print("Error4984191")


        sectionY1 = 0
        sectionY2 = 0

        if y==0:
            sectionY1 = y + 1
            sectionY2 = y + 2
        elif y==1:
            sectionY1 = y - 1
            sectionY2 = y + 1
        elif y==2:
            sectionY1 = y - 2
            sectionY2 = y - 1
        elif y==3:
            sectionY1 = y + 1
            sectionY2 = y + 2
        elif y==4:
            sectionY1 = y - 1
            sectionY2 = y + 1
        elif y==5:
            sectionY1 = y - 2
            sectionY2 = y - 1
        elif y==6:
            sectionY1 = y + 1
            sectionY2 = y + 2
        elif y==7:
            sectionY1 = y - 1
            sectionY2 = y + 1
        elif y==8:
            sectionY1 = y - 2
            sectionY2 = y - 1
        else:
            print("Error49849851")

        allowedValuesRow1 = self.allowedValues[sectionY1]
        allowedValuesRow2 = self.allowedValues[sectionY2]
        
        allowedValuesRow1[sectionX1] &= mask
        allowedValuesRow1[sectionX2] &= mask
        allowedValuesRow2[sectionX1] &= mask
        allowedValuesRow2[sectionX2] &= mask


    def isFilled(self):
        for cell in np.nditer(self.board):
            if cell!=0: return True
        return False

    def enter(self,x,y,value):
        result = self.isEnterValid(x,y,value)
        if result: self.board[y,x]=value
        return result
    
    def reset(self,x,y):
        self.board[y,x]=0

    def isEnterValid(self,x,y,value):
        if self.isColOfCellConatining(x,y,value): return False
        if self.isRowOfCellConatining(x,y,value): return False
        if self.isGridOfCellContaining(x,y,value): return False
        return True
    
    def get(self,x,y):
        return self.board[y,x]
        
    def isCellFilled(self,x,y):
        return not (self.board[y,x]==0)

    def getFreeCellsAsList(self):
        result = []
        for ix,iy in np.ndindex(self.board.shape):
            if not self.isCellFilled(ix,iy):
                result.append((ix,iy))
        # print(result)
        # shuffle(result)
        # print(result)
        return result

    def isRowOfCellConatining(self,x,y,value):
        return self.isRowContaining(y,value)

    def isRowContaining(self,row_index,value):
        row=self.board[row_index]
        for cell in row:
            if cell==value: return True
        return False

    def isColOfCellConatining(self,x,y,value):
        return self.isColContaining(x,value)

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
        for i in n1:
            for j in n2:
                if self.isCellFilled(i,j):
                    if self.get(i,j)==value: return True
        return False   
    




   

    











