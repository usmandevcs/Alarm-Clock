# Banking Program:
import random 
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance: .2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self._balance: .2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: ${self._balance: .2f}")

is_running = True
while is_running:
    print("\nWelcome to the Banking Program!")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Balance")
    print("5. Exit")

    choice = input("Please select an option (1-5): ")

    if choice == '1':
        name = input("Enter your name: ")
        cnic = int(input("Enter your CNIC: "))
        account_number = random.randint(100000000, 999999999)
        account = BankAccount(account_number, name, balance = 0)
        print("Account created successfully.")
        print(f"Account Number: {account.account_number}, Account Holder: {account.account_holder}, CNIC: {cnic}, Balance: ${account._balance: .2f}")
    elif choice == '2':
        if 'account' in locals():  # local variable check to ensure account exists
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        else:
            print("No account found. Please create an account first.")
    elif choice == '3':
        if 'account' in locals():
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        else:
            print("No account found. Please create an account first.")
    elif choice == '4':
        if 'account' in locals():
            account.display_balance()
        else:
            print("No account found. Please create an account first.")
    elif choice == '5':
        is_running = False
        print("Thank you for using the Banking Program. Goodbye!")
    else:
        print("Invalid option. Please try again.")

# Example usage:
if __name__ == "__main__":
    # Create a bank account
    account = BankAccount()

