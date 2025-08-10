import random

class Board:

    def __init__(self, size, start_shuffled=False):
        self.size = size
        self.tiles = self._generate_tiles()
        if start_shuffled:
            self.shuffle()

    def _generate_tiles(self):
        #Create the flat list of numbers based on board size including an empty space: None
        flat_list = self.solved_flat()

        #Compile our flat list into a grid 
        return self.flat_to_grid(flat_list)
    
    def display(self):
        cell_width = len(str(self.size*self.size - 1))
        #Look at each row
        for row in self.tiles:
            clean_list = []
            #Clean each row into string values
            for val in row:
                s = "" if val is None else str(val)
                s = f"{s:>{cell_width}}"
                clean_list.append(s)
            print(" | ".join(clean_list))

    def solved_flat(self):
        #Create the flat list of numbers based on board size including an empty space: None
        return list(range(1, self.size**2)) + [None]

    def flatten_grid(self):
        flat_list = []
        #Flatten grid into a single list ignoring None
        for row in self.tiles:
            for val in row:
                if val is not None:
                    flat_list.append(val)
        return flat_list
    
    def flat_to_grid(self, flat):
        rows = []
        for start in range(0, len(flat), self.size):
            rows.append(flat[start:start+self.size])

        return rows
    
    def count_inversions(self, flat):
        count = 0
        #Check every number and see if all numbers after it are smaller than it
        for i in range(0,len(flat)-1):
            for j in range(i+1,len(flat)):
                if flat[i] > flat [j]:
                    count = count + 1
        return count
    
    def is_solvable(self):
        #Pull the current grids inversion count
        flat = self.flatten_grid()
        inversions = self.count_inversions(flat)
        blank_row = self.get_blanks_row()
        #Check solvability based on grid size
        if self.size % 2 == 1:
            return inversions % 2 == 0
        elif self.size % 2 == 0:
            return (blank_row % 2 == 0 and inversions % 2 == 1) or (blank_row % 2 == 1 and inversions % 2 == 0)
        else:
            return False
        
    def is_solved(self):
        return self.flat_to_grid(self.solved_flat()) == self.tiles
        
    def get_blanks_row(self):
        #Grabs row number that has blank on it. 1-indexed from bottom
        for i, row in enumerate(self.tiles):
            for val in row:
                if val is None:
                    return self.size - i
        raise ValueError("ERROR: Could not find row containing [blank]")

    def shuffle(self):
        #Start with solved flat
        solved = self.solved_flat()
        attempts = 0
        max_attempts = 1000
        while attempts < max_attempts:
            attempts += 1
            #Create clone of solved flat and shuffle it
            shuffled = solved[:]
            random.shuffle(shuffled)
            #Update current board to shuffled and test solvability
            self.tiles = self.flat_to_grid(shuffled)
            if self.is_solvable() and shuffled != solved:
                break
        if attempts == max_attempts:
            raise ValueError("ERROR: Failed to find a solvable board")
            #print("ERROR: Failed to find a solvable board")
            #print("Reverting to solved board...")
            #self.tiles = self._generate_tiles()

    def find_blank(self):
        #Search current grid for None value, return 0-indexed (r,c)
        for i, row in enumerate(self.tiles):
            for j, val in enumerate(row):
                if val is None:
                    return (i,j)
        raise ValueError("ERROR: Failed to find blank space")
    
    def legal_moves(self):
        blank_r, blank_c = self.find_blank()
        legal_list = []
        if blank_r < self.size - 1:
            legal_list.append("U")
        if blank_r > 0:
            legal_list.append("D")
        if blank_c < self.size - 1:
            legal_list.append("L")
        if blank_c > 0:
            legal_list.append("R")
        if not legal_list:
            raise ValueError("ERROR: No legal moves")
        return legal_list
    
    def do_move(self, dir):
        if dir in self.legal_moves():
            #Swap place of blank and pushed tile based on delta transformations
            #Return true for success and false for illegal moves
            blank_r, blank_c = self.find_blank()
            deltas = {"U": (1,0), "D": (-1,0), "L": (0,1), "R": (0,-1)}
            dr, dc = deltas[dir]
            pr, pc = blank_r + dr, blank_c + dc

            self.tiles[blank_r][blank_c], self.tiles[pr][pc] = self.tiles[pr][pc], self.tiles[blank_r][blank_c]
            return True
        else:
            return False

    def to_state(self):
        flat_list = []
        #Flatten grid into a single tuple replacing None with 0
        for row in self.tiles:
            for val in row:
                if val is not None:
                    flat_list.append(val)
                else:
                    flat_list.append(0)
        return tuple(flat_list)