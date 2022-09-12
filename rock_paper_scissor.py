import random

#Winner logic
def result(uMove, cMove):
    if (((uMove == "rock") & (cMove == "scissor")) | ((uMove == "paper") & (cMove == "rock")) | ((uMove == "scissor") & (cMove == "paper"))):
        return "User Wins!"
    elif (uMove == cMove):
        return "It's a Draw!"
    else:
        return "Computer Wins!"

#User move
user_move = input("Make your move (Rock/Paper/Scissor): ").lower()

#Computer move
moves = ["rock", "paper", "scissor"]
computer_move = random.choice(moves)

print("\nYou choose: "+user_move)
print("Computer choose: "+computer_move)
print("\n"+result(user_move,computer_move))