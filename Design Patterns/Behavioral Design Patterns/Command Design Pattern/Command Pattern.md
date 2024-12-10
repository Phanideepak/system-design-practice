The **Command Design Pattern** is a behavioral design pattern that encapsulates a request as an object, thereby allowing you to parameterize objects with different requests, queue or log requests, and support undoable operations. It’s particularly useful in situations where you need to decouple the sender of a request from its receiver.

---

## **Key Components of the Command Pattern**

1. **Command Interface**:  
   Defines a single method (e.g., `execute()`) that all concrete commands must implement. Optionally, it may also have an `undo()` method.

2. **Concrete Command**:  
   Implements the `Command` interface and defines the binding between a receiver and the actions to be performed. This is the "real" command that performs a specific action.

3. **Receiver**:  
   The object that performs the actual work when the command is executed. The receiver contains the business logic.

4. **Invoker**:  
   Responsible for calling the command’s `execute()` method. It maintains a reference to the command object and can also queue commands.

5. **Client**:  
   Creates and configures the concrete commands, receivers, and assigns commands to the invoker.

---

## **Example Workflow**

1. A client creates a `ConcreteCommand`, passing a reference to a `Receiver`.
2. The client assigns the command to an `Invoker`.
3. The `Invoker` executes the command.
4. The `Receiver` performs the action.

---

## **Example: Remote Control for Light**

Here’s an implementation in Python:

```python
# Command Interface
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Receiver
class Light:
    def turn_on(self):
        print("Light is ON")
    
    def turn_off(self):
        print("Light is OFF")

# Concrete Command
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

    def press_undo(self):
        if self.command:
            self.command.undo()

# Client
light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote = RemoteControl()

# Turn light ON
remote.set_command(light_on)
remote.press_button()

# Undo the operation
remote.press_undo()

# Turn light OFF
remote.set_command(light_off)
remote.press_button()

# Undo the operation
remote.press_undo()
```

---

### **Benefits of the Command Pattern**
- **Decoupling**: Separates the invoker from the object that knows how to perform the action.
- **Flexibility**: You can add new commands without changing existing code.
- **Undo/Redo Operations**: Easily support undoable and redoable actions by implementing an `undo()` method.

### **Drawbacks**
- **Complexity**: Increases the number of classes in your design.
- **Overhead**: May introduce unnecessary layers if the actions are simple.

The Command Pattern is widely used in applications like graphical user interfaces (GUIs), task queues, and macro recorders.