""" This program will generate a random password for the user."""
import random

letters = [ chr(i) for i in range(97,123)]
symbols = [ chr(i) for i in range(32,48)]
numbers = [ chr(i) for i in range(48,58)]
password_list = []

print("Welcome to Random Password Generator!")

# This is the easy level part. The password here is in the order of letter+symbols +numbers

rand_lett = ""
rand_sym = ""
ran_num = ""
# full_password = rand_lett + rand_sym + ran_num
number_of_letters = int(input("How many letters do you want in your password?"))
number_of_symbols = int(input("How many symbols do you want in your password?"))
number_of_numbers = int(input("How many numbers do you want in your password?"))

for i in range(1,number_of_letters + 1):
    some_choice = random.choice(letters)
    password_list.append(some_choice)
    rand_lett += some_choice
for i in range(1,number_of_symbols + 1):
    some_choice = random.choice(symbols)
    password_list.append(some_choice)
    rand_sym += some_choice
for i in range(1,number_of_numbers + 1):
    some_choice = random.choice(numbers)
    password_list.append(some_choice)
    ran_num += some_choice
    
full_password = rand_lett + rand_sym + ran_num
print(f"Your random password is {full_password}")



# The harder part. this code will use some of the logic above
password = ""
random.shuffle(password_list)
for full_password in password_list:
    password += full_password
print(f"Your 2nd random password is {password}")

