from collections import deque
import time
from ..solver_utils import get_neighbors, goal_state

def bfs(start_state, size, goal=None):

    if goal is None:
        goal = goal_state(size)

    queue = deque([start_state])    #List of states that we need to visit
    visited = set([start_state])    #List of states that we have already visited
    parent = {start_state: (None, None)}    #Dictionary of: Key = state, value = (previous state, move taken)

    node_counter = 0    #How many states have been taken out of the queue

    start_time = time.perf_counter()

    while queue:
        current = queue.popleft()
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
            
        else:
            for neighbor, move in get_neighbors(current, size):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = (current, move)
                    queue.append(neighbor)

        node_counter += 1

    end_time = time.perf_counter()
    return "No solution found"