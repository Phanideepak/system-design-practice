### **Structural Design Patterns**

Structural design patterns focus on how classes and objects are composed to form larger structures while ensuring flexibility and efficiency. These patterns help simplify relationships between entities and manage how objects interact with one another.

---

### **Key Structural Patterns**

1. **Adapter Pattern**  
   Converts the interface of a class into another interface that clients expect. It acts as a bridge between two incompatible interfaces.

2. **Bridge Pattern**  
   Decouples an abstraction from its implementation so that the two can vary independently.

3. **Composite Pattern**  
   Composes objects into tree structures to represent part-whole hierarchies. It allows clients to treat individual objects and compositions of objects uniformly.

4. **Decorator Pattern**  
   Adds additional responsibilities to an object dynamically, without altering its structure.

5. **Facade Pattern**  
   Provides a simplified interface to a larger body of code, making a subsystem easier to use.

6. **Flyweight Pattern**  
   Reduces the memory footprint by sharing common parts of objects across multiple instances.

7. **Proxy Pattern**  
   Provides a surrogate or placeholder to control access to an object.

---

### **Quick Overview of Patterns**

| **Pattern**          | **Purpose**                                                                                 | **When to Use**                                                                                 |
|-----------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| **Adapter**          | Convert one interface into another.                                                        | When integrating incompatible interfaces or legacy code.                                       |
| **Bridge**           | Separate abstraction from implementation.                                                  | When you need to extend both abstraction and implementation independently.                     |
| **Composite**        | Treat individual objects and groups of objects uniformly.                                   | When building hierarchies (e.g., file systems, graphical elements).                           |
| **Decorator**        | Dynamically add functionality to an object.                                                | When extending functionality without subclassing.                                              |
| **Facade**           | Simplify interactions with a complex subsystem.                                             | When you want to hide complexity and provide a simple interface.                              |
| **Flyweight**        | Share objects to save memory for large numbers of similar objects.                          | When managing a large number of similar objects efficiently.                                   |
| **Proxy**            | Provide controlled access or additional functionality to another object.                    | When adding security, lazy initialization, or monitoring to objects.                          |

---

### **Detailed Descriptions and Examples**

#### **1. Adapter Pattern**
```python
# Existing interface
class OldSystem:
    def specific_request(self):
        return "Old System Request"

# Desired interface
class NewSystem:
    def request(self):
        pass

# Adapter to bridge old and new systems
class Adapter(NewSystem):
    def __init__(self, old_system):
        self.old_system = old_system

    def request(self):
        return self.old_system.specific_request()

# Usage
old_system = OldSystem()
adapter = Adapter(old_system)
print(adapter.request())  # Output: Old System Request
```

---

#### **2. Bridge Pattern**
```python
# Abstraction
class RemoteControl:
    def __init__(self, device):
        self.device = device

    def turn_on(self):
        return self.device.on()

    def turn_off(self):
        return self.device.off()

# Implementations
class TV:
    def on(self):
        return "TV is ON"

    def off(self):
        return "TV is OFF"

class Radio:
    def on(self):
        return "Radio is ON"

    def off(self):
        return "Radio is OFF"

# Usage
tv = TV()
radio = Radio()
remote = RemoteControl(tv)
print(remote.turn_on())  # Output: TV is ON
remote.device = radio
print(remote.turn_on())  # Output: Radio is ON
```

---

#### **3. Composite Pattern**
```python
# Component
class Graphic:
    def render(self):
        pass

# Leaf
class Line(Graphic):
    def render(self):
        return "Rendering a line"

class Circle(Graphic):
    def render(self):
        return "Rendering a circle"

# Composite
class Picture(Graphic):
    def __init__(self):
        self.graphics = []

    def add(self, graphic):
        self.graphics.append(graphic)

    def render(self):
        return [graphic.render() for graphic in self.graphics]

# Usage
line = Line()
circle = Circle()
picture = Picture()
picture.add(line)
picture.add(circle)
print(picture.render())  # Output: ['Rendering a line', 'Rendering a circle']
```

---

#### **4. Decorator Pattern**
```python
class Component:
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"

class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        return self.component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"{super().operation()} + DecoratorA"

# Usage
component = ConcreteComponent()
decorated = ConcreteDecoratorA(component)
print(decorated.operation())  # Output: ConcreteComponent + DecoratorA
```

---

#### **5. Facade Pattern**
```python
class SubsystemA:
    def operation(self):
        return "SubsystemA operation"

class SubsystemB:
    def operation(self):
        return "SubsystemB operation"

class Facade:
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()

    def perform_task(self):
        return f"{self.subsystem_a.operation()} + {self.subsystem_b.operation()}"

# Usage
facade = Facade()
print(facade.perform_task())  # Output: SubsystemA operation + SubsystemB operation
```

---

#### **6. Flyweight Pattern**
```python
class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state

    def operation(self, unique_state):
        return f"Shared({self.shared_state}) + Unique({unique_state})"

class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, shared_state):
        if shared_state not in self.flyweights:
            self.flyweights[shared_state] = Flyweight(shared_state)
        return self.flyweights[shared_state]

# Usage
factory = FlyweightFactory()
flyweight1 = factory.get_flyweight("State1")
print(flyweight1.operation("Unique1"))  # Output: Shared(State1) + Unique(Unique1)
```

---

#### **7. Proxy Pattern**
```python
class RealSubject:
    def request(self):
        return "RealSubject: Handling request"

class Proxy:
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def request(self):
        return f"Proxy: Logging and delegating -> {self.real_subject.request()}"

# Usage
real_subject = RealSubject()
proxy = Proxy(real_subject)
print(proxy.request())  # Output: Proxy: Logging and delegating -> RealSubject: Handling request
```

---

### **Summary Table**

| **Pattern**          | **Key Benefit**                                                                 |
|-----------------------|---------------------------------------------------------------------------------|
| **Adapter**          | Works as a bridge between incompatible interfaces.                              |
| **Bridge**           | Decouples abstraction and implementation for independent variation.             |
| **Composite**        | Handles part-whole hierarchies with uniform treatment for individual objects.   |
| **Decorator**        | Adds new responsibilities dynamically without altering original object.         |
| **Facade**           | Simplifies interaction with a complex subsystem.                                |
| **Flyweight**        | Minimizes memory usage by sharing similar objects.                              |
| **Proxy**            | Provides controlled or enhanced access to an object.                           |