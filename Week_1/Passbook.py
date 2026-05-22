# All the bank calculations will from now on be done here as the main program. 
def filewriter(Username,Age) :
    with open("Account.txt", "a") as f:
        f.write(f"{Username}, {Age} \n")
    with open("Account.txt") as f:
        print(f.read())
    
def AccountCreation():
    Username = input("Enter your User Name: ")
    Age = int(input("Enter your Age: "))
    if Age <= 16 :
        print("Not eligible : You should be older than 16 years to create account ")
    elif Age > 16 :
        print("Congratulations you are eligible to create account")
        NewAccount = input(" Would you like to create account(Yes/No): ")
        if NewAccount.lower() == "yes":
            filewriter(Username, Age)
AccountCreation()



