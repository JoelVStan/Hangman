import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what user had guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('\nYou have', lives, 'lives left!\nYou have used these letters: ', ' '.join(used_letters))

        # what current word is (W _ R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('\nGuess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print("Letter is not in the word")


        elif user_letter in used_letters:
            print('\nYou have already used that character. Please try again!')

        else:
            print('Invalid character. Pleade try again!')

    if lives == 0:
        print('\nOh! Hangman died, you failed! The word was', word)
    else:
        print(f"\nYou guessed the word '{word}' right!! CONGRATS!!")


hangman()