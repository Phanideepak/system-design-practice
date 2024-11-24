### **Liskov Substitution Principle (LSP)**

**Definition**:  
Subtypes must be substitutable for their base types without altering the correctness of the program.  

In simpler terms, objects of a derived class should be able to replace objects of the base class without the program behaving incorrectly.

---

### **Key Points**:
1. **Behavioral Consistency**:
   - Subclasses should not override or change the expected behavior of the base class.
   
2. **Contract Compliance**:
   - Subtypes must honor the contract established by their base types (inputs, outputs, invariants).

3. **Avoid Invalid Assumptions**:
   - Derived classes should not weaken preconditions or strengthen postconditions.

---

### **Benefits**:
- **Code Reusability**: Promotes reliable use of polymorphism.
- **Robustness**: Ensures that derived classes do not introduce unexpected behavior.
- **Maintainability**: Facilitates replacing or extending functionality without breaking existing code.

---

### **Examples**

#### **Violating LSP**
A `Bird` base class assumes all birds can fly. However, an `Ostrich` subclass cannot.

```python
class Bird:
    def fly(self):
        print("Flying")

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostriches can't fly")
```

- **Problems**:
  - The `Ostrich` class violates LSP because it cannot be used wherever the `Bird` class is expected.
  - For example:
    ```python
    def make_bird_fly(bird: Bird):
        bird.fly()

    ostrich = Ostrich()
    make_bird_fly(ostrich)  # Fails with NotImplementedError
    ```

---

#### **Following LSP**
Refactor to separate the concept of flying birds and non-flying birds.

```python
class Bird:
    def make_sound(self):
        pass

class FlyingBird(Bird):
    def fly(self):
        print("Flying")

class Ostrich(Bird):
    def run(self):
        print("Running")
```

- **Advantages**:
  - Now `Ostrich` doesn’t pretend to fly and behaves correctly in its context.
  - LSP is preserved as:
    ```python
    def interact_with_bird(bird: Bird):
        bird.make_sound()

    ostrich = Ostrich()
    interact_with_bird(ostrich)  # Works without issues
    ```

---

### **Real-World Scenarios**

#### **1. Shapes Example**
- **Violating LSP**:
  ```python
  class Rectangle:
      def __init__(self, width, height):
          self.width = width
          self.height = height

      def area(self):
          return self.width * self.height

  class Square(Rectangle):
      def __init__(self, side):
          super().__init__(side, side)

      def set_width(self, width):
          self.width = width
          self.height = width  # Breaks LSP

      def set_height(self, height):
          self.height = height
          self.width = height  # Breaks LSP
  ```

  - **Problem**: A `Square` is not substitutable for `Rectangle`. Modifying one dimension changes both, which breaks expectations of the base class.

- **Following LSP**:
  ```python
  class Shape:
      def area(self):
          pass

  class Rectangle(Shape):
      def __init__(self, width, height):
          self.width = width
          self.height = height

      def area(self):
          return self.width * self.height

  class Square(Shape):
      def __init__(self, side):
          self.side = side

      def area(self):
          return self.side * self.side
  ```

---

#### **2. Payment System**
- **Violating LSP**:
  A base `Payment` class assumes all payment methods require a `card_number`, but `PayPalPayment` doesn’t.

  ```python
  class Payment:
      def process(self, card_number):
          pass

  class CreditCardPayment(Payment):
      def process(self, card_number):
          print(f"Processing credit card payment: {card_number}")

  class PayPalPayment(Payment):
      def process(self, card_number):
          raise NotImplementedError("PayPal does not use a card number")
  ```

  - **Problem**: `PayPalPayment` violates LSP as it doesn’t align with the base class's expectations.

- **Following LSP**:
  Refactor to use a more generic interface.

  ```python
  class Payment:
      def process(self):
          pass

  class CreditCardPayment(Payment):
      def __init__(self, card_number):
          self.card_number = card_number

      def process(self):
          print(f"Processing credit card payment: {self.card_number}")

  class PayPalPayment(Payment):
      def __init__(self, email):
          self.email = email

      def process(self):
          print(f"Processing PayPal payment for {self.email}")
  ```

---

### **Best Practices for LSP**

1. **Use Inheritance Correctly**:
   - Subclasses should only add functionality, not override core behavior.
   
2. **Favor Composition Over Inheritance**:
   - Use composition when the subclass does not fully comply with the base class’s behavior.

3. **Preconditions and Postconditions**:
   - Subclasses should not weaken preconditions or strengthen postconditions.

4. **Use Interfaces/Abstract Classes**:
   - Define clear contracts for base types to ensure consistent behavior.

---

### **Identifying Violations**
- **Unexpected Exceptions**: A derived class throws exceptions where the base class doesn't.
- **Behavioral Changes**: A derived class alters the logic of the base class in unintended ways.
- **Overridden Methods**: Look for methods in derived classes that don’t honor the expectations of the base class.

---

### **Summary**
| Aspect               | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| **Focus**            | Substitutability without altering program behavior.                        |
| **Key Mechanism**    | Polymorphism and clear contracts.                                           |
| **Benefits**         | Ensures reliability, robustness, and maintainability of systems.           |
