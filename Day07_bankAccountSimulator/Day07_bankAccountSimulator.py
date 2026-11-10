# Bank Account Simulator

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
         self.account_holder = account_holder
         self.balance = initial_balance
         
    # Deposit Money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}.")
        else:
            print("Invalid Deposited amount. amount must be positive.")
            
    # Withdraw Money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal failed.")
        elif amount <= 0:
            print("Invalid withdrawal amount. Amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}.")
    
    # Show Account Details
    def show_account_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance}")
        
# Main Program
accounts= {}

def create_account():
    name = input("Enter account holder's name: ").strip()
    initial_deposit = float(input("Enter initial deposit amount: "))
    accounts[name] = BankAccount(name, initial_deposit)
    print(f"Account created for {name} with balance ${initial_deposit}.")
  
def access_account():
    name = input("Enter account holder's name: ").strip()
    if name in accounts:
        account = accounts[name]
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Show Account Details")
            print("4. Exit")
            choice = input("Choose an option: ").strip()
            
            if choice == '1':
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            elif choice == '3':
                account.show_account_details()
            elif choice == '4':
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Account not found. Please create an account first.")  
        
while True:    
    print("\n--- Bank Account Simulator ---")
    print("1. Create Account")
    print("2. Access Account")
    print("3. Exit")
    user_choice = input("Choose an option: ").strip()   
    if user_choice == '1':
        create_account()
    elif user_choice == '2':
        access_account()
    elif user_choice == '3':
        print("Thank you for using the Bank Account Simulator. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")