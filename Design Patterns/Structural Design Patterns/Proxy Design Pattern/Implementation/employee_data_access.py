from abc import ABC, abstractmethod

class Employee:
    def __init__(self, id, name, designation, salary):
        self.__id = id 
        self.__name = name
        self.__designation = designation
        self.__salary = salary

# Abstract class
class EmployeeDao(ABC):
    @abstractmethod
    def create(self, client, emp):
        pass

    @abstractmethod
    def get(self, client, emp_id):
        pass 

    @abstractmethod    
    def delete(self, client, emp_id):
        pass 


class EmployeeDaoImpl(EmployeeDao):
    def create(self, client, emp):
        print('Create a new row in employee table')
    
    def get(self, client, emp_id):
        print(f'Fetching employee by emp_id = {emp_id}')
        return Employee()
    
    def delete(self, client, emp_id):
        print(f'Deleted row with emp_id = {emp_id}')

class EmployeeDaoProxy:
    def __init__(self):
        self.__employeeDao = EmployeeDaoImpl()
    
    def create(self, client, emp):
        if client != 'ADMIN':
           raise Exception('Access Denied')
        
        self.__employeeDao.create(client, emp)
    
    def delete(self, client, emp_id):
        if client != 'ADMIN':
            raise Exception('Access Denied')
        
        self.__employeeDao.delete(client, emp_id)
    
    def get(self, client, empt_id):
        if client not in ['ADMIN','USER']:
            raise Exception('Access Denied')
        
        return self.__employeeDao.get(client, empt_id)


# Client Code
emp_dao = EmployeeDaoProxy()
emp_dao.create('ADMIN', Employee())
print('Operation Successful')