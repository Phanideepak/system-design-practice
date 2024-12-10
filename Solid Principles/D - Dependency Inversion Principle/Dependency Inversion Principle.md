### **Dependency Inversion Principle (DIP)**

**Definition**:  
High-level modules should not depend on low-level modules. Both should depend on abstractions.  
Abstractions should not depend on details. Details should depend on abstractions.  

In simpler terms, code should depend on interfaces or abstract classes rather than concrete implementations.

---

### **Key Points**:
1. **High-Level Modules**:
   - Represent the core business logic or policies of an application.
   - Should remain stable and not depend on implementation details.

2. **Low-Level Modules**:
   - Represent the details or specific implementations (e.g., database connections, file systems).
   - Should be designed to align with the abstractions defined by high-level modules.

3. **Inversion of Dependencies**:
   - Traditionally, high-level modules depend on low-level modules. DIP inverts this by introducing abstractions that both depend on.

---

### **Benefits**:
- **Flexibility**: Makes it easy to swap out low-level implementations without affecting high-level modules.
- **Scalability**: Encourages reusable and loosely coupled components.
- **Maintainability**: Reduces the impact of changes in low-level modules on high-level modules.

---

### **Examples**

#### **Violating DIP**
A high-level `OrderService` directly depends on a low-level `EmailNotification` class.

```python
class EmailNotification:
    def send_email(self, message):
        print(f"Sending email: {message}")

class OrderService:
    def __init__(self):
        self.notification = EmailNotification()

    def place_order(self):
        print("Order placed successfully!")
        self.notification.send_email("Order confirmation email.")
```

- **Problems**:
  - `OrderService` is tightly coupled to `EmailNotification`.
  - Changing the notification system (e.g., SMS, push notifications) requires modifying `OrderService`.

---

#### **Following DIP**
Introduce an abstraction that both `OrderService` and `EmailNotification` depend on.

```python
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass

class EmailNotification(Notification):
    def notify(self, message):
        print(f"Sending email: {message}")

class SMSNotification(Notification):
    def notify(self, message):
        print(f"Sending SMS: {message}")

class OrderService:
    def __init__(self, notification: Notification):
        self.notification = notification

    def place_order(self):
        print("Order placed successfully!")
        self.notification.notify("Order confirmation notification.")
```

- **Advantages**:
  - `OrderService` now depends on the `Notification` abstraction, not a specific implementation.
  - Adding a new notification type (e.g., `PushNotification`) requires no changes to `OrderService`.

---

### **Real-World Scenarios**

#### **1. Payment Gateways**
- **Violating DIP**:
  A `PaymentProcessor` directly depends on a specific payment gateway.

  ```python
  class PayPal:
      def process_payment(self):
          print("Processing payment via PayPal")

  class PaymentProcessor:
      def __init__(self):
          self.gateway = PayPal()

      def process(self):
          self.gateway.process_payment()
  ```

- **Following DIP**:
  Introduce an abstraction for payment gateways.

  ```python
  from abc import ABC, abstractmethod

  class PaymentGateway(ABC):
      @abstractmethod
      def process_payment(self):
          pass

  class PayPal(PaymentGateway):
      def process_payment(self):
          print("Processing payment via PayPal")

  class Stripe(PaymentGateway):
      def process_payment(self):
          print("Processing payment via Stripe")

  class PaymentProcessor:
      def __init__(self, gateway: PaymentGateway):
          self.gateway = gateway

      def process(self):
          self.gateway.process_payment()
  ```

  - Switching between PayPal and Stripe only requires changing the passed gateway.

---

#### **2. Database Access**
- **Violating DIP**:
  A `UserRepository` directly depends on a SQL database.

  ```python
  class SQLDatabase:
      def query(self, sql):
          print(f"Executing SQL: {sql}")

  class UserRepository:
      def __init__(self):
          self.db = SQLDatabase()

      def get_user(self, user_id):
          self.db.query(f"SELECT * FROM users WHERE id = {user_id}")
  ```

- **Following DIP**:
  Use an abstraction for database access.

  ```python
  from abc import ABC, abstractmethod

  class Database(ABC):
      @abstractmethod
      def query(self, query):
          pass

  class SQLDatabase(Database):
      def query(self, query):
          print(f"Executing SQL: {query}")

  class NoSQLDatabase(Database):
      def query(self, query):
          print(f"Executing NoSQL: {query}")

  class UserRepository:
      def __init__(self, db: Database):
          self.db = db

      def get_user(self, user_id):
          self.db.query(f"SELECT * FROM users WHERE id = {user_id}")
  ```

  - Switching from SQL to NoSQL is seamless.

---

### **Best Practices for DIP**

1. **Use Dependency Injection**:
   - Inject dependencies (like interfaces or abstract classes) into classes instead of hardcoding them.

2. **Rely on Abstractions**:
   - Use interfaces or abstract base classes for dependencies.
   
3. **Avoid Tight Coupling**:
   - Ensure that high-level modules do not directly depend on the implementation details of low-level modules.

4. **Design Patterns**:
   - Use patterns like **Strategy**, **Adapter**, or **Dependency Injection** to enforce DIP.

---

### **Identifying Violations**
- **Direct Instantiation**:
  - High-level modules directly create instances of low-level modules.
  
- **Tight Coupling**:
  - High-level modules directly reference low-level implementation details.
  
- **Frequent Changes**:
  - Modifying low-level modules often requires changes to high-level modules.

---

### **Summary**

| Aspect               | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| **Focus**            | High-level and low-level modules depend on abstractions, not each other.    |
| **Key Mechanism**    | Use abstractions (interfaces, abstract classes) to decouple dependencies.   |
| **Benefits**         | Flexibility, scalability, and maintainability.                             |

---