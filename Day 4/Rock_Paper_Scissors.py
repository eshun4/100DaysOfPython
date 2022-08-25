"""This is a Project to create a rock paper scissors game.
"""
import random

rounds = 0
user_score = 0
computer_score = 0


print("Welcome to the Rock, Paper, Scissors Game!")
print('')
test_seed = int(input("Enter any number to play: "))
random.seed(test_seed)

rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    
    rock
    '''

paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    
    paper
    '''

scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    
    scissors
    '''

options = [rock, paper, scissors]
number_of_options = len(options)
random_index = random.randint(0, number_of_options -1)
users_choice = options[random_index]

computer_choice = random.choice(options)
print('This is the computer"s choice.')
print(computer_choice)
print('')
print('')
print('')
print('')
print('This is your choice.')
print(users_choice)
user_score = 0
computer_score = 0

if users_choice == rock and computer_choice == rock:
    print("Draw!\nPlay Again!")
    print(f"Your score: {user_score}")
    print(f"Computer's Score: {computer_score}")
elif users_choice == rock and computer_choice == paper:
    print("You Lost!\nPlay Again!")
    computer_score += 1
    print(f"Your score: {user_score}")
    print(f"Computer's Score: {computer_score}")
elif users_choice == paper and computer_choice == rock:
    print("You Won!")
    user_score += 1
    print(f"Your score: {user_score}")
    print(f"Computer's Score: {computer_score}")
elif users_choice == paper and computer_choice == scissors:
    print("You Lost!\nPlay Again!")
    computer_score += 1
    print(f"Your score: {user_score}")
    print(f"Computer's Score: {computer_score}")
elif users_choice == scissors and computer_choice == paper:
    print("You Won!")
    user_score += 1
    print(f"Your score: {user_score}")
    print(f"Computer's Score: {computer_score}")
elif users_choice == scissors and computer_choice == rock:
    print("You Lost!\nPlay Again!")
    computer_score += 1
    print(f"Your score: {user_score}")
    print(f"Computer's Score: {computer_score}")
elif users_choice == rock and computer_choice == scissors:
    print("You Won!")
    user_score += 1
    print(f"Your score: {user_score}")
    print(f"Computer's Score: {computer_score}")
elif users_choice == paper and computer_choice == paper:
    print("Draw!\nPlay Again!")
    print(f"Your score: {user_score}")
    print(f"Computer's Score: {computer_score}")
elif users_choice == scissors and computer_choice == scissors:
    print("Draw!\nPlay Again!") 
    print(f"Your score: {user_score}")
    print(f"Computer's Score: {computer_score}")  

    
        


