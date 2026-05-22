# Menu Driven
# Continuous Loop
import json
import os

def main_menu():
    filename = input("Enter a filename to store your transactions : ")
    closing_balance = reader(f"{filename}.jsonl")
    while True:
        try:
            options = "\n1.Debit\n2.Credit\n3.View\n4.Exit\n"
            menu_input = int(input(f"What would you wish to do?{options}"))
            if menu_input == 4:
                print("Adios~!")
                exit()
            elif menu_input == 3:
                print(f"Closing Balance = {closing_balance}\n")
                continue
            elif menu_input == 1:
                amount = float(input("Enter Debit Amount: "))
                closing_balance = closing_balance - amount
                data_saver(filename, "debit", amount, closing_balance)
            elif menu_input == 2:
                amount = float(input("Enter Credit Amount: "))
                closing_balance = closing_balance + amount
                data_saver(filename, "credit", amount, closing_balance)
            else:    
                print(f"Wrong OPTIONS MATE!\nLet's try that again{options}")
        except ValueError: 
            print(f"Wrong OPTIONS MATE!\nLet's try that again{options}")
            
def data_saver(filename, transaction_type, amount, closing_balance):
    data = {
        'transaction type' : transaction_type,
        'amount' : amount,
        'closing_balance' : closing_balance
    }

    with open(f"{filename}.jsonl", "a") as f:
        f.write(json.dumps(data) + "\n") 
    reader(f"{filename}.jsonl")
        
def reader(filename):
    if not os.path.exists(filename):
        default_data = {
            'transaction type' : "none",
            'amount' : 0.0,
            'closing_balance' : 0.0
        }
        with open(filename, "w") as f:
            f.write(json.dumps(default_data) + "\n")
        return 0.0
    else:
        with open(filename, "r") as f:
            lines = f.readlines()
        
        if lines:
            last_line_data = json.loads(lines[-1].strip())
            return float(last_line_data['closing_balance'])
        return 0.0
        
if __name__ == "__main__":
    main_menu()