### **Filter (Criteria) Design Pattern**

The **Filter Design Pattern**, also known as the **Criteria Pattern**, is a structural pattern that allows you to filter a set of objects based on different criteria and combine multiple criteria in a flexible way. This pattern is useful for separating the filtering logic from the object structures, making the code more modular and reusable.

---

### **Key Concepts**

1. **Criteria**:
   - Represents a single filtering condition. It defines an interface to filter a collection of objects.

2. **Concrete Criteria**:
   - Implements the `Criteria` interface to provide specific filtering logic.

3. **Composite Criteria**:
   - Combines multiple criteria using logical operations such as AND, OR, or NOT.

4. **Client**:
   - Uses the criteria to filter objects without being aware of the internal filtering logic.

---

### **Use Case**

Use the Filter Design Pattern when:
- You need to apply multiple filters dynamically.
- The filtering logic is complex and needs to be reused in different contexts.
- You want to separate filtering logic from the main business logic.

---

### **Class Diagram**

```
Criteria (Interface)
    + filter(objects: List<Object>) -> List<Object>

ConcreteCriteria
    + filter(objects: List<Object>) -> List<Object>

CompositeCriteria (AND, OR, NOT)
    + filter(objects: List<Object>) -> List<Object>
```

---

### **Python Implementation**

#### **Example: Filtering a List of Persons**

```python
from typing import List

# Person class
class Person:
    def __init__(self, name: str, gender: str, marital_status: str):
        self.name = name
        self.gender = gender
        self.marital_status = marital_status

    def __repr__(self):
        return f"Person(name={self.name}, gender={self.gender}, marital_status={self.marital_status})"


# Criteria Interface
class Criteria:
    def filter(self, persons: List[Person]) -> List[Person]:
        pass


# Concrete Criteria: Male
class CriteriaMale(Criteria):
    def filter(self, persons: List[Person]) -> List[Person]:
        return [person for person in persons if person.gender.lower() == "male"]


# Concrete Criteria: Female
class CriteriaFemale(Criteria):
    def filter(self, persons: List[Person]) -> List[Person]:
        return [person for person in persons if person.gender.lower() == "female"]


# Concrete Criteria: Single
class CriteriaSingle(Criteria):
    def filter(self, persons: List[Person]) -> List[Person]:
        return [person for person in persons if person.marital_status.lower() == "single"]


# Composite Criteria: AND
class AndCriteria(Criteria):
    def __init__(self, criteria: Criteria, other_criteria: Criteria):
        self.criteria = criteria
        self.other_criteria = other_criteria

    def filter(self, persons: List[Person]) -> List[Person]:
        first_filter = self.criteria.filter(persons)
        return self.other_criteria.filter(first_filter)


# Composite Criteria: OR
class OrCriteria(Criteria):
    def __init__(self, criteria: Criteria, other_criteria: Criteria):
        self.criteria = criteria
        self.other_criteria = other_criteria

    def filter(self, persons: List[Person]) -> List[Person]:
        first_filter = self.criteria.filter(persons)
        second_filter = self.other_criteria.filter(persons)
        return list(set(first_filter + second_filter))  # Combine and remove duplicates


# Client Code
if __name__ == "__main__":
    # List of persons
    persons = [
        Person("Alice", "Female", "Single"),
        Person("Bob", "Male", "Married"),
        Person("Charlie", "Male", "Single"),
        Person("Diana", "Female", "Married"),
        Person("Eve", "Female", "Single"),
    ]

    # Define criteria
    male = CriteriaMale()
    female = CriteriaFemale()
    single = CriteriaSingle()
    single_and_male = AndCriteria(single, male)
    single_or_female = OrCriteria(single, female)

    # Apply filters
    print("Males:", male.filter(persons))
    print("Females:", female.filter(persons))
    print("Single Males:", single_and_male.filter(persons))
    print("Single or Females:", single_or_female.filter(persons))
```

#### **Output**:
```
Males: [Person(name=Bob, gender=Male, marital_status=Married), Person(name=Charlie, gender=Male, marital_status=Single)]
Females: [Person(name=Alice, gender=Female, marital_status=Single), Person(name=Diana, gender=Female, marital_status=Married), Person(name=Eve, gender=Female, marital_status=Single)]
Single Males: [Person(name=Charlie, gender=Male, marital_status=Single)]
Single or Females: [Person(name=Alice, gender=Female, marital_status=Single), Person(name=Charlie, gender=Male, marital_status=Single), Person(name=Eve, gender=Female, marital_status=Single), Person(name=Diana, gender=Female, marital_status=Married)]
```

---

### **Advantages**

1. **Reusable Filters**:
   - Criteria can be reused across different parts of the application.

2. **Flexibility**:
   - Combine multiple criteria dynamically using logical operations like AND, OR, and NOT.

3. **Separation of Concerns**:
   - Filtering logic is decoupled from the main application logic.

4. **Scalability**:
   - Easy to add new criteria without modifying existing code.

---

### **Disadvantages**

1. **Complexity**:
   - Managing multiple criteria can lead to a more complex implementation.

2. **Performance**:
   - Applying multiple criteria to large datasets may affect performance.

---

### **Real-World Examples**

1. **E-commerce Platforms**:
   - Filtering products based on price, category, brand, or ratings.

2. **Job Portals**:
   - Filtering job listings by location, experience, and salary.

3. **UI Filtering**:
   - Dynamic search filters for user interfaces like dashboards or admin panels.

---