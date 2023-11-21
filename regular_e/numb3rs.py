#An IPv4 address is a numerical label assigned to each device 
# typically formatted in dot-decimal notation as #.#.#.#. 
# But each # should be a number between 0 and 255, inclusive. 
# Suffice it to say 275 is not in that range! 
# If only NUMB3RS had validated the address in that scene!

# In a file called numb3rs.py, implement a function called
#  validate that expects an IPv4 address as input as a str and 
# then returns True or False, respectively, if that input is a 
# valid IPv4 address or not.

import re
import sys


def main():
   ip = sys.argv[1]
   print(validate(ip))
   

#validate IPv4 address  #.#.#.#
# each 
def validate(ip):

  pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."\
    r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."\
    r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."\
    r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

  if re.match(pattern, ip):
    return True
  else:
    return False


    
     
    ...


...


if __name__ == "__main__":
    main()