The **Memento Design Pattern** is a behavioral design pattern used to capture and store the current state of an object so that it can be restored later. This pattern is particularly useful for implementing features like undo/redo operations.

---

### Key Concepts
1. **State Preservation**: Allows saving and restoring the state of an object without exposing its internal details.
2. **Encapsulation**: Keeps the memento's contents private from other objects, ensuring only the originator can access or modify it.
3. **Temporal Control**: Useful for maintaining a history of states for objects.

---

### Participants
1. **Originator**:
   - The object whose state is to be saved and restored.
   - Creates mementos and restores its state from them.

2. **Memento**:
   - A representation of the saved state.
   - Provides encapsulation to ensure the originator is the only object with access to the state details.

3. **Caretaker**:
   - Manages the memento objects (e.g., storing and retrieving them).
   - Doesn't modify or access the contents of the memento.

---

### Example: Text Editor with Undo Functionality

Let's build a simple text editor that supports undo operations.

#### Code Example (Python)

```python
# Memento
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

# Originator
class TextEditor:
    def __init__(self):
        self._content = ""

    def write(self, text):
        self._content += text

    def save(self):
        return Memento(self._content)

    def restore(self, memento):
        self._content = memento.get_state()

    def show_content(self):
        print(f"Content: '{self._content}'")

# Caretaker
class History:
    def __init__(self):
        self._mementos = []

    def save(self, memento):
        self._mementos.append(memento)

    def undo(self):
        if self._mementos:
            return self._mementos.pop()
        return None

# Client Code
if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    # Writing and saving states
    editor.write("Hello, ")
    history.save(editor.save())

    editor.write("world!")
    history.save(editor.save())

    editor.write(" More text.")
    editor.show_content()

    # Undo operations
    editor.restore(history.undo())
    editor.show_content()

    editor.restore(history.undo())
    editor.show_content()
```

---

### Output
```
Content: 'Hello, world! More text.'
Content: 'Hello, world!'
Content: 'Hello, '
```

---

### Advantages
- **Encapsulation**: Keeps the internal state private while still enabling external objects to save and restore it.
- **State Management**: Simplifies management of an object's state history, enabling undo/redo functionality.
- **Separation of Concerns**: The caretaker manages the history, leaving the originator to focus on its primary behavior.

### Disadvantages
- **Memory Overhead**: Storing many mementos can be costly in terms of memory.
- **Limited Scope**: Does not support partial state saves unless explicitly implemented.

---

### When to Use
- When you need to save snapshots of an object's state to restore later.
- For implementing undo/redo functionality.
- When the internal state of an object must be preserved without exposing its details to other parts of the system.