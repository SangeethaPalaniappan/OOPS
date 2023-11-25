import random
import sys
'''print("\n")
arr = [["Name \t\t",  "Pin\t", "Place\t\t", "Balance"], 
       ["Sangeetha\t", "7478 \t", "Pudukkottai \t", "Indian Bank"],
       ["Ganesh\t\t", "9278 \t", "Pudukkottai \t", "Indian Bank"],
       ["Sam\t\t", "1274 \t", "Pudukkottai \t", "Indian Bank"],
       ["Geetha\t\t", "9763 \t", "Pudukkottai \t", "Indian Bank"]
       ]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end = " ") 

    print("\n")           
'''
print("\n")
print("---------- \t Welcome to Indian Bank\t -----------")
print("\t     *** Mirattunilai Branch *** \t\t")
class ATM:
    branch_name = "Mirattunilai"
    bank_name = "Indian Bank"
    Balance = 100000
    __pin = 7890
    def check_Balance(self):
        print("ATM_current_balance: ", self.Balance)
        print("\n")

    def deposit(self, amount):
        Pin = int(input("Pin : "))
        if self.__pin == Pin:
            self.Balance += amount
            print("\n")
        else:
            print("You don't have the access")    

    def atm_detail(self):
        print("Branch_Name  : ", self.branch_name)
        print("Bank_name    : ", self.bank_name)
        print("Balance      : ", self.Balance)
        print("\n")

    def transaction(self):
        print(self.Balance)
        Pin = int(input("Pin : "))
        if self.__pin == Pin:
            if self.Balance != 0:
                while True:    
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Atm_details")
                    print("4. Exit")
            

                    try:
                        option = int(input("Choose the option: "))
                        print("\n")
                    except Exception:
                        print("Error, enter 1, 2, 3, 4 - any one of these numbers")
                        continue
                    if option == 1:
                        self.check_Balance()

                    elif option == 2:
                        amount = int(input("Enter the amount : "))
                        self.deposit(amount)

                    elif option == 3:
                        self.atm_detail()

                    elif option == 4:             
                        print("Thank You! Visit Again!")   
                        sys.exit()
                    
                      
            
            else:
                print('''
                    Not enough money in ATM
                    Can't take Money
                    Load cash
                    Minimum 100000 ''')
                for i in range(50):
                    try:
                        amount = int(input("Enter amount : "))
                        if amount < 100000:
                            print("Enter minimum 100000")
                            continue

                        else:    
                            break
                    except Exception:
                        print("Please enter the cash in numbers")    
                self.Balance += amount    
        else:
            print("You don't have the access")            
                    




class user(ATM):
    
    def __init__(self, name, acc_no, pin):
        self.name = name
        self.acc_no = acc_no
        self.pin = pin
        self.balance = 0
        


    def account_detail(self):
        print("Account_holder : ", self.name)
        print("Account_number : ", self.acc_no)
        print("Account_balance: ", self.balance)
        print("\n")

    def check_balance(self):
        print("Account_current_balance: ", self.balance)
        print("\n")

    def Deposit(self, amount):
        for i in range(3):
            Pin = int(input("Enter your pin : "))
            if self.pin == Pin:
                self.balance += amount
                self.Balance += amount
                print("Transaction Id: ", random.randint(100000000,1000000000))
                print("\n")
                break
            else:
                print("Enter Correct Pin")    
                att = 2 - i
                print(att, "more attempts")
                if att == 0:
                    sys.exit()

    def Withdraw(self, amount):
        for i in range(3):
            Pin = int(input("Enter your pin : "))
            
            if self.pin == Pin:
                if amount > self.balance:
                    print("Not enough money in your account\n")
                    break
                else:
                    self.balance -= amount
                    self.Balance -= amount
                    print("Transaction Id: ", random.randint(100000000,1000000000))
                    print("\n")
                    break
            else:
                print("Enter Correct Pin")    
                att = 2 - i
                print(att, "more attempts")
                if att == 0:
                    sys.exit()


        

    def transactions(self):
        
        while True:    
            if self.Balance != 0:    
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Account Detail")
                print("5.Exit")

                try:
                    option = int(input("Choose the option: "))
                    print("\n")
                except Exception:
                    print("Error, enter 1, 2, 3, 4, 5 - any one of these numbers")
                    continue
                if option == 1:
                    self.check_balance()

                elif option == 2:
                    
                    for i in range(3):
                        amount = int(input("Enter the amount : "))
                        if amount >= 1000 and amount <= 10000:
                            self.Deposit(amount)
                            break
                        else:
                            print("You can deposit only from 1000 to 10000")
                            att = 2 - i
                            print(att, "more attempts")
                            if att == 0:
                                sys.exit()

                    

                elif option == 3:
                    for i in range(3):
                        amount = int(input("Enter the amount : "))
                        if amount >= 1000 and amount <= 10000:
                            self.Withdraw(amount)
                            break
                        else:
                            print("You can withdraw only from 1000 to 10000")
                            att = 2 - i
                            print(att, "more attempts")
                            if att == 0:
                                sys.exit()
                    
                    

                elif option == 4:
                    self.account_detail()

                elif option == 5:             
                      
                    print(self.transaction())
                    print("Thank You! Visit Again!") 
                    sys.exit()
                    
            else:

                self.transaction()

            
                    
def further_steps():
    option = input("Do you want to do transaction? (Yes/No) ")
    while True:
        if option == "Yes":
            S.transactions()
        else:
            print("Thank You! Visit Again")   
            break 

Sum = ATM()
print("ATM Balance: ", Sum.Balance)


Name = input()

while True:
    Acc_No = int(input("Enter 10 digits number : "))
    if Acc_No in range(1000000000, 10000000000):
        break
    else: 
        print("Enter valid 10 digits number ")


while True:
    Pin = int(input("Enter 4 digits number : "))
    if Pin in range(1000, 10000):
        break
    else: 
        print("Enter valid 4 digits number")
        
S = user(Name, Acc_No, Pin)  
further_steps()


























'''class atm:
    def __init__(self, name, acc_no, pin):
        self.name = name
        self.acc_no = acc_no
        self.pin = pin
        self.balance = 0
        

    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        print("\n")

    def account_detail(self):
        print("Account_holder : ", self.name)
        print("Account_number : ", self.acc_no)
        print("Account_balance: ", self.balance)
        print("\n")

    def check_balance(self):
        print("Account_current_balance: ", self.balance)
        print("\n")

    def deposit(self, amount):
        self.balance += amount
        print("\n")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money in your account\n")
        else:
            self.balance -= amount
            print("\n")

    def transactions(self):
        while True:    
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Account Detail")
            print("5.Exit")

            try:
                option = int(input("Choose the option: "))
                print("\n")
            except Exception:
                print("Error, enter 1, 2, 3, 4, 5 - any one of these numbers")
                continue
            if option == 1:
                self.check_balance()

            elif option == 2:
                amount = int(input("Enter the amount : "))
                self.deposit(amount)

            elif option == 3:
                amount = int(input("Enter the amount : "))
                self.withdraw(amount)

            elif option == 4:
                self.account_detail()

            elif option == 5:             
                print("Thank You! Visit Again!")   
                break
    
            
                    


def further_steps(option):
    while True:
        if option == "Yes":
            S.transactions()
        else:
            print("Thank You! Visit Again")   
            break 


Name = input()
Acc_No = int(input())
Pin = int(input())
S = atm(Name, Acc_No, Pin)  
option = input("option(Yes / No): ")
further_steps(option)


Name = input()
Acc_No = int(input())
Pin = int(input())
D = atm(Name, Acc_No, Pin)  
option = input("option(Yes / No): ")
further_steps(option)
'''