from termcolor import colored
from random_word import RandomWords
import sys

# Menu
print("Let's play Wordle:")
print("Type a 5 letter word below and press Enter. You have 6 tries to guess the random word.\n")


# Random word generator function
def generate_random_word():
    random_word_generator = RandomWords()
    return random_word_generator.get_random_word(hasDictionaryDef = 'true', maxLength = 5, includePartOfSpeech="noun,verb,adjective")

word = generate_random_word()
# print(word)


# User guesses the word function
def Wordle():
    for no_of_attempts in range(1,7):
        user_guess = input().lower()

        # overwriting the last line in the console
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        # printing colored letters
        for i in range(min(len(user_guess), 5)):
            if user_guess[i] == word[i]:
                print(colored(user_guess[i], 'green'), end="")
            elif user_guess[i] in word:
                print(colored(user_guess[i], 'yellow'), end="")
            else:
                print(user_guess[i], end="")
        print()
        
        if user_guess == word:
            print(f"Congratulations! You guessed the word in {no_of_attempts} guesses.")
            break
        elif no_of_attempts == 6:
            print(f"You didn't guess the word within 6 tries, it was: {word}")

Wordle()