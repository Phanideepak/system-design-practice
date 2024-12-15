from item import Item

class ItemShelf:
    def __init__(self):
        self.__code = None
        self.__item : Item = None
        self.__sold_out = None
    
    def get_code(self):
        return self.__code
    
    def set_code(self, code):
        self.__code = code
    
    def get_item(self):
        return self.__item
    
    def set_item(self, item):
        self.__item = item
    
    def is_sold_out(self):
        return self.__sold_out
    
    def set_sold_out(self, sold_out):
        self.__sold_out = sold_out