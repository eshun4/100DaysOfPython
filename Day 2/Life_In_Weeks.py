""" Instructions
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

https://waitbutwhy.com/2014/05/life-weeks.html

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops."""

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
months = int(age) * 12 
days = int(age) * int(365.2425)
weeks = int(age) * 52

months_to_live = 90 * 12
days_to_live = 90 * int(365.2425)
weeks_to_live = 90 * 52

months_remaining = months_to_live - months
days_remaining = days_to_live - days
weeks_remaining = weeks_to_live - weeks
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")



