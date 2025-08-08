class Board:

    def __init__(self, size):
        self.size = size
        self.tiles = self._generate_tiles()

    def _generate_tiles(self):
        #Create the flat list of numbers based on board size including an empty space: None
        flat_list = list(range(1, self.size**2)) + [None]

        #Compile our flat list into a matrix 
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
