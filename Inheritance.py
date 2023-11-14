# Inheritance
# Reuse of the methods and attributes from another class in the current class
# The relation of the two classes is the parent-child class

class calculator:
    def add(self, a, b):
        self.sum = a + b
        return self.sum
    def mul(self, a, b):
        self.mult = a * b 
        return self.mult 

class rectangle(calculator):
    def perimeter(self, a, b):
        print(self.add(a, b))
    def area(self, a, b):
        print(self.mul(2, self.mul(a,b)))   
         
obj = rectangle()
print(obj.sum)
obj.perimeter(10,20)
obj.area(10, 20)

