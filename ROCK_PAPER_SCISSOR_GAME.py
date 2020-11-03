# Rock-Paper-Scissor-Game
from random import randint


def rockPaperScissor():
    Player_score = 0
    Computer_Score = 0
    # create a list of play options
    t = ["Rock", "Paper", "Scissors"]

    # assign a random play to the computer
    computer = t[randint(0, 2)]
    player = input("""\nCHOOSE > Rock, Paper, Scissors.\nYour Move : """)
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            Computer_Score += 1
        else:
            print("You win!", player, "smashes", computer)
            Player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            Computer_Score += 1
        else:
            print("You win!", player, "covers", computer)
            Player_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            Computer_Score += 1
        else:
            print("You win!", player, "cut", computer)
            Player_score += 1
    else:
        print("That's not a valid play. Check your spelling!")
    print("")
    print("Your score: ", str(Player_score) + "\nComputer score: ", str(Computer_Score))


while True:
    rockPaperScissor()
