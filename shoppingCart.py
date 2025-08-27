#ask the user input to select the food
#if user input selected a food not in the menu[fruits] then give them a chance to select another one
#ask the user the price
#add all the total prices to give the total amount price of foods bought
#ask the user input if he/she is done with shopping, if yes , then(Q) to exit else continue loop through the same input
#use the file handling methods like file.write and file read to show past or save history of all the orders the user makes
#try using error handling methods like try and exceptions to handles all the errors
#thanks the user afterward and remind them to have a good day, happy coding


def shopping():
    def history(order):
        try:
            with open("orders.txt", "r") as file:
                print("Your past orders \n")
                file.read(order)
        except FileNotFoundError:
            print("You have no past orders history yet!")


    print("----------------food menu---------------------")
    food = ("orange", "banana", "cherry", "mango", "pineapple")
    food_selected=set()

    for x in food:
        print(x,end="| ")
    print("\n-----------------------------------------------")
    print(sep=" ")
    def main():
        total_amount=0

        while True:
            order = input("Type 'history' to view your pass orders \n"
                          "(Q) to quit or Enter your order: ").strip()


            if order.lower()=="q":
                break
            else:
                if order == 'history':
                    history(order)
                    continue
                elif order not in food:
                    print(f"{order} is unavailable in the menu")
                    print("Please select a another one!")
                elif order in food:
                    try:
                        price = int(input(f"What is the price of {order}:"))
                        total_amount += price
                        with open("price.txt", "a" and "w") as file:
                            file.write(order)
                    except ValueError:
                        print("Please, enter the price in digits or numbers!")
                        continue

                if order in food:
                    food_selected.add(order)

        print(sep=" ")
        print("-------------your order-------------------")
        print(food_selected)
        print(f"Your total is ${round(total_amount,2)}")
        print("Thanks, Have a nice day")

    if __name__=="__main__":
        main()
shopping()



