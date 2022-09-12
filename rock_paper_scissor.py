import random

#Winner logic
num_of_rounds = input("Enter the number of rounds: ")

def result(uMove, cMove):
    if (((uMove=="rock") & (cMove=="scissor")) | ((uMove=="paper") & (cMove=="rock")) | ((uMove=="scissor") & (cMove=="paper"))):
        return "User Wins!"
    elif (uMove==cMove):
        return "It's a draw!"
    else:
        return "Computer Wins!"

#User move
user_move = input("Make your move: (Rock/Paper/Scissor)").lower()

#Computer move
moves = ["rock", "paper", "scissor"]
computer_move = random.choice(moves)

print("You choose: "+user_move)
print("Computer choose: "+computer_move)
print(result(user_move,computer_move))