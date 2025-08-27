#ask the user input to select the food
#if user input selected a food not in the menu[fruits] then give them a chance to select another one
#ask the user the price
#add all the total prices to give the total amount price of foods bought
#ask the user input if he/she is done with shopping, if yes , then(Q) to exit else continue loop through the same input
#use the file handling methods like file.write and file read to show past or save history of all the orders the user makes
#try using error handling methods like try and exceptions to handles all the errors
#thanks the user afterward and remind them to have a good day, happy coding


def shopping():
    
    #this nested function defined is use for viewing past orders history
    def history():
        try:
            with open("price.txt", "r") as file:
                print("Your past orders \n")
                print(file.read())
                print("--------------------------------")
        except FileNotFoundError:
            print("You have no past orders history yet!")
            
                   #a list for foods/fruits
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
                
                #call that nested function name view_history() on top of the file
                if order == 'history':
                    history()
                    continue

                    #Invalid order in the list create 
                elif order not in food:
                    print(f"{order} is unavailable in the menu")
                    print("Please select a another one!")

                    #valid order for items/values in the list we created
                elif order in food:
                    try:
                        price = int(input(f"What is the price of {order}:"))
                        total_amount += price
                        food_selected.add(order)

                        #saving to file
                        file = open("price.txt", "a")
                        file.write(f"{order} - ${round(price,2)} \n")
                        file.close()
                    except ValueError:
                        print("Please, enter the price in digits or numbers!")
                        continue

        print(sep=" ")
        print("-------------your order-------------------")
        print(food_selected)
        print(f"Your total is ${round(total_amount,2)}")
        print("Thanks, Have a nice day")

    if __name__=="__main__":
        main()
shopping()






