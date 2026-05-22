name = input("Enter your name : ")
balance = int(input("Enter your balance : "))

print("Hi", name)
print("your current balance is : ",balance)

while True:
    
    print("------MENU---------\n""Option 1 - Credit\n""Option 2 - Debit\n""Option 3 - Balance\n""Option 4 - exit")

    choice = int(input("Enter your choice 1 - 4 : "))

    if choice == 1:
        amount = int(input ("Enter amount to credit : "))
        balance = balance + amount
        print ("Amount credited successfully. Total balance is: ", balance)

    elif choice == 2:
        amount = int(input ("Enter amount to debit : "))
        if amount > balance:
            print ("Insufficient balance")

        else :
            balance = balance - amount
            print ("amount debited successfully. Total balance is", balance)

    elif choice == 3:
            print ("current balance is ", balance)

    elif choice == 4:
            print("THANK YOU")
            break

    else:
         print("Invalid, try again")
