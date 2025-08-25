#ask the user input to select the food
#if user input selected a food not in the menu[fruits] the give them a chance to select another one
#ask the user the price
#add all the total prices to give the total about of foods bought
#ask the user input if he/she is done with shopping, if no , then(Q) to exit else continue
#thanks the user afterward and remind them to come and there are welcome back next time


def shopping():
    print("             MENU")
    print("------------------------------------")
    fruits = ["orange", "mango", "pineapple", "cherry", "banana"]
    fruits_selected = []

    for x in fruits:
        print(x, end=" ")

    print(sep=" ")
    print("------------------------------------")

    is_running = True
    total_price =0.0

    while is_running:
        food = input("select the food you want (Q) to quit:").strip()
        if food.lower() == "q":
            is_running =False
        else:
            if food not in fruits:
                print(f"{food} is unavailable in the Menu, ")
                print("Please select another one!")
            else:
                price = float(input(f"what is the price of {food}:"))
                total_price+=price

        for x in fruits:
            if food in x:
                fruits_selected.append(food)


    print("------------------------------------")
    print("-------------Your cart---------------")
    print(fruits_selected)
    print(f"your total amount is ${round(total_price,2)}")
    print("************************************")
    print("thanks for shopping, Have a nice day!")




shopping()






