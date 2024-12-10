class Prototype:
    def get_clone(self):
        pass 

class Student(Prototype):
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.__roll_no = roll_no
    
    def get_clone(self):
        return Student(self.name, self.age, self.__roll_no)
    
    def __str__(self):
        return f'id: {id(self)}, Name: {self.name}, Age: {self.age}, Roll No: {self.__roll_no}'

student = Student('Anil', 50, 'S0001')

cloned_student  = student.get_clone()

print(student)
print(cloned_student)

        