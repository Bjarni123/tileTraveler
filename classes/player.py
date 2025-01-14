class Player():
    def __init__(self, location:list = [1, 1], level:int = 1, inventory: int = 0):
        self.location = location #[X Axis, Y Axis]
        self.level = level 
        self.inventory = inventory

    def get_location(self):
        return self.location
    
    def get_level(self):
        return self.level
    
    def get_inventory(self):
        return self.inventory
    
    def set_location(self, value):
        self.location = value
    
    def set_level(self, value):
        self.level = value
    
    def set_inventory(self, value):
        self.inventory = value
    
    def add_to_inventory(self, value):
        self.inventory += value

    def playe_move_north(self):
        '''Moves 2 squares up on the Y axis'''
        self.location[1] += 2

    def playe_move_east(self):
        '''Moves 2 squares up on the x axis'''
        self.location[0] += 2

    def playe_move_south(self):
        '''Moves 2 squares down on the Y axis'''
        self.location[1] -= 2

    def playe_move_west(self):
        '''Moves 2 squares down on the x axis'''
        self.location[0] -=2
