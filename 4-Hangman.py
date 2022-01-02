# 4-Play hangman
import random
from words import words
import string


# Since some words are not valid (because they have "-" or " " within their strings), we need to
# create a function to get a valid word
def get_valid_word(list_words):

    # Choose a random word from the list words
    word = random.choice(list_words)

    # Create a loop to choose a word when it contains "-" or " "
    while "-" in word or " " in word:
        word = random.choice(list_words)

    # We are going to uppercase all our letters
    return word.upper()


# Create the function for the Hangman game
def hangman():
    word = get_valid_word(words)

    # Save word letters in a set
    word_letters = set(word)

    # Create an alphabet
    alphabet = set(string.ascii_uppercase)

    # Empty set with letters guessed by the user
    used_letters = set()

    # Define the number of lives
    lives = 6

    # Create a loop until user guesses the word
    while len(word_letters) > 0 and lives > 0:

        # Print letters used
        # " ".join(['a', 'b', 'cd']) --> 'a b cd' - It converts a list into a string separated by a space
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

        # Print the current word (W _ R D)
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word: ", " ".join(word_list))

        # Get user input
        user_letter = input("Guess a letter: ").upper()

        # Conditional to include user input in used_letters and remove it from word_letters
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1 # Taking away a life if wrong
                print("Letter is not in word")
        elif user_letter in used_letters:
            print("You have already used this letter! Please try again")
        else:
            print("Invalid character! Please try again")

    if lives == 0:
        print("Sorry, you died. The word was: ", word)
    else:
        print("Congrats! You guessed the word: ", word)


hangman()