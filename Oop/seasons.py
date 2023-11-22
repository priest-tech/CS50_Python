#prompts the user for their date of birth in yyy-mm-dd format and prints how old
#they are in minutes rounded to the nearest integer using english words
#without any and between words
# assume the user was born at midnight and the current time will always be midnight regardless of the time the program is ran
from datetime import date
from num2words import num2words


def main():
   s= input("Enter your date of birth in yyy-mm-dd format: ")
   print(f'your age in minutes is {get_age_in_minutes(s)}')


def get_age_in_minutes(s):
   # assuming the user was born at midnight and the current time will always be midnight
   try:
        year, month, day = map(int, s.split('-'))
        today = date.today()
        time = (today - date(year, month, day)).days * 24 * 60
        return num2words(time).replace(" and", "")
   except ValueError:
      return "Invalid date format"
   

   
         
    


if __name__ == "__main__":
    main()