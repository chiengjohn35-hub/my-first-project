#ask the user input to select the food
#if user input selected a food not in the menu[fruits] the give them a chance to select another one
#ask the user the price
#add all the total prices to give the total about of foods bought
#ask the user input if he/she is done with shopping, if no , then(Q) to exit else continue
#thanks the user afterward and remind them to come and there are welcome back next time


def shopping():

    print("              MENU")
    print("--------------------------------------------")
    fruits = ["mango", "orange", "banana", "cherry", "apple", "pineapple", ]
    fruits_selected = []

    for x in fruits:
        print(x, end=" " )

    print(sep="")
    print("--------------------------------------------")
    is_running = True
    total_price = 0.0


    while is_running:
        foods = input("Select the fruits you are buying (Q) to quit : ").strip()
        if foods.lower() == "q":
            is_running = False
        else:
            if foods not in fruits:
                print(f"{foods} is unavailable in the menu")
                print("please select another!")
                continue
            price = float(input(f"what is the price of {foods}?:"))

        for x in fruits:
            if foods in x:
                fruits_selected.append(foods)

            total_price += price

    print("--------------------------------------------------------")
    print("             your cart")


    print(fruits_selected)
    print(f"Your total price of food is ${total_price}")
    print("*********************************************************************")
    print("Thanks for shopping, Have a nice day")

shopping()



# I have some little problem espesically with calculation, it give out all the exact about of total price if added all together
# please feel free to work on it if you can, as i will be working on finding the solution myself



