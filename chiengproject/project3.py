# guessing number
import random
def number():
    min_num = 2
    max_num = 8
    guess_num =random.randint(min_num,max_num)
    num_of_guessing = 10

#adding the players
    player = input("Enter the number(2-3) of players:")
    if player.isdigit():
        player = int(player)
        if 1<= player <=4:
            pass
        else:
            print("players should be 2 to 3")


#adding the max score, for player who guessed the correct
    # score multiply times is considered has the winner
    max_score = 20
    player_score = [0 for _ in range(player)]
    while max(player_score) < max_score:
        while num_of_guessing >0:
            for player_idx in range(player) :
                print("/n player number", player_idx+1  , "turn has just started ")
                print("you have ", num_of_guessing, " chances to guess the correct number /n")


            #Here we have to use while loop to loop through the number of times all the players should
                #guess the correct number given only 10 chances, all for the players
                #then if it's over the winner is de-cleared for those who guessed the exact number at the end of those 10 chances

                player_guessing = int(input("Enter a digit between (2-8) to guess the exact number:"))
                score = 0

                right_num = guess_num


                if player_guessing == right_num:
                    print("You have guessed the correct number", right_num)
                    num_of_guessing -= 1
                    score += 1
                elif player_guessing <2:
                    print("player must be between (2-8)")
                    break

                else:
                    score = 0
                    num_of_guessing -= 1

                    if num_of_guessing > 0:
                        print("keep trying...")
                        print("you have ", num_of_guessing, " chance(s)  to guess!. ")
                        pass
                    else:
                        break


                #Here we have to remind each player his score meaning one correct score,you score is added by one else it's and remains
                # zero for wrong guess as you can see up  them

                #then we will find out who is the winner of the number guessing game using max keyword
                #add we create a variable name winning idx, thus will determine for us who has multiply correct guessed
                #and who has high max score is printed out as the winner
                player_score[player_idx] += score
        max_score = max(player_score)
        winning_idx = player_score.index(max_score)
        print("player number", winning_idx + 1, "is the winner")
        print("he has guessed the correct number", max_score,"time(s)")

number()











