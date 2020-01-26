from datetime import datetime

def check_birthdate(year, month, day):
    today = datetime.now()
    birthdate = datetime(year, month, day)
    if birthdate > today:
        return False
    else:
        return True

def calculate_age(year, month, day):
    today = datetime.now()
    birthdate = datetime(year, month, day)
    age = (today - birthdate).days
    print(f"You are {(age/365):.0f} years old.")
# or     print(f"You are {age//365} years old.") double divide does not take an fractions

year = int(input("Enter the year:  "))
month = int(input("Enter the month:  "))
day = int(input("Enter the day:  "))

if check_birthdate(year,month,day):
    calculate_age(year,month,day)
else:
    print("You have entered an invlaid birthdate.")
