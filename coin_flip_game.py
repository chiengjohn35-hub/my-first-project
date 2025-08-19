#flipping coin game
import random
coin_parts = ["head", "tails"]
flip_coin =random.choice(coin_parts)

#adding the players
players = input("enter the number of players(2-4):").strip()
if players.isdigit():
    players = int(players)
    if  2<= players <=4:
        print("--game starting--")
    else:
        print("players must be between 2-4!")
else:
     print("you should enter a digit or number but no a word!")

max_score = 5
player_score=  [0 for _ in range(players)]
num_of_try = 10
score =0
while max(player_score)<max_score:
    for player_idx in range(players):
        print(" n/ player number", player_idx+1, "turn starts /n")
        secret_flip = coin_parts
        flip_coin = random.choice(coin_parts)

        player_flip = input("enter any (head or tails) to guess coin part:")
        if player_flip == flip_coin:
            print("Correct! Outstanding")
            score += 1
            num_of_try-=1
            break
        else:
            score = 0
            num_of_try -= 1
            if num_of_try > 0:
                print("Wrong! nice try...")
                break
            else:
                print("---game over----")


        player_score[player_idx]+= score
        print("player number", player_idx+1, "score is ", score)
        current_max = max(player_score)
        winning_idx = player_score.index(current_max)
        print("player number", winning_idx+1, "is the winner with a scored of", current_max)










