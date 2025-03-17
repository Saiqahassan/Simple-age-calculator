from datetime import datetime

print("Welcome to the simple age calculator!\n")
print("-------------------------------\n")
def calculate_age():
    birth_date_str = input("Enter your birthdate (DD/MM/YYYY): ")
    try:
        birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
        current_year = 2025
        age = current_year - birth_date.year
        
        if birth_date.month > 1 or (birth_date.month == 1 and birth_date.day > 1):
            age -= 1
        
        print(f"You are {age} years old in {current_year}.")
        if age < 100:
            print(f"You will turn 100 in {100 - age} years.")
        else:
            print("You are 100 years old or older!")
    except ValueError:
        print("Invalid input! Please enter a valid date in DD/MM/YYYY format.")

calculate_age()
