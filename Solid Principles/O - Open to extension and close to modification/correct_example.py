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

class InvoiceDao:
    invoice : Invoice

    def __init__(self, invoice):
        self.invoice = invoice
        pass

    def save(self):
        pass

class DatabaseInvoiceDao(InvoiceDao):

    def __init__(self, invoice):
        super().__init__(invoice) 

    def save(self):
        # Perform Database Operations
        pass
    
class FileInvoiceDao(InvoiceDao): 

    def __init__(self, invoice):
        super().__init__(invoice) 

    def save(self):
        # Perform File Operations
        pass
