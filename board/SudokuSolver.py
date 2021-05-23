import numpy as np
from board.SudokuBoard import SudokuBoard

class SudokuSolver:

    def __init__(self, algo="Backtracking"):
        self.algo = algo

    def __repr__(self):
        return "SudokuSolver with Algorithm: " + self.algo

    def __eq__(self, other):
        if isinstance(other, SudokuSolver):
            return self.algo==other.algo
        return False

    def solve(self,input):
        if self.algo =="Backtracking":
            return self.solveBacktracking(input)
        if self.algo=="PairsAndLines": 
            return self.solvePairsAndLines(input)
        return None

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

#http://byteauthor.com/2010/08/sudoku-solver-update/
    def solvePairsAndLines(self, input :SudokuBoard):
        solution = input.getCopy()


        lastPlacedNumbersCount = 0
        while ((solution.placedNumberCount - lastPlacedNumbersCount)>3 & solution.placedNumberCount < 68 & solution.placedNumberCount>10):
            lastPlacedNumbersCount = solution.placedNumberCount
            solution.placedNumberCount += self.moveNothingElseAllowed(solution)
            solution.placedNumberCount += self.moveNoOtherRowOrColumnAllowed(solution)
            solution.placedNumberCount += self.moveNothingElseAllowed(solution)

            if (solution.placedNumberCount < 35):
                self.applyNakedPairs(solution)
                self.applyLineCandidateConstraints(solution)
            
        if (solution.placedNumberCount < solution.cellAmount):
            bruteForcedBoard = self.attemptBruteForce(solution)

            if (bruteForcedBoard != None):
                solution.placedNumberCount = 0
                
                print('TODO')
           
        return solution.board

    def moveNothingElseAllowed(self, solution :SudokuBoard):
        moveCount = 0
        
        for ix,iy in np.ndindex(solution.board.shape):
            currentAllowedValues = solution.allowedValues[iy][ix]     
            if (self.countSetBits(currentAllowedValues) == 1):
                solution.setValue(ix, iy)
                moveCount+=1

        return moveCount

    def moveNoOtherRowOrColumnAllowed(self, solution :SudokuBoard):
        return 0

    def moveNothingElseAllowed(self, solution :SudokuBoard):
        return 0

    def applyNakedPairs(self, solution :SudokuBoard):
        return None
    
    def applyLineCandidateConstraints(self, solution :SudokuBoard):
        return None

    def attemptBruteForce(self, solution :SudokuBoard):
        return None