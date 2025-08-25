#make s simple bank program
#let there be balance, withdraw and deposit then maybe quit
#if user input wants to check balance. print the account balance
#if user input wants to deposit, ask how much money user wants to deposit
#else if user input wants to withdraw, ask how  much user  wants to withdraw
#else user wants to quit, give the user a number to input then break or quit/stop the problem
#thanks the user afterward


def bank():
    print("         ChiengTech Bank")
    print("----------------------------------------------")

    def balance(account_balance):
        print(f"your account balance is ${account_balance:.2f}")

    def deposit():
        depositing= int(input("How much money are you depositing?:"))
        print(f"You have deposited ${depositing}")


    def withdrawn(account_balance):
        withdrawing = int(input("How much money are you withdrawing?:"))
        if withdrawing < 0:
            print("You can't withdraw money less than you bank account")
            return 0
        elif withdrawing > account_balance:
            print("insufficient funds.")
            return 0
        else:
            withdrawing -= account_balance
            print(f"you have withdraw ${withdrawing:.2f} successfully!")
            return withdrawing

    print("Hello, welcome!")
    print("1. Check balance")
    print("2. deposit money")
    print("3. withdrawn money")
    print("4. quit")
    print("----------------------------------------------")

    def main():
        account_balance = 500
        is_running = True

        while is_running:
            num = input("please select any (1-4):")
            if num == "1":
                balance(account_balance)
            elif num =="2":
                account_balance+=deposit()
            elif num =="3":
                withdrawn(withdrawn(account_balance))
            elif num=="4":
                is_running = False

    if __name__ =="__main__":
        main()


        print("Thanks, Have a nice day!")






bank()
