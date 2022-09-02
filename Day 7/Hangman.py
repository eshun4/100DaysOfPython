""" This is a simple Hangman game."""
#Step 2

import random
import hangman_art
import hangman_words



chosen_word = random.choice(hangman_words.word_list)



lives = 6
#Testing code
print(hangman_art.logo)
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = list()
end_of_game = False
for l in range(len(chosen_word)):
        display += "_"
        
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    print(display)
    #TODO-2: - Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for l in range(len(chosen_word)):
        if chosen_word[l] == guess:
            display[l] = guess
    if "_" not in display:
        end_of_game = True
        print("You Win!")

    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            end_of_game = True
            print(f'Pssst, the solution is {chosen_word}.')
            print("Game Over!")
        else:
            print(hangman_art.stages[lives])
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)
print(hangman_art.stages[lives])