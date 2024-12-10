The **Decorator Design Pattern** is a structural pattern used to add new functionality to an object dynamically, without altering its structure. It allows for behavior extension by "wrapping" objects in new decorators, which enhance or modify the behavior of the original object.

### Key Concepts:
1. **Component**: An interface or abstract class that defines the methods that can be dynamically added or extended.
2. **Concrete Component**: A class that implements the Component interface and defines basic functionality.
3. **Decorator**: A class that implements the Component interface and "wraps" a Concrete Component to add new behavior. It delegates calls to the wrapped component, extending its functionality.
4. **Concrete Decorators**: Specific implementations of the Decorator that add additional behavior.

### Structure:
```
  Component
     ^
     |
  ConcreteComponent
     ^
     |
  Decorator
     ^
     |
 ConcreteDecorator
```

### Example in Code (Python):

```python
from abc import ABC, abstractmethod

# Component Interface
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 5.0

# Decorator (Abstract)
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    @abstractmethod
    def cost(self) -> float:
        pass

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 1.5

class SugarDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.5

# Using the decorators
simple_coffee = SimpleCoffee()
print(f"Cost of Simple Coffee: ${simple_coffee.cost()}")

milk_coffee = MilkDecorator(simple_coffee)
print(f"Cost of Coffee with Milk: ${milk_coffee.cost()}")

sugar_milk_coffee = SugarDecorator(milk_coffee)
print(f"Cost of Coffee with Milk and Sugar: ${sugar_milk_coffee.cost()}")
```

### Output:
```
Cost of Simple Coffee: $5.0
Cost of Coffee with Milk: $6.5
Cost of Coffee with Milk and Sugar: $7.0
```

### When to Use the Decorator Pattern:
- When you need to add responsibilities to objects dynamically and in a flexible way.
- When subclassing would lead to an exponential rise in new classes for every possible combination of behaviors.
- When you want to keep the original class unchanged but allow additional features to be added.

### Advantages:
- **Flexible**: You can add or remove decorators at runtime.
- **Avoids subclassing**: Instead of creating a new class for each combination of behavior, you can simply wrap decorators.
- **Single Responsibility Principle**: Each decorator is focused on a specific behavior, adhering to the SRP.

### Disadvantages:
- **Complexity**: Too many decorators can lead to a system that's difficult to understand or maintain.
- **Multiple Wrapping**: If the decorator chain is too deep, it may become cumbersome to track or manage.