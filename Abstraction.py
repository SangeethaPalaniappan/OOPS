# Import package 
# If the child class has different implementations, Not same as the parent, at this time there is no use in implementing the parent class. This is abstraction
# No implementation in parent class, but implementation for all the methods in the child class, if any of the method missed, then the child class also a abstract class 

from abc import ABC, abstractclassmethod

class animal(ABC):
    @abstractclassmethod
    def sound(self):
        pass
class Dog(animal):
    def sound(self):
        print("Barks")   
class Cat(animal):
    def sound(self):
        print("Meow")

obj = Dog()
obj.sound()
obj1 = Cat()        
obj1.sound()