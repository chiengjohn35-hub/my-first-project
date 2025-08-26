#simple calculator

def main():
    def add():
        num1 = int(input("enter the first number:"))
        num2 = int(input("enter the second number:"))
        print(num1+num2)
    def subtract():
        num1 = int(input("enter the first number:"))
        num2 = int(input("enter the second number:"))
        print(num1-num2)
    def multiply():
        num1 = int(input("enter the first number:"))
        num2 = int(input("enter the second number:"))
        print(num1 * num2)

    def divide():
        num1 = int(input("enter the first number:"))
        num2 = int(input("enter the second number:"))
        if num2 != 0:
            print(round(num1 / num2,2))
        else:
            print("Error... Zero cannot be divided by any number")


    operator = input("Select operator;  + , - , * , /  :")
    if operator=="+":
        add()
    elif operator =="-":
        subtract()
    elif operator =="*":
        multiply()
    elif operator =="/":
        divide()
    else:
        print("INVALID CALCULATOR")

if __name__ == '__main__':
    main()


