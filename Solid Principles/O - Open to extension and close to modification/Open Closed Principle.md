### **Open/Closed Principle (OCP)**

**Definition**:  
A class, module, or function should be **open for extension** but **closed for modification**.  

This principle emphasizes designing systems that allow new functionality to be added without altering existing code.

---

### **Key Points**:
1. **Open for Extension**:
   - The behavior of a module can be extended to accommodate new functionality.
   
2. **Closed for Modification**:
   - Existing, stable code should not be altered to introduce new behavior.

3. **Achieved Through Abstraction**:
   - Leverage interfaces, abstract classes, or polymorphism to make code extensible.

---

### **Benefits**:
- **Reduces Risk**: Minimizes introducing bugs when adding new features.
- **Encourages Scalability**: The system can grow without restructuring existing components.
- **Improves Maintainability**: Existing code remains untouched, making debugging easier.

---

### **Examples**

#### **Violating OCP**
Imagine a `Drawing` class that handles rendering different shapes. Adding a new shape requires modifying the `render` method.

```python
class Circle:
    def draw(self):
        print("Drawing Circle")

class Square:
    def draw(self):
        print("Drawing Square")

class Drawing:
    def render(self, shapes):
        for shape in shapes:
            if isinstance(shape, Circle):
                shape.draw()
            elif isinstance(shape, Square):
                shape.draw()
```

- **Problems**:
  - Adding a new shape, like `Triangle`, requires modifying the `render` method.
  - Violates OCP as the class is not closed for modification.

---

#### **Following OCP**
Using polymorphism allows new shapes to be added without altering the `Drawing` class.

```python
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Square(Shape):
    def draw(self):
        print("Drawing Square")

class Drawing:
    def render(self, shapes):
        for shape in shapes:
            shape.draw()
```

- **Advantages**:
  - Adding a new shape, like `Triangle`, only involves creating a new class:
    ```python
    class Triangle(Shape):
        def draw(self):
            print("Drawing Triangle")
    ```
  - The `Drawing` class remains unchanged.

---

### **Real-World Scenarios**

#### **1. Payment Processing**
- **Violating OCP**:
  ```python
  class PaymentProcessor:
      def process_payment(self, payment_type):
          if payment_type == "credit_card":
              self.process_credit_card()
          elif payment_type == "paypal":
              self.process_paypal()
  ```

- **Following OCP**:
  ```python
  class Payment:
      def process(self):
          pass

  class CreditCardPayment(Payment):
      def process(self):
          print("Processing credit card payment")

  class PayPalPayment(Payment):
      def process(self):
          print("Processing PayPal payment")

  class PaymentProcessor:
      def process_payment(self, payment):
          payment.process()
  ```

  - Adding a new payment type only requires creating a new `Payment` subclass.

---

#### **2. Logging System**
- **Violating OCP**:
  ```python
  class Logger:
      def log(self, message, log_type):
          if log_type == "file":
              self.log_to_file(message)
          elif log_type == "console":
              self.log_to_console(message)
  ```

- **Following OCP**:
  ```python
  class Logger:
      def log(self, message):
          pass

  class FileLogger(Logger):
      def log(self, message):
          print(f"Logging to file: {message}")

  class ConsoleLogger(Logger):
      def log(self, message):
          print(f"Logging to console: {message}")

  class App:
      def __init__(self, logger: Logger):
          self.logger = logger

      def run(self):
          self.logger.log("Application started")
  ```

---

### **Common Techniques to Apply OCP**

1. **Polymorphism**:
   - Use abstract classes or interfaces to define a common behavior and allow extensions.
   
2. **Composition over Inheritance**:
   - Prefer designing systems where behavior can be extended through composition rather than modifying inherited classes.

3. **Design Patterns**:
   - Use patterns like **Strategy**, **Decorator**, or **Factory** to achieve OCP.

---

### **Identifying Violations**
- **Frequent Modifications**: If you need to modify existing classes to support new features, it’s a sign OCP is violated.
- **Hard-Coded Conditions**: A class with multiple `if`/`else` or `switch` statements often violates OCP.

---

### **Summary**
| Aspect               | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| **Focus**            | Extensibility without modifying existing code.                             |
| **Key Mechanism**    | Use abstraction and polymorphism.                                           |
| **Benefits**         | Enhances scalability, reduces bugs, and improves maintainability.           |

---