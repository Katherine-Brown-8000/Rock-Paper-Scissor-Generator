# Generate a Game of rock paper Scissors (My Version)

import random

# print("Rock is 0, Paper is 1, and Scicors is 2")

player_1_num = random.randint(0, 2)
player_2_num = random.randint(0, 2)

conversion = {0:"Rock", 1:"Paper", 2:"Scissors"}

# print(f"Player's 1 number is", player_1_num)
# print(f"Player's 2 number is", player_2_num)

player_1_draw = conversion[player_1_num]
player_2_draw = conversion[player_2_num]

print(f"Player 1 drew", player_1_draw)
print(f"Player 2 drew", player_2_draw)

def winner(player_1_draw, player_2_draw):
    # Player 1 rock conditons
    if player_1_draw == "Rock":
        if player_2_draw == "Paper":
            print("Paper beats Rock, Player 2 Wins!")
        elif player_2_draw == "Scissors":
            print("Rock beats Scissors, Player 1 Wins!")
        else:
            print("Rock and Rock is a Tie...")
    # Player 1 paper condions
    elif player_1_draw == "Paper":
        if player_2_draw == "Rock":
            print("Paper beats Rock, Player 1 Wins!")
        elif player_2_draw == "Scissors":
            print("Scissors Beats Paper, Player 2 Wins!")
        else:
            print("Paper and Paper is a Tie...")
    # Player 1 scicors condions
    elif player_1_draw == "Scissors":
        if player_2_draw == "Rock":
            print("Rock beats Scissors, Player 2 Wins!")
        elif player_2_draw == "Paper":
            print("Scissorss Beats Paper, Player 1 Wins!")
        else:
            print("Scissors and Scissors is a Tie...")
    else:
        print("There was an Error")

winner(player_1_draw, player_2_draw)
