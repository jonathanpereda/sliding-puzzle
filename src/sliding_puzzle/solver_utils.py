
def goal_state(size):
    flat_list = []
    for i in range (size*size -1):
        flat_list.append(i+1)
    flat_list.append(0)
    return tuple(flat_list)

def get_neighbors(state, size):

    neighbors = []

    #get index of blank_index
    bi = state.index(0)
    #translate blank_index into row and collumn
    r, c = divmod(bi, size)

    deltas = {"U": (1,0), "D": (-1,0), "L": (0,1), "R": (0,-1)}

    for move in "UDLR":
        #get row and collumn for current delta translation
        dr, dc = deltas[move]
        #get tile were looking to move (source tile)
        sr, sc = r + dr, c + dc

        #Check if source tile is out of bounds
        if not (0 <= sr < size and 0 <= sc < size):
            continue

        #Swap blank tile with source tile
        s_idx = sr * size + sc
        lst = list(state)
        lst[bi], lst[s_idx] = lst[s_idx], lst[bi]
        #Save tuple of new state
        ns = tuple(lst)
        
        #Append to neighbors list 
        neighbors.append((ns, move))

    return neighbors
