#guessing number
import random
def guess():
    num = random.randint(2,8)
    num_of_guess = 0
    you_try =0

   #adding the user and number of times he guessed the correct number
    while True:
        user = int(input("enter a number between (2-8) to guess the correct number:"))
        if user == num:
            print("you have guess the correct number", num)
            print("it took you ", num_of_guess, " times about to guessed it. ")
            break
        elif user <2:
            print("Number is too low")

        elif user >num:
            print("Number is too high")

        else:
            print("keep trying... " )
            num_of_guess += 1

guess()












#hangman game
import random
def hangman():
    body_parts = ["head", "legs", "arms"]
    num_of_guess = 6
    correct_parts = set()
    guess_parts = random.choice(body_parts)

    while num_of_guess >0:
        user_guess = input("enter any of this (head, legs, arms) to guess the right body part:").strip()
        if user_guess in correct_parts:
            print("you have already guessed this body part", user_guess)
            continue
        correct_parts.add(user_guess)
        if user_guess not in correct_parts:
            continue
        correct_parts.remove(user_guess)

        if user_guess == guess_parts:
            print("you have guessed the right body part", guess_parts)

        else:
            num_of_guess -=1
            if num_of_guess >0:
                print("keep trying... you still have ", num_of_guess, "left to guess body parts.")
            else:
                print("---game over----")
                break
hangman()








        #rock, paper and scissor
    #adding the players
player1 = input("what is player 1 name?:")
player2 = input("what is player 2  name?:")

#adding the questions
while True:
    player1_turn = input(f"{player1} Choose any between the three (rock, paper or scissor) :").strip()
    player2_turn = input(f"{player2} Choose any between the three (rock, paper or scissor) :").strip()
    player1_score = 0
    player2_score = 0

    if player1_turn == "rock" and player2_turn == "scissor":
        print(f"{player1} wins!")
    elif player1_turn == "scissor" and player2_turn == "paper":
        print(f"{player1} wins!")
    elif player1_turn ==  "paper" and player2_turn == "rock":
        print(f"{player1} wins")
    elif player2_turn == "rock" and player1_turn == "scissor":
        print(f"{player2} wins!")
    elif player2_turn == "scissor" and player1_turn == "paper":
        print(f"{player2} wins!")
    elif player2_turn ==  "paper" and player1_turn == "rock":
        print(f"{player2} wins")
    else:
        print("that's not part of the game")
        break
























