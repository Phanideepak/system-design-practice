The **Flyweight Pattern** is a structural design pattern that aims to reduce the number of objects created by sharing common objects, rather than creating new ones each time. It is used when a system needs to create a large number of similar objects that consume a lot of memory, and there’s an opportunity to share some of their data.

The Flyweight pattern helps in minimizing memory usage by storing shared data externally, allowing many objects to share the same data rather than duplicating it. This is especially useful in cases where the objects have many common properties, but only a small subset of their data is unique.

### Key Concepts:
1. **Flyweight**: The object that shares common data. It stores the intrinsic state (common or shared data).
2. **Intrinsic State**: The shared state of the object that is immutable and can be shared among multiple Flyweights.
3. **Extrinsic State**: The unique state of the object, which cannot be shared. This is usually provided by the client at runtime.
4. **Flyweight Factory**: A factory that manages and reuses existing Flyweight objects. It ensures that shared Flyweights are used when appropriate and creates new Flyweights if necessary.

### Structure:
```
                +----------------+
                |  Flyweight     |
                +----------------+
                | - Intrinsic    |
                |   State        |
                | + Operation()  |
                +----------------+
                       ^
                       |
       +-----------------------------------+
       |                                   |
+---------------+                +---------------+
| ConcreteFlyweight |              | ConcreteFlyweight |
+---------------+                +---------------+
| - Intrinsic    |               | - Intrinsic    |
|   State        |               |   State        |
+---------------+                +---------------+
       ^
       |
 +--------------------+
 | Flyweight Factory  |
 +--------------------+
 | - Flyweights       |
 | + GetFlyweight()   |
 +--------------------+
```

### Example in Code (Python):

```python
class Character:
    """Flyweight class representing a character."""
    def __init__(self, symbol: str):
        self.symbol = symbol  # Intrinsic state (shared)

    def display(self, x: int, y: int):
        print(f"Character {self.symbol} at position ({x}, {y})")

class CharacterFactory:
    """Flyweight Factory that manages shared characters."""
    def __init__(self):
        self._characters = {}

    def get_character(self, symbol: str) -> Character:
        """Returns an existing Character object or creates a new one."""
        if symbol not in self._characters:
            self._characters[symbol] = Character(symbol)
            print(f"Creating character '{symbol}'")
        return self._characters[symbol]

# Client code
factory = CharacterFactory()

# Using shared Flyweights
c1 = factory.get_character('A')
c2 = factory.get_character('B')
c3 = factory.get_character('A')  # Reuses the 'A' character
c4 = factory.get_character('C')

# Displaying characters with unique extrinsic state (position)
c1.display(0, 0)
c2.display(1, 1)
c3.display(2, 2)
c4.display(3, 3)
```

### Output:
```
Creating character 'A'
Creating character 'B'
Creating character 'C'
Character A at position (0, 0)
Character B at position (1, 1)
Character A at position (2, 2)
Character C at position (3, 3)
```

### Explanation:
- **Intrinsic state**: The `Character` class stores the symbol (e.g., 'A', 'B', 'C') as the intrinsic state, which is shared across all instances of the same character.
- **Extrinsic state**: The position `(x, y)` is the extrinsic state, passed in as arguments when calling the `display()` method. This state is unique for each instance and can change dynamically.
- **Flyweight Factory**: The `CharacterFactory` class manages the creation and reuse of `Character` objects. It ensures that only one instance of each unique character is created and reused.

### When to Use the Flyweight Pattern:
- When your application needs to create a large number of objects that have a significant amount of shared state.
- When object creation is expensive in terms of memory or computation, and sharing objects would save resources.
- When the shared state is immutable or can be reused across instances, and only the extrinsic state changes.

### Advantages:
- **Memory Efficiency**: The Flyweight pattern minimizes memory consumption by sharing common data among multiple objects.
- **Improved Performance**: Since the intrinsic state is shared, fewer objects are created, improving performance by reducing the number of allocations.
- **Reduced Object Creation**: It reduces the number of instances created, which can be particularly useful in scenarios where a large number of objects are needed.

### Disadvantages:
- **Complexity**: The pattern can introduce additional complexity to the design, especially when managing shared and extrinsic states.
- **Increased Coupling**: Since the client needs to pass the extrinsic state to the Flyweight, there may be tighter coupling between the client and the Flyweight object.
- **State Management**: Managing the distinction between intrinsic and extrinsic states can become cumbersome, especially in complex systems with many object variations.

### Use Cases:
- **Text Rendering**: In applications like text editors or word processors where characters, words, or formatting options can be shared across different parts of a document.
- **Graphical Systems**: Games or graphic applications where many similar objects (like pixels or shapes) need to be rendered with minimal memory usage.
- **Database Querying**: When querying a large dataset where certain queries are repeated frequently, and sharing query results can save memory.

The Flyweight pattern is particularly useful when you need to scale the number of objects in a system while keeping resource consumption minimal.