#File handling or savings
#Adding or check your previous name or text using file handling with
#methods like write(), read(), open() etc

print("1. Enter name:")
print("2. check name")
print("3. quit")
print(sep="")
while True:

    choice = input("enter your choice:").strip()
    #Adding or saving to file
    if choice == "1":
        name = input("enter your name:")
        file = open("name.txt", "a")
        file.write(f"{name} \n")
        file.close()

    #Viewing the save names in the file
    elif choice =="2":
        try:
            with open("name.txt", "r") as file:
                print("Your past names")
                print(file.read())
        except FileNotFoundError:
            print("No name is saved in the history yet")

    elif choice=="4":
        break
    else:
        print("INVALID CHOICE!")




