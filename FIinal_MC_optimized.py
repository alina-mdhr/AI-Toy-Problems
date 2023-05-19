import copy
import Final_BFS
class MC():
    def __init__(self,missionary,cannibal,boat_initial,boat_final,boat_capacity):
        self.missionary = missionary
        self.cannibal = cannibal
        self.initial_state = [missionary,cannibal,boat_initial,0,0]
        self.final_state = [0,0,boat_final,missionary,cannibal]
        self.boat_capacity = boat_capacity


    def is_goal(self,curState):
        return(curState==self.final_state)

    def is_valid(self,curState):
        missionaryL = curState[0]
        cannibalL = curState[1]
        missionaryR = curState[3]
        cannibalR = curState[4]
        return ((missionaryL == 0 or missionaryL >= cannibalL) and (missionaryR == 0 or missionaryR >= cannibalR))
            
    
    def successors(self,curState):
        #nextState = copy.deepcopy(curState)
        missionaryL = curState[0]
        cannibalL = curState[1]
        boat_pos = curState[2]
        missionaryR = curState[3]
        cannibalR = curState[4]

        children = []
        capacity = self.boat_capacity + 1 
        for m in range(capacity):
            for c in range(capacity - m):
                if (m > 0 or c > 0) and (m == 0 or m >= c):
                    new_state = [missionaryL+(boat_pos*m),cannibalL+(boat_pos*c),boat_pos*(-1),
                    missionaryR-(boat_pos*m),cannibalR-(boat_pos*c)]
                    if self.is_valid(new_state):
                        children.append(new_state)
        
        return children


    def print_solution(self,solution):
        # sol = solution.reverse()
        print('the solution is:'+ str(solution))

mc = MC(3,3,-1,1,2) #-1 = boat on left side, 1 = boat on right side [missionary,cannibal,boat_initial,boat_final,boat_capacity]
sol = Final_BFS.bfs(mc)
mc.print_solution(sol)