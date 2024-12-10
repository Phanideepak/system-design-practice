The **Interpreter Design Pattern** is a behavioral design pattern used to evaluate or process expressions written in a particular language or notation. It provides a way to define a grammar for a language and interpret sentences in that language. The pattern is particularly useful for building interpreters for domain-specific languages (DSLs) or processing custom rules.

### Key Concepts
1. **Abstract Syntax Tree (AST)**: The pattern often represents expressions as a tree structure where each node is an operation or terminal value in the grammar.
2. **Grammar Representation**: The rules of the language are defined using classes or structures, with each class representing a grammatical rule.
3. **Interpreter**: A mechanism to evaluate or interpret the expressions based on the defined grammar.

---

### Participants
1. **Abstract Expression**:  
   Defines the interface for interpreting expressions. This is typically an abstract class or interface.

2. **Terminal Expression**:  
   Represents a leaf node in the AST. It evaluates to a value directly (e.g., constants, variables).

3. **Non-Terminal Expression**:  
   Represents a composite expression (e.g., operators, rules). It delegates interpretation to its child expressions.

4. **Context**:  
   Holds the global state or environment required during interpretation, such as variable values or external data.

5. **Client**:  
   Builds the expression tree and invokes the interpreter.

---

### Example: Mathematical Expression Interpreter
Let's build an interpreter for a simple language that supports addition and subtraction.

#### Code Example (Python)
```python
# Abstract Expression
class Expression:
    def interpret(self, context):
        pass

# Terminal Expression
class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value

# Non-Terminal Expression
class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)

class Subtract(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) - self.right.interpret(context)

# Client
if __name__ == "__main__":
    # Context is not used in this simple example
    context = {}

    # (5 + 3) - (2 + 1)
    expression = Subtract(
        Add(Number(5), Number(3)),
        Add(Number(2), Number(1))
    )

    result = expression.interpret(context)
    print(f"Result: {result}")  # Output: Result: 5
```

---

### Advantages
- **Flexibility**: Can process expressions of varying complexity.
- **Extensibility**: Adding new rules is straightforward by creating new classes.

### Disadvantages
- **Complexity**: The number of classes grows with the complexity of the grammar.
- **Performance**: Not suitable for very complex grammars due to overhead in class management.

### When to Use
- When you have a fixed grammar or language to interpret.
- For building small-scale parsers, rule engines, or DSLs.

The Interpreter Pattern works best when combined with other design patterns, such as Composite (for tree structure) and Visitor (for processing the AST).