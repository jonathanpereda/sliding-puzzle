class Board:

    def __init__(self, size):
        self.size = size
        self.tiles = self._generate_tiles()

    def _generate_tiles(self):
        #Create the flat list of numbers based on board size including an empty space: None
        flat_list = list(range(1, self.size**2)) + [None]

        #Compile our flat list into a grid 
        rows = []
        for start in range(0, len(flat_list), self.size):
            rows.append(flat_list[start:start+self.size])

        return rows
    
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

    def flatten_grid(self):
        flat_list = []
        #Flatten grid into a single list ignoring None
        for row in self.tiles:
            for val in row:
                if val is not None:
                    flat_list.append(val)
        return flat_list
    
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



