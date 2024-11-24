### **Single Responsibility Principle (SRP)**

**Definition**:  
A class should have only one reason to change, meaning it should focus on a single responsibility or functionality. Each class should encapsulate a single part of the system's functionality.

---

### **Key Points**:
1. **Single Responsibility**:
   - A class should be responsible for one and only one job.
   - This ensures that changes in one part of the system don’t ripple unnecessarily into unrelated areas.

2. **Reason to Change**:
   - If a class has more than one responsibility, changes to one responsibility can unintentionally affect others, increasing the risk of bugs.

3. **Cohesion**:
   - SRP encourages high cohesion—grouping related tasks into a single class or module.

---

### **Benefits**:
- **Improved Readability**: Classes are easier to understand because they have a clear purpose.
- **Easier Maintenance**: Changes to a specific feature are isolated to a single class.
- **Testability**: Each responsibility can be tested independently.
- **Better Reusability**: Classes with a single responsibility are more likely to be reusable in other contexts.

---

### **Examples**

#### **Violating SRP**
Here, the `Invoice` class handles both business logic and file operations.

```python
class Invoice:
    def calculate_total(self):
        # Calculate total amount for the invoice
        pass

    def save_to_file(self, filename):
        # Save the invoice to a file
        pass
```

- **Problems**:
  - If the file-saving logic changes (e.g., saving to a database instead of a file), the `Invoice` class must be modified.
  - Violates SRP by combining two responsibilities: calculating total and saving to a file.

---

#### **Following SRP**
Separate the responsibilities into two classes.

```python
class Invoice:
    def calculate_total(self):
        # Calculate total amount for the invoice
        pass

class FileSaver:
    def save_to_file(self, data, filename):
        # Logic to save data to a file
        pass
```

- **Advantages**:
  - Changes to file-saving logic don’t affect the `Invoice` class.
  - `Invoice` is now focused only on business logic.

---

### **Applying SRP in Real-Life Scenarios**

#### **Example 1: Logging**
- **Violating SRP**: A class combines core functionality with logging.
  ```python
  class DataProcessor:
      def process_data(self):
          print("Processing data...")  # Logging responsibility
          # Core processing logic
  ```
- **Following SRP**: Separate logging into its own class.
  ```python
  class Logger:
      def log(self, message):
          print(message)

  class DataProcessor:
      def __init__(self, logger):
          self.logger = logger

      def process_data(self):
          self.logger.log("Processing data...")
          # Core processing logic
  ```

---

#### **Example 2: User Management**
- **Violating SRP**: A `User` class handles user details and database operations.
  ```python
  class User:
      def __init__(self, username, password):
          self.username = username
          self.password = password

      def save_to_db(self):
          # Logic to save user to a database
          pass
  ```
- **Following SRP**: Split responsibilities into `User` and `UserRepository`.
  ```python
  class User:
      def __init__(self, username, password):
          self.username = username
          self.password = password

  class UserRepository:
      def save_user(self, user):
          # Logic to save user to a database
          pass
  ```

---

### **Identifying Violations of SRP**
1. **Too Many Methods**: A class with numerous unrelated methods often violates SRP.
2. **Multiple Actors**: If multiple teams or stakeholders modify the same class for different purposes, it's a sign of SRP violation.
3. **Long Classes**: Large classes with several responsibilities are candidates for refactoring.

---

### **Conclusion**
The Single Responsibility Principle helps maintain clean, modular, and maintainable code. By isolating responsibilities into individual classes, you reduce coupling, simplify testing, and make future changes easier to implement.

Let me know if you’d like to explore more examples or dive deeper!