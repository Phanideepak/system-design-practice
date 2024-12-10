### **Creational Design Patterns**

Creational design patterns deal with the process of object creation, ensuring that objects are created in a manner suitable for the situation. These patterns provide flexibility in how objects are instantiated and emphasize reuse and encapsulation.

---

### **1. Singleton**
**Intent**: Ensure a class has only one instance and provide a global access point to it.

**Key Features**:
- Single instance of the class.
- Controlled access through a global point.
- Useful for configurations, logging, or thread pools.

**Example**:

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

---

### **2. Factory Method**
**Intent**: Define an interface for creating an object but let subclasses decide which class to instantiate.

**Key Features**:
- Promotes loose coupling.
- The exact class of the object is determined during runtime.

**Example**:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Square(Shape):
    def draw(self):
        print("Drawing Square")

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError("Unknown shape type")

# Usage
factory = ShapeFactory()
shape = factory.create_shape("circle")
shape.draw()  # Drawing Circle
```

---

### **3. Abstract Factory**
**Intent**: Provide an interface to create families of related or dependent objects without specifying their concrete classes.

**Key Features**:
- Useful for systems requiring multiple related objects.
- Ensures consistency among related objects.

**Example**:

```python
from abc import ABC, abstractmethod

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        print("Rendering Windows Button")

class MacButton(Button):
    def render(self):
        print("Rendering Mac Button")

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

class WindowsCheckbox(Checkbox):
    def render(self):
        print("Rendering Windows Checkbox")

class MacCheckbox(Checkbox):
    def render(self):
        print("Rendering Mac Checkbox")

# Usage
factory = WindowsFactory()
button = factory.create_button()
button.render()  # Rendering Windows Button
```

---

### **4. Builder**
**Intent**: Separate the construction of a complex object from its representation, allowing the same construction process to create different representations.

**Key Features**:
- Focuses on step-by-step construction.
- Useful for constructing immutable or complex objects.

**Example**:

```python
class Burger:
    def __init__(self, bun, patty, sauce):
        self.bun = bun
        self.patty = patty
        self.sauce = sauce

    def __str__(self):
        return f"Bun: {self.bun}, Patty: {self.patty}, Sauce: {self.sauce}"

class BurgerBuilder:
    def __init__(self):
        self.bun = None
        self.patty = None
        self.sauce = None

    def set_bun(self, bun):
        self.bun = bun
        return self

    def set_patty(self, patty):
        self.patty = patty
        return self

    def set_sauce(self, sauce):
        self.sauce = sauce
        return self

    def build(self):
        return Burger(self.bun, self.patty, self.sauce)

# Usage
builder = BurgerBuilder()
burger = builder.set_bun("Sesame").set_patty("Beef").set_sauce("Barbecue").build()
print(burger)  # Bun: Sesame, Patty: Beef, Sauce: Barbecue
```

---

### **5. Prototype**
**Intent**: Create new objects by copying existing objects, providing an alternative to subclassing for object creation.

**Key Features**:
- Reduces the cost of creating complex objects.
- Useful when object creation is resource-intensive.

**Example**:

```python
import copy

class Prototype:
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)

# Usage
original = Prototype([1, 2, 3])
clone = original.clone()
clone.value.append(4)

print(original.value)  # [1, 2, 3]
print(clone.value)     # [1, 2, 3, 4]
```

---

### **6. Object Pool**
**Intent**: Manage reusable objects to reduce the cost of object creation and destruction.

**Key Features**:
- Useful for managing expensive-to-create objects.
- Optimizes performance by reusing objects.

**Example**:

```python
class ObjectPool:
    def __init__(self, create_object, max_size=5):
        self.pool = []
        self.create_object = create_object
        self.max_size = max_size

    def get(self):
        if self.pool:
            return self.pool.pop()
        return self.create_object()

    def release(self, obj):
        if len(self.pool) < self.max_size:
            self.pool.append(obj)

# Usage
pool = ObjectPool(lambda: {"connection": "new_connection"})
conn1 = pool.get()
conn2 = pool.get()
pool.release(conn1)
reused_conn = pool.get()
print(conn1 is reused_conn)  # True
```

---

### **Summary of Creational Patterns**

| **Pattern**       | **Intent**                                                                 |
|--------------------|---------------------------------------------------------------------------|
| **Singleton**      | Ensure only one instance of a class exists globally.                     |
| **Factory Method** | Delegate object creation to subclasses or methods.                       |
| **Abstract Factory** | Create families of related objects without specifying concrete classes.  |
| **Builder**        | Build complex objects step-by-step.                                      |
| **Prototype**      | Clone existing objects for object creation.                              |
| **Object Pool**    | Reuse objects to optimize performance and resource usage.                |

---