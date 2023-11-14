# Encapsulation - Hide some variables and methods from outside the class by making it private, 
# in python making private by, use double underscore infront of the variable or method name
# even the object cannot access directly but can access through the public method or protector
# It can access only inside the class

class BankAccount:
    def __init__(self):
        self.__accountnumber = 12345678

    def balanceM(self):    
        self.__balance = 500
        return self.__balance
    
    def getAcc(self):    
        return self.__accountnumber


obj = BankAccount()
print(obj.getAcc())
print(obj.balanceM())