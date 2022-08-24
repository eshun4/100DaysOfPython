""" This program calculates the tip each person is supposed to pay after the total bill."""

print("Welcome to the tip Calculator.")

total_bill = input("What was the total bill? $")
percentage_tip = input("What percentage tip would you like to give? 10, 12, 03 15? ")
people = input("How many people to split the bill? ")

each_person_pays = float(total_bill) / float(people)
tip_per_person = ((float(percentage_tip)/100) * (each_person_pays))
total_amount_per_person = each_person_pays + tip_per_person

print(f"Each person pays: ${round(total_amount_per_person,2)}")