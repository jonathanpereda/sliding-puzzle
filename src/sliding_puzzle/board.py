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
        #Look at each row
        for row in self.tiles:
            clean_list = []
            #Clean each row into string values
            for val in row:
                if val is not None:
                    clean_list.append(str(val))
                else:
                    clean_list.append(" ")
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
        #Check solvability based on grid size
        if self.size == 3:
            return inversions % 2 == 0
        elif self.size == 4:
            return False
        else:
            return False

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
            print("ERROR: Failed to find a solvable board")
            print("Reverting to solved board...")
            self.tiles = self._generate_tiles()

        
                