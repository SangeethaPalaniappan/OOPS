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