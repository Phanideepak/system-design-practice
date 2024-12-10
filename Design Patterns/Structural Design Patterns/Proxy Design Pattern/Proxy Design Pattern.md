The **Proxy Pattern** is a structural design pattern that provides an object representing another object. It acts as an intermediary or placeholder for the real object and controls access to it. The Proxy can add additional functionality such as access control, logging, lazy initialization, or remote communication, without modifying the original object.

### Types of Proxy Patterns:
1. **Virtual Proxy**: This is used to delay the creation of a resource-heavy object until it’s actually needed (lazy initialization).
2. **Protection Proxy**: This type is used to control access to an object, usually for security reasons. It can enforce permissions or restrict access based on roles.
3. **Remote Proxy**: Used when an object is located remotely (e.g., over a network), and the proxy serves as a local representative or placeholder for the real object.
4. **Cache Proxy**: Used to store temporary results (caching) to improve performance by avoiding repeated calculations or network requests.

### Key Concepts:
1. **Subject**: An interface or abstract class that both the RealObject and Proxy implement.
2. **RealSubject**: The actual object that performs the real operations.
3. **Proxy**: The object that controls access to the RealSubject, potentially adding additional behavior or logic (such as access control or lazy initialization).

### Structure:

```
          Subject
             ^
             |
       +-------------+
       |   Proxy    |
       +-------------+
            |
    +----------------+
    |   RealSubject  |
    +----------------+
```

### Example in Code (Python):

```python
from abc import ABC, abstractmethod

# Subject Interface
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# RealSubject: The actual image class that performs the real action
class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"Loading image {self.filename} from disk...")

    def display(self):
        print(f"Displaying image {self.filename}")

# Proxy: Controls access to the RealSubject
class ImageProxy(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._real_image = None

    def display(self):
        if not self._real_image:
            self._real_image = RealImage(self.filename)  # Lazy initialization
        self._real_image.display()

# Using Proxy to control access to RealSubject
proxy_image = ImageProxy("photo.jpg")
proxy_image.display()  # Loads and displays the image
proxy_image.display()  # Displays the image without loading (since it's cached)
```

### Output:
```
Loading image photo.jpg from disk...
Displaying image photo.jpg
Displaying image photo.jpg
```

### When to Use the Proxy Pattern:
- When you need to control access to an object, such as for security or performance reasons.
- When the real object is resource-heavy and should only be created when needed (lazy loading).
- When dealing with remote objects and you want to provide a local placeholder (remote proxy).
- When you want to add extra functionalities (like caching) to an object without modifying it directly.

### Advantages:
- **Control Access**: The Proxy can restrict or control access to the real object.
- **Lazy Initialization**: Delays the creation of a resource-heavy object until necessary (virtual proxy).
- **Separation of Concerns**: The proxy encapsulates the additional behavior, keeping it separate from the real object.
- **Enhanced Performance**: By using caching proxies, you can improve performance by avoiding redundant work (e.g., fetching data from a remote server).

### Disadvantages:
- **Complexity**: Introducing proxies adds an extra layer of abstraction, which may make the system harder to understand or maintain.
- **Performance Overhead**: The proxy itself can introduce additional overhead, especially if it adds extra layers of indirection.

### Use Cases:
- **Virtual Proxy**: Image rendering, where the image file is only loaded when it’s displayed.
- **Protection Proxy**: A user authentication system where access to certain services is restricted based on roles.
- **Remote Proxy**: A client application accessing a service over a network (e.g., remote database access).
- **Cache Proxy**: A proxy that stores the results of expensive operations (like database queries) to speed up subsequent requests.