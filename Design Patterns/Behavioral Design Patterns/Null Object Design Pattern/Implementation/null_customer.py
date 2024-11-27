from abc import ABC, abstractmethod


# Abstract Customer
class Customer(ABC):
    def __init__(self):
        self._name = None
    
    @abstractmethod
    def get_name(self):
        pass 

    @abstractmethod
    def is_null(self):
        pass

    def __str__(self):
        return self.get_name()


class RealCustomer(Customer):
    def __init__(self, name):
        self._name = name 
    
    def get_name(self):
        return self._name
    
    def is_null(self):
        return False


class NullCustomer(Customer):
    def get_name(self):
        return 'Customer not found in the database'
    
    def is_null(self):
        return True

    
class CustomerFactory:
    def __init__(self):
        self.__names = ['Abhi', 'Dilip', 'Deepak']

    def get_customer(self, name):
        if name in self.__names:
            return RealCustomer(name)
        return NullCustomer()


# client code. 

factory = CustomerFactory()

customer1 = factory.get_customer('Abhi')
customer2 = factory.get_customer('Rama')
customer3 = factory.get_customer('Deepak')
customer4 = factory.get_customer('Lin')

print(customer1, customer2, customer3, customer4, sep='\n')

