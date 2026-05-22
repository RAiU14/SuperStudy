# Menu Driven Account Balance Calculator. Without Database.
# Input: Name, Opening Balance, Transaction Count, Transactions
# Display: Closing Balance
# Menu should have option to add more transaction to credit and debit into the account as well as an exit function also.

# function to take input from user on their choice
def abc():

    while True:
        userchoice = input('''\nEnter your choice, select corresponding number: 
    1. Check Balance
    2. Credit transaction
    3. Debit transaction
    4. Exit
    Choice: ''')

        if userchoice == "1":
            current_balance(0)
        elif userchoice == "2":
            current_balance(input("Enter number to credit to balance: "))
        elif userchoice == "3":
            current_balance(-int(input("Enter number to debit from balance: ")))
        elif userchoice == "4":
            print("Nikal..peheli phursath mai nikal")
            exit()
        else: 
            print("Glath choice hai chammooo")

# function to calculate balance amount           
balance = 0
def current_balance(amount):
    global balance
    balance += int(amount)
    print("Tera ghar bikh jayenga isme : ", balance)
    
abc()