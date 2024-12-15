from item_shelf import ItemShelf
from item import Item

class Inventory:
    
    def __init__(self, item_count):
        self.inventory = [None for i in range(item_count)]
    
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
    
    def add_item(self, item : Item, code_number):
        for inventory_item_shelf in self.inventory:
            if inventory_item_shelf.get_code() == code_number:
                if inventory_item_shelf.is_sold_out():
                    inventory_item_shelf.set_item(item)
                    inventory_item_shelf.set_sold_out(True)
                else:
                    raise Exception('already item is present, you can not add item here')
    
    def get_item(self,code_number) -> Item:
        for inventory_item_shelf in self.inventory:
            if inventory_item_shelf.get_code() == code_number:
                if inventory_item_shelf.is_sold_out():
                    raise Exception('item already sold out') 
                else:
                    return inventory_item_shelf.get_item()
        
        raise Exception('Invalid code')


    def update_sold_out_item(self, code_number):
        for inventory_item_shelf in self.inventory:
            if inventory_item_shelf.get_code() == code_number:
               inventory_item_shelf.set_sold_out(True)