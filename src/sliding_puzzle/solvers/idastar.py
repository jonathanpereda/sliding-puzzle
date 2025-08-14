import time
from math import inf
from ..solver_utils import get_neighbors, gen_goal_map, manhattan_dist, goal_state

def idastar(start_state, size, goal=None):

    if goal is None:
        goal = goal_state(size)     #Solution set

    goal_map = gen_goal_map(size)   #Goal map to refrence for manhattan distance
    gofn = 0    #current cost
    fofn = gofn + manhattan_dist(goal_map,start_state,size) #g(n) +   h(n) <- estimated cost to get to goal board

    bound = manhattan_dist(goal_map,start_state,size)   #Start the bound at h(start_state)

    new_bound = inf   #Lowest found f(n) > than bound [changes every attempt]

    ancestor_list = [(start_state, None)]   #Track paths ancestors so it doesnt loop [changes every path]   And keeps track of moves made along this path

    global node_counter    #How many states its visited
    node_counter = 0


    ################ RETURN VARS:
    
    moves = []
    stats = {}


    def parse_branch(current, cur_g, cur_ancestors, bound, new_bound):

        if time.perf_counter() - start_time > 100:
            print("Broke time limit")
            raise SystemExit() 

        if(current == goal):                                            #We found the solution

            #print("Found solution [1]")
            #print("\ncur_ancestors =" + str(cur_ancestors) +"\n")        
            
            return cur_ancestors, new_bound, True
        else:

            for neighbor, move in get_neighbors(current, size):             #Pull all of the next possible states

                global node_counter
                node_counter += 1                                               #++ node counter
                fofn = cur_g+1 + manhattan_dist(goal_map, neighbor, size)          #get the f(n) of this considered state

                if(fofn <= bound and all(node != neighbor for node, _ in cur_ancestors)):            #This new state cheap enough to parse and not in the ancestor list

                    cur_ancestors.append((neighbor, move))
                    foo, dive_new_bound, status = parse_branch(neighbor, cur_g+1, cur_ancestors, bound, new_bound)   #Parse this new state (Increment g(n) and update path's ancestor list)
                    if status:                                                      #Check if solution has been found
                        return cur_ancestors, new_bound, True
                    if dive_new_bound < new_bound:                                  #Get new bound from paths
                        new_bound = dive_new_bound
                    cur_ancestors.pop()                          #Trim ancestors off failed branch path

                elif(fofn > bound and fofn < new_bound):                        #This new state is too expensive or an ancestor
                    new_bound = fofn                                                #Update new bound
                    #print("changing new bound [1]. bound = "+str(bound)+" new bound = "+str(new_bound))

        #print("HERE: newbound = " +str(new_bound))
        return None, new_bound, False

    
    start_time = time.perf_counter()

    while True:
        ret_anc, new_bound, status = parse_branch(start_state, gofn, ancestor_list, bound, new_bound)
        if status:     #Found solution
            #print("Found solution [3]")

            for node, move in ret_anc:
                if move:
                    moves.append(move)

            end_time = time.perf_counter()

            depth = len(moves)

            stats = {
                "nodes_expanded": node_counter,
                "depth": depth,
                "time_ms": (end_time - start_time) * 1000.0,
            }  

            return moves, stats
        else:                                           #Attempt failed
            #print("No solution found, changing bound of: "+str(bound) +" to new bound of: "+str(new_bound))
            bound = new_bound                               #Set new bound for next attempt
            new_bound = inf



    