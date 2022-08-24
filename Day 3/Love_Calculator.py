"""Instructions
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is **z**."
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()
total_true = 0
total_love = 0
if lowercase_name1.count('t') >= 0 and lowercase_name2.count('t') >= 0:
    total_true += lowercase_name1.count('t') + lowercase_name2.count('t')
if lowercase_name1.count('r') >= 0 and lowercase_name2.count('r') >= 0:
    total_true += lowercase_name1.count('r') + lowercase_name2.count('r')
if lowercase_name1.count('u') >= 0 and lowercase_name2.count('u') >= 0:
    total_true += lowercase_name1.count('u') + lowercase_name2.count('u')
if lowercase_name1.count('e') >= 0 and lowercase_name2.count('e') >= 0:
    total_true += lowercase_name1.count('e') + lowercase_name2.count('e')
else:
    pass
if lowercase_name1.count('l') >= 0 and lowercase_name2.count('l') >= 0:
    total_love += lowercase_name1.count('l') + lowercase_name2.count('l')
if lowercase_name1.count('o') >= 0 and lowercase_name2.count('o') >= 0:
    total_love += lowercase_name1.count('o') + lowercase_name2.count('o')
if lowercase_name1.count('v') >= 0 and lowercase_name2.count('v') >= 0:
    total_love += lowercase_name1.count('v') + lowercase_name2.count('v')
if lowercase_name1.count('e') >= 0 and lowercase_name2.count('e') >= 0:
    total_love += lowercase_name1.count('e') + lowercase_name2.count('e')
else:
    pass

love_score = f'{total_true}{total_love}'
number_score = int(love_score)

if number_score < 10 or number_score > 90:
    print(f"Your score is {number_score}, you go together like coke and mentos.")
elif 40 < number_score < 50:
    print(f"Your score is {number_score}, you are alright together.")
else:
    print(f"Your score is {number_score}.")