# Code With out using Prototype Pattern

```python
class Student: 
    def __init__(self, name = None, age = None, roll_no = None):
        self.name = name
        self.age = age
        self.__roll_no = roll_no
    
student = Student('Vikram', 22, 'S0001')

clone_student = Student()
clone_student.name = student.name
cloned_student.age = student.age

# It is impossible to access private attribute roll number
cloned_student.age = student.__roll_no

```

- In the above code, It is impossible to clone the private attributes of the orignal object.

## Code with Prototype Pattern

```python

class Prototype:
    def get_clone(self):
        pass

class Student(Prototype)
    def __init__(self, name = None, age = None, roll_no = None):
        self.name = name
        self.age = age
        self.__roll_no = roll_no
    
    def get_clone(self):
        return Student(self.name, self.age, self.__roll_no)

student = Student('Vikram', 22, 'S0001')
cloned_student = student.get_clone()

```

- It is possible to clone the private members of the class by using prototype pattern
