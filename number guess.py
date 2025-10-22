import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
is_running = True
guesses = 0

print("Welome to Python Number Guessing Game!")

while is_running:
    guess = input(f"Enter any number between {lowest_num} and {highest_num}: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("Your Guess is out of Range!")
            print(f"Please enter any number between {lowest_num} and {highest_num}")
        elif guess > answer:
            print("TOO HIGH! TRY AGAIN!")
        elif guess < answer:
            print("TOO LOW! TRY AGAIN!")
        elif guess == answer:
            print("-----------------------------------")
            print(f"CORRECT! The Answer is {answer}")
            print(f"Number of Guesses: {guesses}")
            print("-----------------------------------")
            is_running = False

    else:
        print("Invalid Guess!")




