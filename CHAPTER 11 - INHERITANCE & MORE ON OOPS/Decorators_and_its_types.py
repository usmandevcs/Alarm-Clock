# DECORATOR - “Gift wrapping function”
'''
Decorator ek wrapper hota hai jo function ko bina change 
kiye uska behavior modify karta hai.

Real life analogy:
Tumne simple gift diya
Kisi ne usko wrap kar diya ribbon se
Gift same, look better.
'''
'''
in simple words, decorator ek function hai jo dusre function 
ko as an argument leta hai aur usko modify karke return 
karta hai. Iska use hum logging, timing, access control, etc. 
ke liye karte hain.
'''
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
@decorator
def say_hello():
    print("Hello!")
# Usage
say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
# Benefits of Decorators:
'''
1. Code Reusability: Common functionality ko decorator me 
define karke reuse kar sakte hain.
2. Separation of Concerns: Core functionality ko separate 
rakhte hain, aur additional behavior ko decorators me 
handle karte hain.
3. Flexibility: Existing code ko modify kiye bina naye 
behavior add kar sakte hain.
4. Readability: Code ko cleaner aur more readable banata hai,
kya ho raha hai easily samajh aata hai.
5. Built-in Decorators: Python me kuch built-in decorators
hote hain jaise @staticmethod, @classmethod, @property, etc.
6. Third-party Libraries: Python me kai third-party libraries
hote hain jo powerful decorators provide karte hain, jaise
Flask me route decorators, Django me model decorators, etc.
'''

# Decorator with arguments
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):  # args = positional arguments, kwargs = keyword arguments
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator
@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")
# Usage
greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!

# Timer example:
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper
@timer
def compute_square(n):
    return n * n
# Usage
print(compute_square(10))
# Output:
# Execution time: 0.0001 seconds (example)
# Logging example:
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is called with arguments: {args} and keyword arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper
@logger
def add(a, b):
    return a + b
# Usage
print(add(5, 3))
# Output:
# Function 'add' is called with arguments: (5, 3) and keyword arguments: {}
# 8

# GETTER and SETTER - “Safe gate”
'''
Encapsulation me direct variable access nahi karte
Getter → value read
Setter → value update with rules
'''
class Person:
    def __init__(self, name):
        self._name = name  # Protected variable
    @property
    def name(self):
        return self._name  # Getter method
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip():
            self._name = value  # Setter method with validation
        else:
            raise ValueError("Name must be a non-empty string.")
# Usage
person = Person("Alice")
print(person.name)  # Output: Alice
person.name = "Bob"  # Update name using setter
print(person.name)  # Output: Bob
# person.name = ""  # This will raise ValueError due to validation in setter

# STATIC METHOD - “Class ka helper tool”

# Object data use nahi karta.
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def multiply(a, b):
        return a * b
# Usage
print(MathUtils.add(5, 3))  # Output: 8
print(MathUtils.multiply(5, 3))  # Output: 15

# CLASS METHOD - “Class level ka kaam”

# Class variable modify karta.

class Counter:
    count = 0  # Class variable
    @classmethod
    def increment(cls):
        cls.count += 1  # Modify class variable
        return cls.count
# Usage
print(Counter.increment())  # Output: 1
print(Counter.increment())  # Output: 2


# SUMMARY - Baby Brain Model
'''
Encapsulation → secret locker
Abstraction → simple buttons
Decorator → function ka wrapper gift
Getter/Setter → safe gate
Property → smart gate
Static method → tool box
Class method → class ka counter

System thinking:
Encapsulation = safety
Abstraction = simplicity
Decorator = behavior control
Methods types = responsibility separation.
'''