import pytest
from board.SudokuBoard import SudokuBoard
import numpy as np



content0 = np.array([    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                         [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                         [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                         [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                         [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                         [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                         [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                         [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                         [-1,-1,-1,-1,-1,-1,-1,-1,-1]], np.int32)

#https://www.researchgate.net/figure/An-Example-Sudoku-Puzzle-and-its-Solution-1_fig1_264572573
content1 = np.array([    [-1,-1,-1,-1,-1,-1,2,-1,-1],
                         [-1,8,-1,-1,-1,7,-1,9,-1],
                         [6,-1,2,-1,-1,-1,5,-1,-1],
                         [-1,7,-1,-1,6,-1,-1,-1,-1],
                         [-1,-1,-1,9,-1,1,-1,-1,-1],
                         [-1,-1,-1,-1,2,-1,-1,4,-1],
                         [-1,-1,5,-1,-1,-1,6,-1,3],
                         [-1,9,-1,4,-1,-1,-1,7,-1],
                         [-1,-1,6,-1,-1,-1,-1,-1,-1]], np.int32)

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
    assert fullboard1.get(0,0)==-1
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