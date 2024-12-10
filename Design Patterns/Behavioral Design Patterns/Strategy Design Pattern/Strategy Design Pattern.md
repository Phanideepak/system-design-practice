The **Strategy Design Pattern** is a behavioral design pattern that allows you to define a family of algorithms, encapsulate each one in a separate class, and make them interchangeable. It enables selecting an algorithm's behavior at runtime without modifying the clients that use it.

This pattern is particularly useful when you have multiple ways to perform an operation, and you want to decouple the algorithm's implementation from the code that uses it.

---

### Key Components
1. **Context**: Maintains a reference to a Strategy object and interacts with it. The Context delegates work to the currently selected Strategy object.
2. **Strategy Interface**: Defines a common interface for all supported algorithms.
3. **Concrete Strategies**: Implement the Strategy interface, each representing a specific algorithm or behavior.

---

### Benefits
1. **Open/Closed Principle**: New strategies can be added without modifying existing code.
2. **Single Responsibility Principle**: Separates algorithm implementations from the context code.
3. **Flexibility**: You can change the behavior of an object at runtime by changing its strategy.

---

### Example: Payment Processing
#### Scenario:
You have an e-commerce application that supports different payment methods (e.g., Credit Card, PayPal, Bitcoin).

#### Implementation:
```python
from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using Credit Card ending in {self.card_number[-4:]}.")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using PayPal account: {self.email}.")

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using Bitcoin.")

# Context
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0.0

    def add_item(self, item: str, price: float):
        self.items.append(item)
        self.total += price

    def checkout(self, payment_strategy: PaymentStrategy):
        payment_strategy.pay(self.total)

# Usage
cart = ShoppingCart()
cart.add_item("Laptop", 999.99)
cart.add_item("Mouse", 49.99)

# Choose payment strategy
payment_method = PayPalPayment("user@example.com")
cart.checkout(payment_method)
```

---

### When to Use
1. When you have multiple algorithms for a specific task and want to switch between them easily.
2. When you need to avoid using multiple conditional statements (e.g., `if` or `switch`) to choose an algorithm.
3. When the behavior of a class should be easily configurable and extendable.