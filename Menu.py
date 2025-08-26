print("-------------MENU--------------")
foods ={
        "chicken curry":      50.0,
        "veg.fried rice":     50.00,
        "eggs fried rice":60.00,
        "special fried rice":90.00,
        "chicken fried rice":70.00,
}

for x, obj in foods.items():
    print(f"{x}:  {obj}")
print("----------------------------------")
print(sep=" ")

def main():
    total = 0
    foods_selected = set()

    while True:
        order = input("What is you order please? (Q) to quit : ").strip()
        if order.lower()=="q":
            break
        else:
            if order.isdigit():
                print("Please Customer enter you order in words!")
                continue
            if order not in foods:
                print(f"Your order {order} is unavailable in the Menu,")
                print("please Customer select another one!")
            else:
                price = int(input(f"How many plates or orders of {order} you want?:"))

                total += foods[order]*float(price)


            for _ in foods:
                if order in _:
                    foods_selected.add(order)

    print(sep="")
    print("---------------your order-----------")
    print(foods_selected)
    print(f"Your total is ${round(total,2)}")
    print("-------------------------------------")
    print("Thank Customer, Have a nice day!")

if __name__=="__main__":
    main()







