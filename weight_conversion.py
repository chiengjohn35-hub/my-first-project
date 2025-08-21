#weight conversion

unit = input("enter the weight unit:(pounds,lbs or kg):").lower()
weight= float(input("enter the weight:"))

if unit =="kg":
    results = round((weight*2.2),3)
    print(f"{results}lbs")
elif unit == "lbs" or "pounds":
    results = round((weight/2.2),2)
    print(f"{results}kgs")
else:
    print("that's unit is available!")

