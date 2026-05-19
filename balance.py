import math

Username = input("Enter your User Name: ")
Openingbalance = int(input("Enter your Opening Balance: "))
OB = "Openingbalance"
print(Openingbalance)
Transactions = int(input("Enter number of Transactions: "))
for i in range(0, Transactions):
 type = input("Enter transaction type (credit/debit): ")
 amount = int(input("Enter amount: "))
if type == "credit":
    Openingbalance =  Openingbalance + amount
elif type == "debit":
    Openingbalance = Openingbalance - amount
print("Current balance:", Openingbalance)