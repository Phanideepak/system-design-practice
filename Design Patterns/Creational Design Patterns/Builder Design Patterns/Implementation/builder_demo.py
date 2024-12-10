class Department:
    def __init__(self, id, name):
        self.id = id 
        self.name = name


class DepartmentBuilder:
    def __init__(self):
        self.id = None
        self.name = None 

    def set_id(self, id):
        self.id = id
        return self

    def set_name(self, name):
        self.name = name
        return self

    def build(self):
        return Department(self.id, self.name)


class Employee:
    def __init__(self, id, firstname, lastname, age, gender, dept, salary):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.dept = dept
        self.salary = salary

    def __str__(self):
        return f'{self.firstname} - {self.lastname} aged {self.age} gender {self.gender} works in  {self.dept.name} department'


class EmployeeBuilder:
    def __init__(self):
        self.id = None 
        self.firstname = None 
        self.lastname = None 
        self.age = None 
        self.gender = None 
        self.dept = None 
        self.salary = None
    
    def set_id(self, id):
        self.id = id 
        return self

    def set_firstname(self, firstname):
        self.firstname = firstname
        return self
    
    def set_lastname(self, lastname):
        self.lastname = lastname
        return self
    
    def set_age(self, age):
        self.age = age
        return self
    
    def set_gender(self, gender):
        self.gender = gender
        return self
    
    def set_dept(self, dept):
        self.dept = dept
        return self
    
    def set_salary(self, salary):
        self.salary = salary
        return self
    
    def build(self):
        return Employee(self.id, self.firstname, self.lastname, self.age, self.gender, self.dept, self.salary)

employeeBuilder = EmployeeBuilder()
departmentBuilder = DepartmentBuilder()


emp = ( 
        employeeBuilder.set_id(1)
                    .set_firstname('Vikram')
                    .set_lastname('Rathore')
                    .set_age(29)
                    .set_gender('Male')
                    .set_salary(100000)
                    .set_dept(departmentBuilder.set_id(1)
                          .set_name('IT')
                          .build())
                    .build() 
       )

print(emp)
