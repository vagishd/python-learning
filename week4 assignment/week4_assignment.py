from functools import wraps
from collections import namedtuple
import time

# Q1: Object Modeling & Core OOP
print("=" * 20)
print("Q1: Object Modeling & Core OOP - Multi-role User Management System")
print("=" * 20)


class User:
    total_active_users = 0

    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.is_active = True
        User.total_active_users += 1

    def get_role(self):
        return "User"

    def deactivate(self):
        if self.is_active:
            self.is_active = False
            User.total_active_users -= 1

    def __str__(self):
        return f"{self.name} ({self.email})"


class Admin(User):

    def __init__(self, user_id, name, email, admin_level):
        super().__init__(user_id, name, email)
        self.admin_level = admin_level

    def get_role(self):
        return "Admin"

    def manage_system(self):
        return f"Admin {self.name} is managing the system at level {self.admin_level}"


class Student(User):

    def __init__(self, user_id, name, email, student_id):
        super().__init__(user_id, name, email)
        self.student_id = student_id
        self.courses = []

    def get_role(self):
        return "Student"

    def enroll_course(self, course_name):
        self.courses.append(course_name)
        return f"Student {self.name} enrolled in {course_name}"


class Teacher(User):

    def __init__(self, user_id, name, email, department):
        super().__init__(user_id, name, email)
        self.department = department

    def get_role(self):
        return "Teacher"

    def teach_course(self, course_name):
        return f"Teacher {self.name} is teaching {course_name} in {self.department}"


admin1 = Admin("A001", "test user 1", "testuser1@admin.com", "Super Admin")
student1 = Student("S001", "test user 2", "testuser2@student.com", "STU123")
teacher1 = Teacher("T001", "test user 3", "testuser3@teacher.com", "Computer Science")

print(f"Admin: {admin1.get_role()} - {admin1}")
print(f"Student: {student1.get_role()} - {student1}")
print(f"Teacher: {teacher1.get_role()} - {teacher1}")
print(f"Total Active Users: {User.total_active_users}")
print()

# Q2: Advanced Class Construction (classmethod and staticmethod)
print("=" * 20)
print("Q2: Advanced Class Construction - classmethod and staticmethod")
print("=" * 20)


class Product:

    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    @classmethod
    def from_string(cls, product_string):
        # Format: "id:name:price"
        parts = product_string.split(":")
        return cls(parts[0], parts[1], float(parts[2]))

    @staticmethod
    def is_valid_price(price):
        return price > 0 and isinstance(price, (int, float))

    def __str__(self):
        return f"Product({self.product_id}, {self.name}, ${self.price})"


product1 = Product.from_string("P001:Laptop:999.99")
print(f"Created from string: {product1}")
print(f"Is 50.0 a valid price? {Product.is_valid_price(50.0)}")
print(f"Is -10 a valid price? {Product.is_valid_price(-10)}")
print()

# Q3: Deep Usage of Special Methods
print("=" * 20)
print("Q3: Special Methods - __str__, __repr__, __len__, __eq__, __lt__, __call__")
print("=" * 20)


class Book:

    def __init__(self, title, author, pages, isbn):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):

        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages}, isbn='{self.isbn}')"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.isbn == other.isbn

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages

    def __call__(self, action):
        if action == "read":
            return f"Reading '{self.title}'..."
        elif action == "info":
            return f"Book Info: {self.__str__()}, {self.pages} pages"
        else:
            return f"Unknown action: {action}"


book1 = Book("Python Basics", "test user 1", 300, "ISBN-001")
book2 = Book("Advanced Python", "test user 2", 500, "ISBN-002")
book3 = Book("Python Basics", "test user 2", 300, "ISBN-001")

print(f"__str__: {str(book1)}")
print(f"__repr__: {repr(book1)}")
print(f"__len__: {len(book1)} pages")
print(f"__eq__: book1 == book3? {book1 == book3}")
print(f"__eq__: book1 == book2? {book1 == book2}")
print(f"__lt__: book1 < book2? {book1 < book2}")
print(f"__call__: book1('read') = {book1('read')}")
print(f"__call__: book1('info') = {book1('info')}")
print()

# Q4: Decorator-Driven Behavior Control
print("=" * 20)
print("Q4: Decorator-Driven Behavior Control")
print("=" * 20)


def log_execution(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"[LOG] Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        print(f"[LOG] Arguments: args={args}, kwargs={kwargs}")
        print(f"[LOG] Result: {result}")
        return result

    return wrapper


def conditional_log(enable=True):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if enable:
                print(f"[CONDITIONAL LOG] Calling '{func.__name__}' with args={args}")
            result = func(*args, **kwargs)
            if enable:
                print(f"[CONDITIONAL LOG] '{func.__name__}' returned: {result}")
            return result

        return wrapper

    return decorator


class Calculator:

    @log_execution
    def add(self, a, b):
        return a + b

    @log_execution
    def multiply(self, a, b):
        return a * b

    @conditional_log(enable=True)
    def subtract(self, a, b):
        return a - b

    @conditional_log(enable=False)
    def divide(self, a, b):
        return a / b if b != 0 else "Cannot divide by zero"



calc = Calculator()
print("Testing log_execution decorator:")
result1 = calc.add(5, 3)
print()

print("Testing conditional_log decorator (enabled):")
result2 = calc.subtract(10, 4)
print()

print("Testing conditional_log decorator (disabled):")
result3 = calc.divide(20, 4)
print()

# Q5: Generator-Based Data Streaming
print("=" * 20)
print("Q5: Generator-Based Data Streaming")
print("=" * 20)


class DataProcessor:

    def __init__(self, data):
        self.data = data

    def process_lazy(self, start_index=0):

        for i in range(start_index, len(self.data)):
            processed_item = self.data[i] * 2
            yield processed_item

    def get_all_processed(self):
        return [item * 2 for item in self.data]


# Demonstrate Q5
large_dataset = list(range(1, 50))
processor = DataProcessor(large_dataset)

print("Using generator (lazy processing, partial consumption):")
gen = processor.process_lazy()
print(f"First 3 items: {[next(gen) for _ in range(3)]}")
print(f"Next 2 items: {[next(gen) for _ in range(2)]}")
print(f"Remaining items: {list(gen)}")
print()

print("Resuming from index 5:")
gen2 = processor.process_lazy(start_index=5)
print(f"Items from index 5: {list(gen2)}")
print()

# Q6: Immutable Data Modeling with namedtuple
print("=" * 20)
print("Q6: Immutable Data Modeling with namedtuple")
print("=" * 20)

Configuration = namedtuple('Configuration', ['app_name', 'version', 'debug_mode', 'max_users'])


class AppSettings:

    def __init__(self):
        self.configs = []

    def add_config(self, config):
        self.configs.append(config)

    def get_latest_config(self):
        return self.configs[-1] if self.configs else None

    def get_config_by_version(self, version):
        for config in self.configs:
            if config.version == version:
                return config
        return None



settings = AppSettings()


config1 = Configuration("MyApp", "1.0", False, 100)
config2 = Configuration("MyApp", "2.0", True, 500)

settings.add_config(config1)
settings.add_config(config2)

print(f"Latest config: {settings.get_latest_config()}")
print(f"Config v1.0: {settings.get_config_by_version('1.0')}")

# Demonstrate immutability (trying to modify will raise AttributeError)
print(f"\nImmutability demonstration:")
print(f"Config fields: {config1.app_name}, {config1.version}, {config1.debug_mode}")
print("Note: config1.app_name = 'NewName' would raise AttributeError (immutable)")
print()

# Q7: Control Flow with Loop else# ============================================================================
print("=" * 20)
print("Q7: Control Flow with Loop else")
print("=" * 20)


def search_user(users, target_email):

    for user in users:
        if user.email == target_email:
            print(f"User found: {user.name}")
            break
    else:
        print(f"User with email '{target_email}' not found")


def validate_number(numbers, min_value):

    for num in numbers:
        if num < min_value:
            print(f"Validation failed: {num} is less than {min_value}")
            break
    else:
        print(f"All numbers are >= {min_value}")


# Demonstrate Q7
users_list = [admin1, student1, teacher1]
print("Search for existing user:")
search_user(users_list, "testuser1@student.com")
print()

print("Search for non-existing user:")
search_user(users_list, "notfound@email.com")
print()

print("Validate numbers (all valid):")
validate_number([10, 20, 30], 5)
print()

print("Validate numbers (one invalid):")
validate_number([10, 3, 30], 5)
print()

# Q8: Module Execution Boundary
print("=" * 20)
print("Q8: Module Execution Boundary")
print("=" * 20)


def business_logic_function():

    return "Business logic executed successfully"


def utility_function(data):
    return f"Processed: {data}"



if __name__ == "__main__":
    print("This module is being run directly (not imported)")
    print(f"Business logic result: {business_logic_function()}")
    print(f"Utility result: {utility_function('test data')}")
    print()
    print("Note: If this module were imported, the code above")
    print("      (inside if __name__ == '__main__') would not execute.")
    print()

print("=" * 20)
print("Q9: Cross-Cutting Concerns via Decorators")
print("=" * 20)


def timing_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMING] {func.__name__} took {end - start:.4f} seconds")
        return result

    return wrapper


def permission_check(required_permission):

    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if hasattr(self, 'permissions') and required_permission in self.permissions:
                return func(self, *args, **kwargs)
            else:
                return f"Access denied: '{required_permission}' permission required"

        return wrapper

    return decorator


class Document:

    def __init__(self, title, permissions=None):
        self.title = title
        self.permissions = permissions or []

    @timing_decorator
    def process_document(self):
        """Method with timing decorator."""
        time.sleep(0.1)  # Simulate processing
        return f"Document '{self.title}' processed"

    @permission_check("read")
    def read(self):
        """Method with permission check."""
        return f"Reading document: {self.title}"

    @permission_check("write")
    def write(self):
        """Method with permission check."""
        return f"Writing to document: {self.title}"


doc1 = Document("Report.pdf", permissions=["read"])
doc2 = Document("Secret.txt", permissions=["read", "write"])

print("Timing decorator:")
doc1.process_document()
print()

print("Permission decorator:")
print(f"doc1.read(): {doc1.read()}")
print(f"doc1.write(): {doc1.write()}")
print(f"doc2.write(): {doc2.write()}")
print()

# Q10: System-Level Integration
print("=" * 20)
print("Q10: System-Level Integration - Combining All Components")
print("=" * 20)


class IntegratedSystem:


    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.activities = []

    @timing_decorator
    def process_activities(self, activity_list):
        for activity in self._activity_generator(activity_list):
            self.activities.append(activity)
        return f"Processed {len(activity_list)} activities"

    def _activity_generator(self, activities):
        for activity in activities:
            yield f"Activity: {activity}"

    def __str__(self):
        return f"System User: {self.name} ({self.email})"

    def __repr__(self):
        return f"IntegratedSystem(user_id='{self.user_id}', name='{self.name}')"

    def __len__(self):
        return len(self.activities)

    def __eq__(self, other):
        if not isinstance(other, IntegratedSystem):
            return False
        return self.user_id == other.user_id

    def __call__(self, action):
        return f"System executing action: {action}"


print("Creating integrated system instance:")
system = IntegratedSystem("SYS001", "System Admin", "sys@example.com")

print(f"__str__: {str(system)}")
print(f"__repr__: {repr(system)}")
print(f"Initial __len__: {len(system)}")
print()

print("Processing activities (with timing decorator):")
activities = ["login", "view_data", "generate_report", "logout"]
system.process_activities(activities)
print()

print(f"After processing, __len__: {len(system)}")
print(f"__call__: {system('backup')}")
print()

print("Comparing systems:")
system2 = IntegratedSystem("SYS001", "Different Name", "different@example.com")
system3 = IntegratedSystem("SYS002", "Another", "another@example.com")
print(f"system == system2 (same ID): {system == system2}")
print(f"system == system3 (different ID): {system == system3}")
print()

