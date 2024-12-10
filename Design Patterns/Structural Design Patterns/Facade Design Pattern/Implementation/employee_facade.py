# Employee Details
class Employee:
    def __init__(self, id, name, salary, age):
        self.__id = id
        self.__name = name
        self.__salary = salary
        self.__age = age
    
    def set_name(self, name):
        self.__name = name
    
    def __str__(self):
        print(f'Employee: id = {self.__id}, name = {self.__name}, salary = {self.__salary} and age = {self.__age}')

# Data Access Object
class EmployeeDAO:
    def insert(self, name, salary, age):
        print(f'Inserting into employee : ({name}, {salary}, {age})')

    def get_by_id(self, emp_id):
        return Employee('emp', 100000, 20)   

    def get_all(self):
        pass 

    def update_employee_name(self, emp_id, name):
        emp = Employee(emp_id)
        emp.set_name(name)

    def delete_by_id(self, emp_id):
        pass



# Employee Facade
class EmployeeFacade:
    def __init__(self):
        self.__employee_dao = EmployeeDAO()
    
    def insert_employee_details(self, name, salary, age):
        self.__employee_dao.insert(name, salary, age)
    
    def get_details(self, id):
        return self.__employee_dao.get_by_id(id)


# Client
employee_facade = EmployeeFacade()
employee_facade.insert_employee_details('Test Employee', 100000, 24)