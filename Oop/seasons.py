#prompts the user for their date of birth in yyy-mm-dd format and prints how old
#they are in minutes rounded to the nearest integer using english words
#without any and between words
# assume the user was born at midnight and the current time will always be midnight regardless of the time the program is ran
from datetime import  datetime
from num2words import num2words
import sys


def main():
   s= sys.argv[1]
   print(f'{get_age_in_minutes(s)}')


def get_age_in_minutes(s):
    # assuming the user was born at midnight and the current time will always be midnight
    try:
        dob = datetime.strptime(s, "%Y-%m-%d").replace(hour=0, minute=0, second=0, microsecond=0)
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        age_time = 0

        # Calculate age in minutes
        age_time = (today - dob).total_seconds() / 60

        # Handle leap years within the if statement
        if leap_year(dob.year):
            age_time += 24 * 60

        return num2words(age_time).replace(" and", "")
    except ValueError:
        return "Invalid date format"

def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
   
   
         
    


if __name__ == "__main__":
    main()