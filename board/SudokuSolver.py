import numpy as np
from board.SudokuBoard import SudokuBoard

class SudokuSolver:

    def __init__(self, algo="backtracking"):
        self.algo = algo

    def __repr__(self):
        return "SudokuSolver with Algorithm: " + self.algo

    def __eq__(self, other):
        if isinstance(other, SudokuSolver):
            return self.algo==other.algo
        return False

    def solve(self,input):
        if self.algo =="backtracking":
            return self.solveBacktracking(input)
        else: return None

    def solveBacktracking(self, input :SudokuBoard):
        solution = input.getCopy()
        
        listFreeCells=input.getFreeCellsAsList()
        currentPosition=0
        currentValue = 1
        solutionFound = False
        counter_iter = 0
        counter_valueEntered = 0

        while not solutionFound:
            counter_iter+=1     
            if currentValue>input.size:
               solution.reset(listFreeCells[currentPosition][0],listFreeCells[currentPosition][1])
               currentPosition-=1
               if currentPosition<0:
           
                   break
               currentValue=solution.get(listFreeCells[currentPosition][0],listFreeCells[currentPosition][1]) 

            if not solution.enter(listFreeCells[currentPosition][0],listFreeCells[currentPosition][1],currentValue):
                currentValue+=1
            else:
                counter_valueEntered+=1

                currentPosition+=1
                currentValue=1
                if currentPosition==(len(listFreeCells)): 
                    solutionFound = True
                    print(solution)

        return solution.board


        