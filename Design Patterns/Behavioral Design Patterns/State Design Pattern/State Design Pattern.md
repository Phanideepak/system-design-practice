The **State Design Pattern** is a behavioral design pattern that allows an object to alter its behavior when its internal state changes. This pattern encapsulates state-specific behavior into separate classes, enabling the object to delegate behavior to the current state object.

---

### Key Concepts
1. **State Encapsulation**:
   - Each state is represented as a distinct class.
   - The context object delegates state-specific behavior to the current state instance.
2. **Behavioral Change**:
   - Changing the state object dynamically changes the behavior of the context.
3. **Open/Closed Principle**:
   - New states can be added without modifying the existing codebase.

---

### Participants
1. **Context**:
   - Maintains a reference to the current state object.
   - Delegates state-specific behavior to the state object.

2. **State (Interface/Abstract Class)**:
   - Defines the interface for behavior associated with a particular state.

3. **Concrete States**:
   - Implements behavior specific to a particular state.

---

### Example: Traffic Light System

A traffic light can be in one of three states: Green, Yellow, or Red. The behavior (e.g., transition rules) changes based on the current state.

#### Code Example (Python)

```python
from abc import ABC, abstractmethod

# State Interface
class TrafficLightState(ABC):
    @abstractmethod
    def handle_request(self, context):
        pass

# Concrete States
class GreenLight(TrafficLightState):
    def handle_request(self, context):
        print("Green Light: Go!")
        context.set_state(YellowLight())

class YellowLight(TrafficLightState):
    def handle_request(self, context):
        print("Yellow Light: Prepare to stop.")
        context.set_state(RedLight())

class RedLight(TrafficLightState):
    def handle_request(self, context):
        print("Red Light: Stop!")
        context.set_state(GreenLight())

# Context
class TrafficLight:
    def __init__(self):
        self._state = RedLight()  # Initial state

    def set_state(self, state):
        self._state = state

    def request(self):
        self._state.handle_request(self)

# Client Code
if __name__ == "__main__":
    traffic_light = TrafficLight()

    # Simulate traffic light changes
    for _ in range(6):
        traffic_light.request()
```

---

### Output
```
Red Light: Stop!
Green Light: Go!
Yellow Light: Prepare to stop.
Red Light: Stop!
Green Light: Go!
Yellow Light: Prepare to stop.
```

---

### Advantages
1. **Encapsulation**:
   - State-specific behavior is encapsulated in separate classes, improving modularity.
2. **Simplifies Context**:
   - The context class delegates behavior to state objects, reducing complexity.
3. **Extensibility**:
   - Adding new states is straightforward without modifying the context or existing states.

### Disadvantages
1. **Increased Complexity**:
   - Introduces additional classes for each state, which can increase the codebase size.
2. **Tight Coupling**:
   - The context must know and manage all possible states.

---

### When to Use
- When an object’s behavior depends on its state, and it must change behavior dynamically at runtime.
- To eliminate large conditionals (e.g., `if-else` or `switch` statements) that check for the object's state.
- For systems with finite, well-defined states, such as vending machines, game character states, or workflow processes.