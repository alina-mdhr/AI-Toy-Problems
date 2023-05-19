import copy
import Final_BFS
class Puzzle():
    def __init__(self,initial_state, row, col, goal_state, rowG, colG):
        self.initial_state = [initial_state, row, col]
        self.goal_state = [goal_state, rowG, colG]
        self.size = len(initial_state)

    def is_goal(self,curState):
        #self.curState = curState
        return(curState[0]==self.goal_state[0])

    def is_valid(self, row, col):
        return(row >= 0 and row < self.size and col >= 0 and col < self.size)


    def Move(self, curState, row, col, i, j):
        nextState = copy.deepcopy(curState)
        if not(i==0):
            nextState[row][col] = nextState[row+i][col] 
            nextState[row+i][col] = 0

        if not(j==0):
            nextState[row][col] = nextState[row][col+j]
            nextState[row][col+j] = 0
  

        return([nextState, row+i, col+j]) 

    def successors(self, curState_row_col):
        curState = curState_row_col[0]
        row = curState_row_col[1]
        col = curState_row_col[2]
        children = []

        for i in [-1,1]:
            if (self.is_valid(row+i, col)): children.append(self.Move(curState, row, col, i, 0))
            if (self.is_valid(row, col+i)): children.append(self.Move(curState, row, col, 0, i))

        return(children)

    def print_solution(self,solution):
        length = len(solution)
        print('length of solution = '+ str(length))
        print('the solution is:'+ str(solution))
        #print('the solution is:'+ str(solution[1][0]))

        

ep = Puzzle([[0,2,3],[1,5,6],[4,7,8]],0,0,[[1,2,3],[4,5,6],[7,8,0]],2,2)
sol = Final_BFS.bfs(ep)
ep.print_solution(sol)








 