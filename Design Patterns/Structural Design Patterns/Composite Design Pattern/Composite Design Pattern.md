### **Composite Design Pattern**

The **Composite Design Pattern** is a structural design pattern that allows you to compose objects into tree-like structures to represent part-whole hierarchies. This pattern lets clients treat individual objects and compositions of objects uniformly.

---

### **Key Concepts**

1. **Component**:
   - An abstract base class or interface that defines the common functionality for both leaf and composite nodes.

2. **Leaf**:
   - Represents individual objects in the hierarchy that cannot have children.

3. **Composite**:
   - Represents complex objects that can have children. It implements the `Component` interface and manages its child components.

4. **Client**:
   - Interacts with objects through the `Component` interface without worrying about whether they are `Leaf` or `Composite`.

---

### **Use Case**

Use the Composite Design Pattern when:
- You need to represent a tree structure, such as a file system, organization chart, or UI component hierarchy.
- You want clients to treat individual objects and groups of objects the same way.

---

### **Class Diagram**

```
Component (Interface or Abstract Class)
    + operation()

Leaf (Implements Component)
    + operation()

Composite (Implements Component)
    + operation()
    + add(component)
    + remove(component)
    + getChild(index)
```

---

### **Python Implementation**

#### **Example: File System**

```python
from abc import ABC, abstractmethod

# Component: Abstract base class
class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass


# Leaf: Represents individual files
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print(" " * indent + f"File: {self.name}")


# Composite: Represents directories that can contain files or other directories
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def display(self, indent=0):
        print(" " * indent + f"Directory: {self.name}")
        for child in self.children:
            child.display(indent + 2)


# Client code
if __name__ == "__main__":
    # Create files
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    file3 = File("file3.txt")

    # Create directories
    dir1 = Directory("dir1")
    dir2 = Directory("dir2")
    root = Directory("root")

    # Build the tree structure
    dir1.add(file1)
    dir1.add(file2)
    dir2.add(file3)
    root.add(dir1)
    root.add(dir2)

    # Display the file system structure
    root.display()
```

#### **Output**:
```
Directory: root
  Directory: dir1
    File: file1.txt
    File: file2.txt
  Directory: dir2
    File: file3.txt
```

---

### **Advantages**

1. **Flexibility**:
   - Add or remove components easily without affecting the client code.

2. **Uniformity**:
   - Treat individual objects and composite structures uniformly.

3. **Simplifies Client Code**:
   - Reduces the complexity of client code by abstracting away tree traversal and management.

---

### **Disadvantages**

1. **Complexity**:
   - Managing child components and maintaining tree structures can add overhead.

2. **Type Safety**:
   - It may be difficult to enforce restrictions on which components can be children of others.

---

### **Real-World Examples**

1. **File System**:
   - Files and directories where directories can contain files or other directories.

2. **UI Components**:
   - Buttons, panels, and windows in GUI frameworks.

3. **Organization Hierarchy**:
   - Employees and managers in a company structure.

---