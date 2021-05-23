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
            # print("Iteration: " + str(counter_iter) + " CurrrentValue: " + str(currentValue) + " CurrentPosition: " + str(currentPosition) + " at " + str(listFreeCells[currentPosition][0]) + "/"+ str(listFreeCells[currentPosition][1]) )
            # print(solution)
            
            if currentValue>input.size:
            #    print("Tried all at:" + str(listFreeCells[currentPosition][0]) + "/"+ str(listFreeCells[currentPosition][1])) 
            #    print(solution)
            #    print("Now remove:")

               solution.reset(listFreeCells[currentPosition][0],listFreeCells[currentPosition][1])
            #    print(solution)

               currentPosition-=1
               if currentPosition<0:
                #    print("Error")
                #    print(solution)
                #    print(counter_iter)
                #    print(counter_valueEntered)
                #    print(solution==input)
                   
                   break
               currentValue=solution.get(listFreeCells[currentPosition][0],listFreeCells[currentPosition][1]) 
            #    currentValue+=1
            #    print("next we check:" + str(currentValue) + " at " + str(listFreeCells[currentPosition][0]) + "/"+ str(listFreeCells[currentPosition][1]))
               


            if not solution.enter(listFreeCells[currentPosition][0],listFreeCells[currentPosition][1],currentValue):
                # print("Not added")
                currentValue+=1
            else:
                counter_valueEntered+=1
                # print("Added value: " + str(currentValue) + " at " + str(listFreeCells[currentPosition][0]) + "/"+ str(listFreeCells[currentPosition][1])  )
                # print(solution)
                currentPosition+=1
                currentValue=1
                if currentPosition==(len(listFreeCells)): 
                    solutionFound = True
                    print(solution)

        return solution.board