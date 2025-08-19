import math
def calculator():
#adding the user input
    try:
        x = int(input("enter the first number:"))
        y = int(input("enter the second number:"))
        operator = input("select operator  +, -, /, * , ^, sqrt, sin, cos :").strip()

#adding the arithmatic operators
        if operator =="+":
            print ("results:",x+y)
        elif operator =="-":
            print("Results:", x-y)
        elif operator == "*":
            print("Results:",  x*y)
        elif operator == "/":
            if y != 0:
                print("Results:", x / y)
            else:
                print("ERROR, Value cannot be divided by Zero!")
        elif operator == "sin":
            print("Results: ", math.sin(x))
            print("Results :", math.sin(y))
        elif operator == "sqrt":
            print("Results: ", round(math.sqrt(x),2))
            print("Results :", round(math.sqrt(y,),2))
        elif operator == "cos":
            print("Results: ", math.cos(x))
            print("results :", math.cos(y))
        else:
            print("operator invalid")
    except ValueError:
        print("you must enter a digit or number but no word")


calculator()