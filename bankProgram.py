#make s simple bank program
# there should be balance, withdraw and deposit then later to quit if user feels so
#use file handling methods like file.write and file.read to save or show the user the bank history/past records
#use error handling methods like try and except.
#if user input wants to check balance. print the account balance
#if user input wants to deposit, ask how much money user wants to deposit
#elif  user input wants to withdraw, ask how  much money user  wants to withdraw
#else user wants to quit, give the user a number to input then break or quit/stop the problem
#thanks the user afterward



def bank():
    def balance(account_balance):
        print(f"Dear Customer, You have a balance of ${account_balance}")


    def deposit(account_balance):
        depositing= int(input("how much money are you depositing?:"))
        if depositing <0:
            print("You can't deposit less money than your bank account")
        else:
            print(f"You have successfully deposited ${depositing:.2f} ")
            file = open("depositing.txt", "w")
            file.write(f"you have deposited ${round(depositing,2)} to your account. \n ")
            return depositing


    def withdraw(account_balance):
        withdrawing = int(input("How much money are you withdrawing?: "))
        if withdrawing < 0:
            print("You can't withdraw amount less than Zero!")
            return 0
        elif withdrawing > account_balance:
            print("Insufficient Funds! ")
            return 0
        else:
            print(f"You have successfully withdrawn ${withdrawing:.2f} ")
            file = open("withdrawing.txt", "w")
            file.write(f"You have withdrawn -${round(withdrawing,2)} from your account. \n")
            return withdrawing


    def bank_history(account_balance):
        try:
            with open("depositing.txt", "r")  as file:
                print(sep=" ")
                print("-------Your Bank history record-----------", )
                print(end=file.read())
            with open("withdrawing.txt", "r") as file:
                print(file.read().rstrip())
                print("------------------------------------------")

        except FileNotFoundError:
            print("You have no bank history yet!")
            return account_balance


    def main():
        print("-----------CHIENGTECT BANK----------- ")
        print(sep="")
        print("1. Check balance")
        print("2. Deposit money ")
        print("3. Withdrawn money")
        print("4. bank history")
        print("5. Quit")
        print("-------------------------------------")

        account_balance =0
        while True:
            customer = input("select any of your choice: ")
            if customer =="1":
                 balance(account_balance)
            elif customer =="2":
                account_balance+=deposit(account_balance)
            elif customer =="3":
                account_balance-= withdraw(account_balance)
            elif customer =="4":
                bank_history(account_balance)
            elif customer =="5":
                break

        print("-------------------------------------")
        print("Thanks Customer, Have a nice day")

    if __name__=="__main__":
        main()
bank()
