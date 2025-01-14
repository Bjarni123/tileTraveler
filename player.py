class Player():
    def __init__(self, location, level, inventory):
        self.location = location
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





