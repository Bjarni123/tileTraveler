class Map:
    def __init__(self, current_level_file: str = 'saves_and_levels/level1.txt'):
        self.map = list()
        self.change_level(current_level_file)

    def get_map(self):
        """Returns the map as a list"""
        return self.map
    
    def get_available_actions(self, position: list[int, int]) -> list[bool, bool, bool, bool, int]:
        """
        Takes in position and returns which directions are not blocked by a wall.
        Returns: [North: bool, East: bool, South: bool, West: bool, lever: int]
        """
        # Name       X position             Y position         wall
        north = self.map[position[0] + 1][position[1]]      != 'w'
        east = self.map[position[0]]     [position[1] + 1]  != 'w'
        south = self.map[position[0] - 1][position[1]]      != 'w'
        west = self.map[position[0]]     [position[1] - 1]  != 'w'

        # value of the current tile
        lever = self.map[position[0]][position[1]]
        return [north, east, south, west, lever]

# -------------- Possibly have this in main ------------------------

    def change_level(self, current_level_file):
        """Changes level, and updates map"""
        self.map = list()
        for column in self.open_file(current_level_file=current_level_file):
            cleaned_column = list()
            for tile in column:
                try:
                    cleaned_column.append(int(tile))
                except:
                    cleaned_column.append(tile)
            self.map.append(cleaned_column)
        

    def open_file(self, current_level_file: str) -> list[list]:
        """Tries to open file given and returns it"""

        with open(current_level_file, 'r') as file:
            return file
        
# ------------------------------------------------------------------