def bfs(obj):
    if obj.is_goal(obj.initial_state):
        return [obj.initial_state]
    else:
         print('the objecttt is:'+str(obj))
    states_to_explore = [[obj.initial_state,[]]]
    print('visited='+str(states_to_explore))

    while states_to_explore:
        state_path = states_to_explore.pop(0)
        state = state_path[0]
        path = state_path[1]

        if obj.is_goal(state):
                return state_path
                
        else:
                children = obj.successors(state)
                newPath = [state] + path
                for child in children:
                    states_to_explore.append([child,newPath])  
                              
    return None