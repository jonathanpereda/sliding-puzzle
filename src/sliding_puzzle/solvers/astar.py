from collections import deque
from math import inf
import time, heapq
from itertools import count
from ..solver_utils import get_neighbors, gen_goal_map, manhattan_dist, goal_state

def astar(start_state, size, goal=None):

    if goal is None:
        goal = goal_state(size)

    goal_map = gen_goal_map(size)   #Goal map to refrence for manhattan distance
    gofn = 0    #current cost
    fofn = gofn + manhattan_dist(goal_map,start_state,size) #g(n) +   h(n) <- estimated cost to get to goal board

    tie = count()
    heap_queue = [(fofn, -gofn, next(tie), start_state)]     #Heap (f(n), g(n), id, state)

    closed = set()    #List of states that we've closed when we visted then at lower g cost
    g_costs = {start_state: 0}  #Keep track of the costs we've seen at different states

    parent = {start_state: (None, None)}    #Dictionary of: Key = state, value = (previous state, move taken)

    node_counter = 0    #How many states have been taken out of the queue

    start_time = time.perf_counter()


    while heap_queue:
        fofn, neg_gofn, sid, current = heapq.heappop(heap_queue)
        gofn = -neg_gofn

        if(gofn > g_costs.get(current, inf)):       #Check that we dont have a better version of this state already
            continue

        if current == goal:     
            moves = []
            node = current
            while True:
                prev, mv = parent[node]     #Using the key of the current node save prev state and move made
                if prev is None:
                    break
                moves.append(mv)
                node = prev     #Load new prev state in as "current" to continue walk-back
            moves.reverse()

            depth = len(moves)
            end_time = time.perf_counter()
            stats = {
                "nodes_expanded": node_counter,
                "depth": depth,
                "time_ms": (end_time - start_time) * 1000.0,
            }
            return moves, stats
        
        closed.add(current)
        node_counter += 1

        for neighbor, move in get_neighbors(current, size):
            cur_g = gofn + 1
            if neighbor not in closed and cur_g < g_costs.get(neighbor, inf): #Check that we dont have a better version of this neighbor already
                g_costs[neighbor] = cur_g
                parent[neighbor] = (current, move)
                fofn = cur_g + manhattan_dist(goal_map,neighbor,size)
                heapq.heappush(heap_queue, (fofn, -cur_g, next(tie), neighbor))


    end_time = time.perf_counter()
    return None