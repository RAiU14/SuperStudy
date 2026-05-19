## Menu Driven Account Balance Calculator. Without Database. 
# Input: Name, Opening Balance, Transaction Count, Transactions
# Display: Closing Balance
# Menu should have option to add more transaction to credit and debit into the account as well as an exit function also. 
amount = []
while True:
    try:
        starting_acc = input("Welcome to Study Bank\n1.Register User\n2.Exit\n")
        if int(starting_acc) == 1:
            name = input("What's your name?\n")
            throw_var = input("I'm sorry. For security purposes. Enter it again. What is your name?\n")
            while name.lower() != throw_var.lower():
                print("Well, you didn't get that right for sure\nAnyways....retry\n")
                name = input("What's your name?\n")
                throw_var = input("I'm sorry. For security purposes. Enter it again. What is your name?\n")
            print(f"I'm just kidding, I know your name is {name}\n")

            age = int(input("What's your age? "))
            if age < 18: 
                print("This app is not for kids!!!")
                break
            else:
                n = 0 
                opening_bal = float(input("What's your opening balance? "))
            
            closing_balance = opening_bal
            
            while True:
                doc = int(input("What would you wish to do ?\n1.Debit\n2.Credit\n3.View\n4.Exit\n"))
                if doc == 4:
                    exit()
                elif doc == 3:
                    print(f"Closing Balance = {closing_balance}\n")
                elif doc == 1:
                    debit = float(input("Enter Debit Amount: "))
                    closing_balance = closing_balance - debit
                elif doc == 2:
                    credit = float(input("Enter Credit Amount: "))
                    closing_balance = closing_balance + credit
                else:    
                    print("Wrong OPTIONS MATE!\nLet's try that again\n1.Debit\n2.Credit\n3.View\n4.Exit\n")
                            
        elif int(starting_acc) == 2:
            break
        else:
            print("Wrong OPTIONS MATE!\nLet's try that again\n1.Register User\n2.Exit\n")
                    
    except ValueError:
                    print("Oops! Wrong input. ")