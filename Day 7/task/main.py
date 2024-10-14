import random
from hangman_words import word_list
from hangman_art import *

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
display = placeholder

while display != chosen_word:

    guess = input("Guess a letter: ").lower()
    in_word = False
    # TODO-2: Change the for loop so that you keep the previous correct letters in display.

    if guess in display:
        print(f"You have already guessed {guess}")
        continue

    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display = display[:index] + guess + display[index+1:] #Ersetzen der Buchstaben
            in_word = True

    print(display)

    if not in_word:
        lives -= 1
        print(stages[lives])
        print(f"You guessed {guess}, that's not in the word\n****************************{lives} LIVES LEFT****************************")

    if lives == 0:
        print(f'It was {chosen_word}! YOU LOSE!')
        break

    if(lives != 0) and display == chosen_word:
        print(f'You WIN! The Word is {chosen_word}')
