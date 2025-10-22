import random

choices = ("rock","paper","scissors")

is_running = True
while is_running:

    player = None
    computer = random.choice(choices)


    while player not in choices:
        player = input("Enter any choice (rock, paper, scissor): ").lower()
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        if player == computer:
            print("ITS A TIE!")
        elif player == "scissors" and computer == "paper":
            print("YOU WIN!")
        elif player == "paper" and computer == "rock":
            print("YOU WIN!")
        elif player == "rock" and computer == "scissors":
            print("YOU WIN!")
        else:
            print("YOU LOSE!")
        if not input("'y' to play AGAIN and 'n' to NOT: ").lower() == "y":
            is_running = False
print("Thanks for playing")

