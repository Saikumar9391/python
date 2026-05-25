import datetime

current_year = datetime.datetime.now().year

try:
    name = input("Enter your name: ").strip().title()
    
    birth_year = int(input("Enter your birth year (e.g., 1995): "))

    age = current_year - birth_year

    if birth_year > current_year:
        print("Error: Your birth year cannot be in the future!")
    elif age > 120:
        print("Error: Please enter a realistic birth year.")
    else:
        print(f"\nHello, {name}! You are {age} years old this year.")

except ValueError:
    print("Error: Please enter a valid 4-digit number for your birth year.")