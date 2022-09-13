import random

#Check if user input is number (try/except statement)
#Keep prompting the user until they enter a number (while loop)
num_of_rounds = 1

while True:
    try:
        num_of_rounds = int(input("Enter the number of rounds you want to play: "))
    except ValueError:
        print("Please enter a valid integer")
        continue
    else:
        print(f'You entered: {num_of_rounds}')
        break

#Winner logic
def result(uMove, cMove, computerScore, userScore, drawScore):
    if (((uMove == "rock") & (cMove == "scissor")) | ((uMove == "paper") & (cMove == "rock")) | ((uMove == "scissor") & (cMove == "paper"))):
        print("User Wins!")
        userScore+=1
    elif (uMove == cMove):
        print("It's a Draw!")
        drawScore+=1
    else:
        print("Computer Wins!")
        computerScore+=1
    return (userScore,drawScore,computerScore)

#loop for number of rounds
try:
    computerScore = 0
    userScore = 0
    drawScore = 0
    for rounds in range(num_of_rounds):
        print("\nPlaying Round "+str(rounds+1))
        print("Press Ctrl+C to Exit")
        #Computer move
        moves = ["rock", "paper", "scissor"]
        computer_move = random.choice(moves)

        #User move
        user_move = ""
        while True:
            user_move = input("\nMake your move (Rock/Paper/Scissor): ").lower()
            if user_move in moves:
                break
            else:
                print("Not a valid move")

        print("\nYou choose: "+user_move)
        print("Computer choose: "+computer_move)
        print("\nRound "+str(rounds+1)+" Result: ")
        userScore,drawScore,computerScore = result(user_move,computer_move,computerScore, userScore, drawScore)
except KeyboardInterrupt:
    pass

print("\nSCORE\nPlayer: "+str(userScore)+"\nComputer: "+str(computerScore)+"\nDraws: "+str(drawScore))