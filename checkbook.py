import os # operating system



print("~~~ Welcome to your terminal checkbook! ~~~")


# read the balance from  file if it exists

if os.path.exists("balance.txt"):
    with open("balance.txt","r") as f:
        balance=f.read()
else:
    balance=0
            
balance = float(balance)           
# Function to display the current balance
def view_balance(bal):
    print(f"your current balance is ${bal:.2f}")
    
    

# Function to record a withdraw 
def record_withdraw(bal):
    try:
        withdraw_amount = float(input("How much is the debit? $"))
        if withdraw_amount > bal:
            print("Insufficient funds.")
        else:
            bal -= withdraw_amount
            print(f"${withdraw_amount:.2f} debited from your account.")
        return bal
    except:
        print("Invalid input. Please enter a valid amount.")
        return bal



# Function to record a deposit
def record_deposit(bal):
    try:
        deposit_amount = float(input("How much is the credit? $"))
        if deposit_amount < 0:
            print("Invalid input. Credit amount cannot be negative.")
        else:
            bal += deposit_amount
            print(f"${deposit_amount:.2f} credited to your account.")
        return bal
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        return bal

# Functin to save_balance
def save_balance(bal):
    with open('balance.txt','w') as f:
     
        f.write(str(bal))







while True:
        # print the choices
        print("\nWhat would you like to do?\n")
        print("1) view current balance")
        print("2) record a debit (withdraw)")
        print("3) record a credit (deposit)")
        print("4) exit")

        choice = input("\nYour choice? ")

        if choice == "1":
            view_balance(balance)
        elif choice == "2":
            balance = record_withdraw(balance)
        elif choice == "3":
            balance = record_deposit(balance)
        elif choice == "4":
            save_balance(balance)
            print("Thanks, have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
