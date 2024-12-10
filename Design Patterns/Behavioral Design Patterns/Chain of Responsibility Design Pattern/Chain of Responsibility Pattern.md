The **Chain of Responsibility Design Pattern** is a behavioral pattern that allows multiple objects to handle a request, without the sender needing to know which object will ultimately handle it. The request is passed along a chain of handlers, and each handler in the chain either processes the request or passes it to the next handler in the chain.

### Key Concepts:
1. **Handler**: A base class or interface that defines a method to process a request, often with a reference to the next handler in the chain.
2. **Concrete Handlers**: Specific classes that implement the handling logic for the request. Each handler may either handle the request or pass it to the next handler in the chain.
3. **Client**: The object that sends the request to the first handler in the chain. The client does not need to know which handler will process the request, as it's handled internally by the chain.

### Structure:

```
       Client
          |
   +------v------+
   |  Handler   | <---------+
   +-------------+           |
        |                    |
        v                    v
  +-------------+      +-------------+
  | Concrete    |      | Concrete    |
  | Handler 1   |      | Handler 2   |
  +-------------+      +-------------+
        |                    |
        v                    v
  +-------------+      +-------------+
  | Concrete    |      | Concrete    |
  | Handler 3   |      | Handler N   |
  +-------------+      +-------------+
```

### Example in Code (Python):

Let’s say we have a series of approval levels for a document in an organization (e.g., manager, director, CEO). The request (approval) is passed along the chain of handlers until it is processed.

```python
from abc import ABC, abstractmethod

# Handler (Abstract class)
class ApprovalHandler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler  # Reference to the next handler in the chain

    @abstractmethod
    def handle_request(self, request):
        pass

# Concrete Handlers
class Manager(ApprovalHandler):
    def handle_request(self, request):
        if request <= 10:
            print(f"Manager approved the request of amount {request}")
        elif self.next_handler:
            print("Manager can't approve. Passing to the next level...")
            self.next_handler.handle_request(request)

class Director(ApprovalHandler):
    def handle_request(self, request):
        if request <= 50:
            print(f"Director approved the request of amount {request}")
        elif self.next_handler:
            print("Director can't approve. Passing to the next level...")
            self.next_handler.handle_request(request)

class CEO(ApprovalHandler):
    def handle_request(self, request):
        print(f"CEO approved the request of amount {request}")

# Client code
# Create the chain of responsibility
ceo = CEO()
director = Director(ceo)  # Director passes to CEO
manager = Manager(director)  # Manager passes to Director

# Send requests
manager.handle_request(5)   # Manager approves
manager.handle_request(20)  # Director approves
manager.handle_request(100) # CEO approves
```

### Output:
```
Manager approved the request of amount 5
Manager can't approve. Passing to the next level...
Director approved the request of amount 20
Manager can't approve. Passing to the next level...
Director can't approve. Passing to the next level...
CEO approved the request of amount 100
```

### Explanation:
- **Handler**: The `ApprovalHandler` is an abstract class (or interface) with a method `handle_request` to process the request. It has a reference to the next handler in the chain.
- **Concrete Handlers**: The `Manager`, `Director`, and `CEO` classes are concrete implementations of the `ApprovalHandler` that handle specific ranges of request amounts.
- **Client**: The client creates the chain of handlers (`Manager`, `Director`, `CEO`) and sends the request to the first handler (`manager.handle_request`), which passes it along the chain until the appropriate handler processes the request.

### When to Use the Chain of Responsibility Pattern:
- When you want to decouple the sender of a request from its receivers, allowing multiple handlers to process the request.
- When you want to add or remove responsibilities from the handler chain dynamically without altering the client code.
- When multiple handlers can process the request, and it’s important to let the handlers decide which one is appropriate.
- When the request should be processed by the first handler that can handle it, without needing to know which one that is.

### Advantages:
- **Decouples Sender and Receiver**: The sender does not need to know which handler will process the request, promoting loose coupling between components.
- **Extensibility**: New handlers can be added easily to the chain without modifying the existing code, following the open/closed principle.
- **Flexible Request Handling**: The chain can be dynamically modified to change the order or composition of handlers based on the requirements.
- **Separation of Concerns**: Each handler focuses only on processing its own part of the request, maintaining a clear responsibility.

### Disadvantages:
- **Request Not Always Handled**: If none of the handlers in the chain can process the request, the request will not be handled, leading to potential failure.
- **Complexity**: The pattern can lead to complex chains of handlers, making it difficult to understand and maintain if not designed carefully.
- **Performance Overhead**: If the chain becomes long, the overhead of passing requests through each handler can impact performance.

### Use Cases:
- **Logging**: In logging frameworks, multiple loggers (e.g., file logger, console logger, database logger) can form a chain, and each logger can process messages based on different severity levels.
- **Event Processing**: In event-driven systems where events are processed by multiple handlers (e.g., mouse events, keyboard events), and the events need to be passed through a series of handlers based on certain conditions.
- **Middleware Systems**: In web servers or application frameworks where requests pass through a series of middleware components (e.g., authentication, logging, input validation) before reaching the final handler.

### Summary:
The **Chain of Responsibility Pattern** allows a request to be passed along a chain of handlers, where each handler can process the request or forward it to the next handler. It helps decouple the sender from the receivers, allows flexibility in handling requests, and promotes extensibility by allowing handlers to be added or removed dynamically.