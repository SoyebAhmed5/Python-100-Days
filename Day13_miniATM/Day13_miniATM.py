# Mini ATM MAchine

class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.__pin = pin
        self.__balance = balance
        
    # Validate PIN
    def validate_pin(self, pin):
        return self.__pin == pin
    
    # Deposit Money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw Money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient balance or invalid amount.")
    
    # Check Balance
    def check_balance(self):
        return self.__balance
    
    # Change PIN
    def change_pin(self, old_pin, new_pin):
        if self.validate_pin(old_pin):
            self.__pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Invalid old PIN.")
            
    # Display Account Details
    def display_account_details(self):
        print("\n--- Account Details ---")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.__balance}")
        
    def get_account_number(self):
        return self.account_number
    
    def create_account(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.__pin = pin
        self.__balance = balance
        print(f"Account {account_number} created successfully with balance ${balance}.")
        
    def delete_account(self):
        print(f"Account {self.account_number} deleted successfully.")
        self.account_number = None
        self.__pin = None
        self.__balance = 0
        
    def  account_menu(self):
        while True:
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Change PIN")
            print("5. Display Account Details")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                print(f"Current Balance: ${self.check_balance()}")
            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            elif choice == '4':
                old_pin = input("Enter old PIN: ")
                new_pin = input("Enter new PIN: ")
                self.change_pin(old_pin, new_pin)
            elif choice == '5':
                self.display_account_details()
            elif choice == '6':
                print("Exiting ATM. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")