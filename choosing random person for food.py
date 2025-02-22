import random

# Get the number of persons
numbers_for_split = int(input("Enter the number of persons for lunch (between 2 and 10): "))

# Ensure the input is within the valid range
if numbers_for_split < 2 or numbers_for_split > 10:
    print("Invalid input! Please enter a number between 2 and 10.")
else:
    # Collect names using a loop
    names = []
    for i in range(1, numbers_for_split + 1):
        name = input(f"Enter name {i:02}: ")
        names.append(name)

    # Select a random person to pay
    person_who_will_pay = random.choice(names)
    print(f"{person_who_will_pay} is going to pay for today's meal!")
