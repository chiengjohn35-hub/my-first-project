#File handling or savings
#Adding or check your previous name or text using file handling with
#methods like write(), read(), open() etc



print("1. Enter name:")
print("2. check name")
print("3. quit")
print(sep="")
while True:

    choice = input("enter your choice:").strip()
    if choice == "1":
        name = input("enter your name:")
        with open("name.txt", "a") as file:
            file.write(name)

    elif choice =="2":
        try:
            with open("names.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No name is saved in the history yet")

    elif choice=="4":
        break
    else:
        print("INVALID CHOICE!")





