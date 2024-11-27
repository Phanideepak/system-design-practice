The **Template Method Design Pattern** is a behavioral design pattern that defines the skeleton of an algorithm in a base class and allows subclasses to override specific steps of the algorithm without changing its overall structure. It ensures a consistent algorithm structure while promoting code reuse and flexibility.

---

### Key Concepts
1. **Algorithm Skeleton**: The base class defines the fixed structure of the algorithm.
2. **Step Customization**: Subclasses override or implement specific steps of the algorithm to provide custom behavior.
3. **Control Inversion**: The base class controls the overall algorithm, while subclasses supply specific behavior.

---

### Participants
1. **Abstract Class**:
   - Defines the template method that outlines the algorithm.
   - Implements the invariant steps of the algorithm.
   - Defines abstract or hook methods for steps that can be customized by subclasses.

2. **Concrete Classes**:
   - Implement or override the steps of the algorithm defined in the abstract class.

---

### Example: Beverage Preparation

Let's create a template for preparing beverages like tea and coffee, where the general steps are similar but differ in specific details.

#### Code Example (Python)

```python
from abc import ABC, abstractmethod

# Abstract Class
class Beverage(ABC):
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water...")

    def pour_in_cup(self):
        print("Pouring into cup...")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

# Concrete Class: Tea
class Tea(Beverage):
    def brew(self):
        print("Steeping the tea...")

    def add_condiments(self):
        print("Adding lemon...")

# Concrete Class: Coffee
class Coffee(Beverage):
    def brew(self):
        print("Dripping coffee through filter...")

    def add_condiments(self):
        print("Adding sugar and milk...")

# Client Code
if __name__ == "__main__":
    print("Preparing Tea:")
    tea = Tea()
    tea.prepare()

    print("\nPreparing Coffee:")
    coffee = Coffee()
    coffee.prepare()
```

---

### Output
```
Preparing Tea:
Boiling water...
Steeping the tea...
Pouring into cup...
Adding lemon...

Preparing Coffee:
Boiling water...
Dripping coffee through filter...
Pouring into cup...
Adding sugar and milk...
```

---

### Key Elements
1. **Template Method**:
   - In this example, the `prepare` method is the template method that defines the algorithm steps.
   - It calls the fixed steps (`boil_water`, `pour_in_cup`) and customizable steps (`brew`, `add_condiments`).

2. **Hook Methods**:
   - Optional steps can be implemented as "hooks," which subclasses may override if needed.

---

### Advantages
- **Code Reusability**: Common parts of the algorithm are implemented once in the base class.
- **Flexibility**: Subclasses can vary specific behavior without altering the algorithm's structure.
- **Consistency**: Ensures a consistent algorithm across all subclasses.

### Disadvantages
- **Subclass Explosion**: Adding too many variations may lead to a large number of subclasses.
- **Inflexibility in Structure**: Changes to the template method require changes to the base class, potentially affecting all subclasses.

---

### When to Use
- When multiple classes share the same structure for an algorithm but implement specific steps differently.
- To enforce a consistent algorithm structure while allowing customization in specific steps.
- For frameworks or libraries where the high-level algorithm is fixed, but details may vary.