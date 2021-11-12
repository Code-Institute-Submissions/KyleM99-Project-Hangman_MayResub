import random
from words import words
from hangman_visuals import hangman_lives_visual
import string

# Function to pull a random word from the list
def random_hangman_word(words):
    word = random.choice(words) # Chooses a word at random
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

# Main hangman function
def hangman():
    word = random_hangman_word(words)
    words_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    # User input
    while len(words_letter) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # Current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(hangman_lives_visual[lives])
        print('Current Word: ', ' '.join(word_list))

        # User guess
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in words_letter:
                words_letter.remove(user_letter)
                print('')
            else:
                lives = lives - 1 # Removes 1 life if wrong
                print('\nYour letter,', user_letter, 'is not in the word!')
        elif user_letter in used_letters:
            print('\nYou have already tried that letter. Guess another!')
        else:
            print('\nThat is not a valid letter.')
    
    if lives == 0:
        print(hangman_lives_visual[lives])
        print('You have lost the game of Hangman. The word was', word)
    else:
        print('Congrats! You guessed the word', word, '!!')
    #
if __name__ == '__main__':
    hangman()