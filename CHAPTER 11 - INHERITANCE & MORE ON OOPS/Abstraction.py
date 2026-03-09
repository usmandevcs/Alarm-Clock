# ABSTRACTION - “Sirf button dikhao, engine nahi”

# Abstraction ka matlab:
'''
User ko sirf simple buttons dikhao, andar ka complex 
system hide karo.

Real life analogy:
TV remote
Tum sirf power button dabate ho
Andar circuit kaise chalta hai → nahi dekhte.
'''
# Python me abstraction kaise hota hai?
'''
Python me abstraction ke liye hum abstract classes aur
abstract methods ka use karte hain.
Abstract class: Ek aisi class jo khud se object nahi bana 
sakti,lekin dusri classes ke liye blueprint ka kaam karti 
hai.
Abstract method: Ek aisi method jo abstract class me 
declare hoti hai,lekin uska implementation nahi hota. 
Subclasses ko is method ko implement karna padta hai.
'''
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass  # Abstract method, implementation subclasses me hoga
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started.")
# Usage
car = Car()
bike = Bike()
car.start_engine()  # Output: Car engine started.
bike.start_engine()  # Output: Bike engine started.
# Abstraction ke benefits:
'''
1. Code Reusability: Common functionality ko abstract class me define
karke reuse kar sakte hain.
2. Code Maintainability: Complex implementation ko hide karke code
ko modular banata hai, jisse maintain karna easy hota hai.
3. Flexibility: Internal implementation ko change kar sakte hain bina
external code ko affect kiye.
'''