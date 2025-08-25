import random
from simple import words

def guessing():
    selected_words = set()
    score = 0
    num_of_try = 26

    parts = random.choice(words).split(",")
    question = parts[0]
    answers = parts[1]
    print("create word for each any every in Alphabet ")
    print("--------------------------------------------")
    print(sep="")

    user_question = input(question).strip()

    while num_of_try>0:
        if not user_question.isalpha():
            print("please enter a word for each letter")
            continue
        if answers in question:
            print("You have already answer")
            print("please try other ones!")
            continue
        selected_words.add(answers)
        if user_question == answers:
            print(f"Correct!, it stands for {answers}")
            score+= 1
            num_of_try-=1
            continue

        else:
            score=0
            if num_of_try>0:
                print(f"Incorrect!, the correct word is {answers}")
                print("please try again!")
            elif num_of_try<0:
                print("your chances are finished")
                break

    print(sep="")
    print("--------------------------------------------")
    print(f"your total Marks is {score} out of 26")

guessing()