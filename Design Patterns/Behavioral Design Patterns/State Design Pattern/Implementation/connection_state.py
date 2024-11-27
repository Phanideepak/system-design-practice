

# interface Connection
class Connection():

    def open(self):
        pass


    def close(self):
        pass 

  
    def update(self):
        pass    


    def log(self):
        pass

# Concrete classes 
class Accounting(Connection):
    def open(self):
        print('Open database for accounting')
    
    def close(self):
        print('close the database')
    
    def log(self):
        print('log activities')
    
    def update(self):
        print('Accounting has been updated')


class Sales(Connection):
    def open(self):
        print('Open database for sales')
    
    def close(self):
        print('close the database')
    
    def log(self):
        print('log activities')
    
    def update(self):
        print('Sales has been updated')


class Management(Connection):
    def open(self):
        print('Open database for management')
    
    def close(self):
        print('close the database')
    
    def log(self):
        print('log activities')
    
    def update(self):
        print('Management has been updated')


class Controller:
    def __init__(self):
        self.accounting = Accounting()
        self.sales = Sales()
        self.management = Management()
        self.__con = Connection()

    def set_accounting_connection(self):
        self.__con = self.accounting
    
    def set_sales_conneciton(self):
        self.__con = self.sales
    
    def set_management_connection(self):
        self.__con = self.management
    
    def open(self):
        self.__con.open()
    
    def close(self):
        self.__con.close()
    
    def update(self):
        self.__con.update()
    
    def log(self):
        self.__con.log()
    


# Client Code
con = 'management'
controller = Controller()

if con == 'management':
    controller.set_management_connection()

if con == 'sales':
    controller.set_sales_conneciton()

if con == 'accounting':
    controller.set_accounting_connection()

controller.open()
controller.log()
controller.close()
controller.update()


