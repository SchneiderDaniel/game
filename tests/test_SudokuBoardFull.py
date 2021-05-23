import pytest
from board.SudokuBoard import SudokuBoard
import numpy as np



content0 = np.array([    [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0]], np.int32)

#https://www.researchgate.net/figure/An-Example-Sudoku-Puzzle-and-its-Solution-1_fig1_264572573
content1 = np.array([    [0,0,0,0,0,0,2,0,0],
                         [0,8,0,0,0,7,0,9,0],
                         [6,0,2,0,0,0,5,0,0],
                         [0,7,0,0,6,0,0,0,0],
                         [0,0,0,9,0,1,0,0,0],
                         [0,0,0,0,2,0,0,4,0],
                         [0,0,5,0,0,0,6,0,3],
                         [0,9,0,4,0,0,0,7,0],
                         [0,0,6,0,0,0,0,0,0]], np.int32)

emptyBoard = SudokuBoard(9)
fullboard0 = SudokuBoard(9)
fullboard0.fill(content0)
fullboard1 = SudokuBoard(9)
fullboard1.fill(content1)
fullboard1copy = fullboard1.getCopy()


def testisEqual1():
    assert fullboard1==fullboard1copy

def testisEqual2():
    assert emptyBoard==fullboard0

def testisEqual3():
    assert (emptyBoard!=fullboard0)==False

def testisEqual4():
    assert (fullboard1!=fullboard1copy)==False

def testisFilled0():
    assert fullboard0.isFilled()==False

def testisFilled1():
    assert fullboard1.isFilled()==True

def testGet1():
    assert fullboard1.get(0,0)==0
def testGet2():
    assert fullboard1.get(1,1)==8
def testGet3():
    assert fullboard1.get(2,2)==2
def testGet4():
    assert fullboard1.get(8,6)==3
def testGet5():
    assert fullboard1.get(7,7)==7
def testGet6():
    assert fullboard1.get(2,8)==6

def testIsColContaining1():
    assert fullboard1.isColContaining(0,6)==True

def testIsColContaining2():
    assert fullboard1.isColContaining(2,4)==False

def testIsColContaining3():
    assert fullboard1.isColContaining(6,5)==True

def testIsColContaining4():
    assert fullboard1.isColContaining(8,4)==False

def testIsRowContaining1():
    assert fullboard1.isRowContaining(0,2)==True

def testIsRowContaining2():
    assert fullboard1.isRowContaining(3,4)==False

def testIsRowContaining3():
    assert fullboard1.isRowContaining(6,5)==True

def testIsRowContaining4():
    assert fullboard1.isRowContaining(8,1)==False

def testIsRowOfCellConatining1():
    assert fullboard1.isRowOfCellConatining(2,1,8)==True

def testIsRowOfCellConatining2():
    assert fullboard1.isRowOfCellConatining(2,1,1)==False

def testIsRowOfCellConatining3():
    assert fullboard1.isRowOfCellConatining(8,7,1)==False

def testIsRowOfCellConatining3():
    assert fullboard1.isRowOfCellConatining(8,7,7)==True

def testIsColOfCellConatining1():
    assert fullboard1.isColOfCellConatining(2,7,1)==False

def testIsColOfCellConatining1():
    assert fullboard1.isColOfCellConatining(2,7,5)==True

def testIsColOfCellConatining3():
    assert fullboard1.isColOfCellConatining(6,1,2)==True

def testIsColOfCellConatining3():
    assert fullboard1.isColOfCellConatining(6,1,9)==False

def testIsGridOfCellContaining1():
    assert fullboard1.isGridOfCellContaining(0,0,2)==True

def testIsGridOfCellContaining2():
    assert fullboard1.isGridOfCellContaining(0,0,3)==False

def testIsGridOfCellContaining3():
    assert fullboard1.isGridOfCellContaining(8,8,6)==True

def testIsGridOfCellContaining4():
    assert fullboard1.isGridOfCellContaining(8,8,1)==False

def testIsGridOfCellContaining5():
    assert fullboard1.isGridOfCellContaining(3,3,6)==True

def testIsGridOfCellContaining6():
    assert fullboard1.isGridOfCellContaining(3,3,4)==False


def testIsGridOfCellContaining7():
    assert fullboard1.isGridOfCellContaining(4,7,4)==True


def testIsGridOfCellContaining8():
    assert fullboard1.isGridOfCellContaining(4,7,2)==False

def testIsEnterValid1():
    assert fullboard1.isEnterValid(2,7,4)==False

def testIsEnterValid2():
    assert fullboard1.isEnterValid(2,7,9)==False

def testIsEnterValid3():
    assert fullboard1.isEnterValid(2,7,6)==False

def testIsEnterValid4():
    assert fullboard1.isEnterValid(2,7,2)==False

def testIsEnterValid5():
    assert fullboard1.isEnterValid(2,7,7)==False


def testIsEnterValid6():
    assert fullboard1.isEnterValid(2,7,1)==True


def testIsEnterValid7():
    assert fullboard1.isEnterValid(2,7,8)==True

def testEnter():

    temp = fullboard1.getCopy()

    temp.enter(0,0,3)

    assert temp!=fullboard1

def testMask():
    allowed = fullboard1.allowedValues[0][0]
    assert allowed==int("0101011101", 2)

def testMask2():
    allowed = fullboard1.allowedValues[7][8]
    
    assert allowed==int("0010010011", 2)

def testMask3():
    allowed = fullboard1.allowedValues[0][3]
    
    assert allowed==int("0010110101", 2)

def testMask4():
    allowed = fullboard1.allowedValues[8][8]
    
    assert allowed==int("0110011011", 2) 

def testMask5():
    allowed = fullboard1.allowedValues[8][5]
    
    assert allowed==int("0110011110", 2) 
    
def testCountBit1():
    assert fullboard1.countSetBits(8,8)==6

def testCountBit2():    
    assert fullboard1.countSetBits(3,0)==5

def testCountBit3():
    assert fullboard1.countSetBits(8,7)==4

def testLastBit1():
    assert fullboard1.getLastSetBitIndex(8,8)==0

def testLastBit2():
    assert fullboard1.getLastSetBitIndex(3,0)==0

def testLastBit3():
    assert fullboard1.getLastSetBitIndex(5,8)==1

