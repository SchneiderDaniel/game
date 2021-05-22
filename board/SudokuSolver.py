import numpy as np

class SudokuSolver:

    def __init__(self, algo="default"):
        self.algo = algo

    def __repr__(self):
        return "SudokuSolver with Algorithm: " + self.algo

    def __eq__(self, other):
        if isinstance(other, SudokuSolver):
            return self.algo==other.algo
        return False

    def solve(self,input):
        if self.algo =="default":
            return self.solveDefault(input)
        else: return None

    def solveDefault(self,input):
        return input.board