# 2-Guess the number (computer): The computer has a number and we need to guess it
import random


# Define a function to guess the number
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low")
        elif guess > random_number:
            print("Sorry, guess again. Too high")
    print(f"Yay, congrats! You have guessed the number {random_number} correctly!")


# guess(10)


# 3-Guess the number (user): The user has a number and the computer has to guess it
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess_computer = random.randint(low, high)
        else:
            guess_computer = low # or high as they are the same
        feedback = input(f'Is {guess_computer} too high (h), too low (l), or correct (c)')
        if feedback == 'h':
            high = guess_computer - 1
        elif feedback == 'l':
            low = guess_computer + 1

    print(f'Yay! The computer guessed your number {guess_computer} correctly')

computer_guess(1000)