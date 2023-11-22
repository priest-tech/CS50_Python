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

        # Count leap years between DOB and today
        leap_years = 0
        for year in range(dob.year, today.year):
            if leap_year(year):
                leap_years += 1

        # Add leap day minutes if applicable
        if leap_years > 0:
            age_time += leap_years * 24 * 60

        return num2words(age_time).replace(" and", "")
    except ValueError:
        print("Invalid date format. Please enter date in YYYY-MM-DD format.")
        sys.exit(1)

def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
         
    


if __name__ == "__main__":
    main()