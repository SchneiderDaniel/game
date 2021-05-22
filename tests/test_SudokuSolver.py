import pytest
from board.SudokuSolver import SudokuSolver
from board.SudokuBoard import SudokuBoard
import numpy as np



#https://www.researchgate.net/figure/An-Example-Sudoku-Puzzle-and-its-Solution-1_fig1_264572573
content = np.array([    [-1,-1,-1,-1,-1,-1,2,-1,-1],
                         [-1,8,-1,-1,-1,7,-1,9,-1],
                         [6,-1,2,-1,-1,-1,5,-1,-1],
                         [-1,7,-1,-1,6,-1,-1,-1,-1],
                         [-1,-1,-1,9,-1,1,-1,-1,-1],
                         [-1,-1,-1,-1,2,-1,-1,4,-1],
                         [-1,-1,5,-1,-1,-1,6,-1,3],
                         [-1,9,-1,4,-1,-1,-1,7,-1],
                         [-1,-1,6,-1,-1,-1,-1,-1,-1]], np.int32)
                         #

solution = np.array([    [9,5,7,6,1,3,2,8,4],
                         [4,8,3,2,5,7,1,9,6],
                         [6,1,2,8,4,9,5,3,7],
                         [1,7,8,3,6,4,9,5,2],
                         [5,2,4,9,7,1,3,6,8],
                         [3,6,9,5,2,8,7,4,1],
                         [8,4,5,7,9,2,6,1,3],
                         [2,9,1,4,3,6,8,7,5],
                         [7,3,6,1,8,5,4,2,9]], np.int32)


fullboard = SudokuBoard(9)
fullboard.fill(content)

solver=SudokuSolver()

def testSolution():
    assert solution==solver.solve(fullboard)