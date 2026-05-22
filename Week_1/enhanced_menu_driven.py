# Menu Driven
# Continous Loop

def main_menu():
    closing_balance = 0
    while True:
        try:
            options = "\n1.Debit\n2.Credit\n3.View\n4.Exit\n"
            menu_input = int(input(f"What would you wish to do?{options}"))
            if menu_input == 4:
                print("Adios~!")
                exit()
            elif menu_input == 3:
                print(f"Closing Balance = {closing_balance}\n")
            elif menu_input == 1:
                closing_balance = closing_balance - float(input("Enter Debit Amount: "))
            elif menu_input == 2:
                closing_balance = closing_balance + float(input("Enter Credit Amount: "))
            else:    
                print(f"Wrong OPTIONS MATE!\nLet's try that again{options}")
        except ValueError: 
            print(f"Wrong OPTIONS MATE!\nLet's try that again{options}")

if __name__ == "__main__":
    main_menu()
    