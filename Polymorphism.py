# Polymorphism 

# Overloading and Overridding

class calculator:
    def add(self, a, b = 10):
        return a + b

class calci(calculator):
    def add(self, a, b, c = 20):
        return a + b + c    

obj = calculator()
print(obj.add(10))
print(obj.add(10, 20))

obj1 = calci()
print(obj1.add(1, 2))