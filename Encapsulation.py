# Encapsulation - Cannot access by the object

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