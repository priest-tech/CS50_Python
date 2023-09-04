def main():
  tank=fuel("Fraction: ")
  print(f"{tank}")

def fuel(prompt):
  while True:
    try:
      fraction = (input(prompt))
      numerator,denominator =map(int, fraction.split('/'))
      percentage = (int(numerator)/int(denominator)) * 100 
      if percentage >= 99.0:
          return("F")
      elif percentage <= 1.0:
          print("E")  
      else:  
        return str(percentage) + "%"    
    except (ValueError,ZeroDivisionError):
      
      pass
       

main()    
