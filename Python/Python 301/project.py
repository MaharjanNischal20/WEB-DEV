class Bank:
    def __init__(self,initial_amount = 0.00):
        self.balance = initial_amount

    def log_transcation(self,transaction_string):
        with open("transactions.txt",'a') as file:
            file.write(f"{transaction_string}\t\t\t Balance: ${self.balance}\n")

    def withdraw(self,amount):
        try:
            amount = float(amount)
            
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance - amount
            self.log_transcation(f"Withdrew ${amount}")
            
        
    def deposit(self,amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.log_transcation(f"Deposited ${amount}")

account =Bank(50)
while(True):
    try:
        action = input("What kind of action do you want?")
        action.lower()
    except KeyboardInterrupt:
        print("Leaving the ATM\n")
        break;
    if action in ['withdraw','deposit']:
        if action =="withdraw":
            amount = input("How much do want to take out??")
            account.withdraw(amount)
        
        else:
            amount = input("How much do want to put in??")
            account.withdraw(amount)

        print("Your balance is ",account.balance)

    else:
        print("This is not a valid action, Try again.")
