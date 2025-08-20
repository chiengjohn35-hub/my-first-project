
#student information stored in the nested dictionary
students = {
    "david":{
        "age": 18,
        "Math": 76,
        "ENG": 82,
        "CHEM": 64,
        "PHY": 74,

    },
    "montana":{
        "age": 22,
        "Math": 68,
        "ENG": 76,
        "CHEM": 64,
        "PHY": 69,

    },
    "shariff": {
        "age": 16,
        "Math": 76,
        "ENG": 67,
        "CHEM": 78,
        "PHY": 63,
    },
    "sarah": {
        "age": 16,
        "Math": 78,
        "ENG":67,
        "CHEM":78,
        "PHY": 63,
    },
}


#asking user to enter a name using input prompt method to check if it's in the dictionary
#then we go to use a method like slice index or just index to access those values in the nested dictionary
students_name = input("what is student's name?:").strip()
if students_name in students:
    print("you are ", students[students_name]["age"], "years old")
    print("math:",students[students_name]["Math"],)
    print("english:",students[students_name]["ENG"])
    print("chemistry:",students[students_name]["CHEM"])
    print("physic:",students[students_name]["PHY"],)
    students_marks = (students[students_name]["Math"]  + students[students_name][ "ENG"]
                      +students[students_name]["CHEM"] + students[students_name]["PHY"])
    print("student scored in  percentages is ", students_marks/4)

    #showing the values to the user same time reminding them(student)  their scored and scores
    if students_marks >85:
        print("Result : Grade A+")
        print("You have Pass!")
        print("congratulations on your Outstanding Results")
        print("such a smart and hard working student, keep up")
    elif students_marks >75:
        print("Result : Grade A")
        print("You have Pass!")
        print("Grade results, keep up!")
    elif students_marks >65:
        print("Result : Grade B+")
        print("You have Pass!")
        print("Much efforts needed next time")
    elif students_marks >55:
        print("Result : Grade B")
        print("You have Pass!")
        print("Work harder and push yourself to your limits")
    elif students_marks >45:
        print("Result : Grade C")
        print("You have Pass!")
        print("much effort and work harder next time")
    else:
        print("Failed!")
        print(f"{students_name},You have to repeat class")


else:
    #using update method to add a new values to the dictionary

    print(f"{students_name} has not seated  for this  examinations")
    student_add= input(f"Has {students_name} seated for this examination?:(YES or NO!):").lower()
    if student_add == "yes":
        student_age = int(input(f"Enter {students_name}'s age:"))
        print(f"{students_name} is {student_age} years old")
        student_math = int(input(f"What's {students_name} marks  scored in Math?: "))
        student_eng = int(input(f"what is {students_name}'s marks  scored in English?: "))
        student_chem = int(input(f"what is {students_name}'s marks scored in Chemistry? "))
        student_phy = int(input(f"what is {students_name}'s marks scored in physic?: "))
        student_marks = (student_phy+student_chem+student_eng+student_math+student_chem )
        student_percent = (student_marks/4)
        if student_percent > 85:
            print("Result : Grade A+")
            print("You have Pass!")
            print("congratulations on your Outstanding Results")
            print("such a smart and hard working student, keep up")
        elif student_percent > 75:
            print("Result : Grade A")
            print("You have Pass!")
            print("Grade results, keep up!")
        elif student_percent > 65:
            print("Result : Grade B+")
            print("You have Pass!")
            print("Much efforts needed next time")
        elif student_percent > 55:
            print("Result : Grade B")
            print("You have Pass!")
            print("Work harder and push yourself to your limits")
        elif student_percent > 45:
            print("Result : Grade C")
            print("You have Pass!")
            print("much effort and work harder next time")
        else:
            print("Failed!")
            print(f"{students_name},You have to repeat class")

        students.update({f"{students_name}":{"age":{student_age},"Math":{student_math},
                                             "ENG": student_eng,"CHEM": student_chem,"PHY":student_phy,}})


    else:
        print(f"then {students_name} has to sat for the exams again!")



#using for loop to loop through nested dictionaries
# for x, obj in students.items():
#     print(x)
#     for y in obj:
#      print(y+ ":", obj[y])



