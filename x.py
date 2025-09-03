class Bank:
    account_balance = 0.0
    def __init__(self, deposit, withdraw, balance=0):
        self._balance = balance
        self._deposit = deposit
        self._withdraw = withdraw

    def balance(self):
        return self._balance

    def deposit(self, new_amount):
        if new_amount <0:
            raise ValueError("You can't deposit amount less than Zero!")
        else:
            print(f"You have successfully deposited ${new_amount}")
            self._deposit = new_amount
            self._balance+= new_amount
            return new_amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("You can't withdrawn negative amount")
        elif amount > self._balance:
            raise ValueError("Insufficient funds!")
        else:
            print(f"You have successfully withdrawn ${amount}")
            self._withdraw = amount
            self._balance-= amount
            return amount


customer = Bank(0, 0, 0)

customer2 = customer.deposit(300)
print(f"your new balance is {customer.balance()} ")
customer3 = customer.withdraw(90)
print(f"your new balance is {customer.balance()} ")
