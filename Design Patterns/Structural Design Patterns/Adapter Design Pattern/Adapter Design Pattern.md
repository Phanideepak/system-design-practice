### **Adapter Design Pattern**

The **Adapter** design pattern is a structural design pattern that allows incompatible interfaces to work together by translating one interface into another. It acts as a bridge between two systems, enabling them to communicate without modifying their source code.

---

### **Key Features**:
1. **Interface Compatibility**:  
   Converts the interface of one class into another that a client expects.
   
2. **Reusability**:  
   Enables the reuse of existing classes without altering their source code.

3. **Decoupling**:  
   Decouples the client from the implementation details of the adapted class.

---

### **When to Use**:
- When you want to use an existing class but its interface is incompatible with the rest of the system.
- When you need to integrate a third-party or legacy system that doesn’t match your codebase.

---

### **Advantages**:
- **Increases Flexibility**: Adapts existing code without modifying it.
- **Promotes Reusability**: Allows integration of otherwise incompatible systems.

### **Disadvantages**:
- **Increased Complexity**: Introduces additional layers, which can complicate the design.

---

### **Types of Adapters**:

1. **Class Adapter**:  
   Uses multiple inheritance to adapt one interface to another.
   
2. **Object Adapter**:  
   Uses composition to adapt the interface by wrapping the existing object.

---

### **Implementation**

#### **1. Object Adapter Example**

```python
# Existing class with an incompatible interface
class OldSystem:
    def specific_request(self):
        return "Old System: Specific Request"

# Target interface
class NewSystem:
    def request(self):
        pass

# Adapter that translates OldSystem to NewSystem
class Adapter(NewSystem):
    def __init__(self, old_system):
        self.old_system = old_system

    def request(self):
        return self.old_system.specific_request()

# Client Code
old_system = OldSystem()
adapter = Adapter(old_system)
print(adapter.request())  # Output: Old System: Specific Request
```

---

#### **2. Class Adapter Example (Using Multiple Inheritance)**

```python
# Existing class with incompatible interface
class OldSystem:
    def specific_request(self):
        return "Old System: Specific Request"

# Target interface
class NewSystem:
    def request(self):
        pass

# Adapter that inherits from both interfaces
class ClassAdapter(OldSystem, NewSystem):
    def request(self):
        return self.specific_request()

# Client Code
adapter = ClassAdapter()
print(adapter.request())  # Output: Old System: Specific Request
```

---

### **Real-World Examples**

#### **1. Integrating Legacy Code**
Suppose you have a payment system using an old interface, and you need to adapt it to work with a new system.

```python
class OldPaymentGateway:
    def process_payment(self, amount):
        return f"Processing payment of ${amount} through Old Gateway"

class NewPaymentGateway:
    def make_payment(self, amount):
        pass

class PaymentAdapter(NewPaymentGateway):
    def __init__(self, old_gateway):
        self.old_gateway = old_gateway

    def make_payment(self, amount):
        return self.old_gateway.process_payment(amount)

# Usage
old_gateway = OldPaymentGateway()
adapter = PaymentAdapter(old_gateway)
print(adapter.make_payment(100))  # Output: Processing payment of $100 through Old Gateway
```

---

#### **2. Using Python Libraries**
If a library provides data in one format but your codebase expects another, an adapter can bridge the gap.

```python
# Third-party library providing data
class ThirdPartyAPI:
    def get_json_data(self):
        return '{"name": "John", "age": 30}'

# Expected format in your system
class DataProcessor:
    def process_data(self, data):
        return f"Processing: {data}"

# Adapter to convert JSON to dictionary
import json

class APIAdapter:
    def __init__(self, api):
        self.api = api

    def get_data(self):
        json_data = self.api.get_json_data()
        return json.loads(json_data)

# Usage
api = ThirdPartyAPI()
adapter = APIAdapter(api)
processor = DataProcessor()
data = adapter.get_data()
print(processor.process_data(data))  # Output: Processing: {'name': 'John', 'age': 30}
```

---

### **UML Representation**

- **Client**: The entity that uses the Target interface.
- **Target**: The expected interface by the Client.
- **Adaptee**: The existing class with an incompatible interface.
- **Adapter**: The bridge that converts Adaptee's interface to Target's interface.

```
Client -> Target
         ^
         |
       Adapter
         |
      Adaptee
```

---

### **Comparison with Other Patterns**

| **Aspect**       | **Adapter**                                | **Facade**                          | **Decorator**                     |
|-------------------|--------------------------------------------|--------------------------------------|-----------------------------------|
| **Purpose**       | Convert one interface into another.        | Simplify access to a subsystem.     | Add responsibilities dynamically. |
| **Scope**         | Works on one specific class or system.     | Works on an entire subsystem.       | Enhances functionality of an object. |
| **Complexity**    | Moderate.                                  | Low.                                | Moderate to High.                 |

---

### **Summary**

| **Aspect**               | **Details**                                                        |
|--------------------------|--------------------------------------------------------------------|
| **Intent**               | Convert an interface into another expected by the client.         |
| **Key Components**       | Target, Adaptee, Adapter, Client.                                 |
| **Advantages**           | Enables integration of incompatible interfaces.                  |
| **Disadvantages**        | Adds complexity through additional layers.                       |
| **Common Use Cases**     | Legacy code integration, third-party library adaptation, APIs.    |