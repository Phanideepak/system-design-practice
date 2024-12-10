#Component Interface that acts as blueprint for parent and child
class Employee:
    def get_id(self):
        pass 

    def get_name(self):
        pass

    def get_salary(self):
        pass

    def print(self):
        pass 

    def add(self, emp):
        pass

    def remove(self, emp):
        pass

    def getChild(self, index):
        pass

# Parent Class
class BankManager(Employee):
    def __init__(self, id, name, salary):
        self.__id = id 
        self.__name = name
        self.__salary = salary
        self.__emps = []
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_salary(self):
        return self.__salary

    def print(self):
        for emp in self.__emps:
            print(emp)
    
    def add(self, emp):
        self.__emps.append(emp)
    
    def remove(self, emp):
        self.__emps.remove(emp)
    
    def getChild(self, index):
        return self.__emps[index]


# Child Class
class Cashier(Employee):
    def __init__(self, id, name, salary):
        self.__id = id 
        self.__name = name
        self.__salary = salary
    
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def get_salary(self):
        return self.__salary
    
    def add(self, emp):
        raise NotImplementedError('Operation not supported for child')
    
    def remove(self, emp):
        raise NotImplementedError('Operation not supported for child')
    
    def getChild(self, index):
        return None
    
    def __str__(self) :
        return f'Cashier id = {self.__id}, name = {self.__name}, salary = {self.__salary}'


emp1 = Cashier(1, 'Aravind reddy', 100000)
emp2 = Cashier(2, 'Pandi Anil', 600000)

manager = BankManager(3, 'Anil', 1000000)

manager.add(emp1)
manager.add(emp2)

manager.print()