from item_type import ItemType 


class Item:
    def __init__(self):
        self.__type : ItemType = None 
        self.__price = 0 
    
    def get_type(self):
        return self.__type
    
    def set_type(self, type):
        self.__type = type
    
    def set_price(self, price):
        self.__price = price
    
    def get_price(self):
        return self.__price