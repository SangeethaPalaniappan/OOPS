# object is the only way to interact with class

# Class - template or blueprint
# Which contains methods and attributes
# Class does not occupy any memory

class calculator:
    def add(self, a, b):
        self.sum = a + b
        print(self.sum)
    def mul(self, a, b):
        self.mult = a * b 
        print(self.mult)   

# Object - instance(example) of a object
# Memory representation of a class

cal = calculator()
calculator.add(cal, 10, 20)
calculator.mul(cal, 10, 20)