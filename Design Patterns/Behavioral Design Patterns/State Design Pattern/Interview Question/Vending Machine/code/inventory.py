class Inventory:
    inventory = None

    def __init__(self, item_count):
        inventory = [ItemShelf() for i in range(item_count)]
    
    def get_inventory(self):
        return self.inventory
    
    def set_inventory(self, inventory):
        self.inventory = inventory
    
    def initial_empty_inventory(self):
        start_code = 101
        for i in range(len(self.inventory)):
            space = ItemShelf()
            space.set_code(start_code)
            space.set_sold_out(True)
            self.inventory[i] = space
            start_code += 1
    
    def add