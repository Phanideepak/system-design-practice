class Marker:
    name : str
    color : str
    year : int 
    price : int

    def __init__(self, name, color, year, price):
        self.name = name
        self.color = color
        self.year = year
        self.price = price

class Invoice:
    __marker : Marker
    __quantity : int

    def __init__(self, marker, quantity):
        self.__marker = marker
        self.__quantity = quantity

    def calculate_total(self):
        return self.__marker.price * self.__quantity

    def print_invoice(self):
        # Printing the Invoice
        pass

    def saveToDatabase(self):
        # Save Invoice to Database
        pass