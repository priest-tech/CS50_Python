def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) >= 2 and len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            if s[-1].isdigit():
                for i in range(2, len(s) - 1):
                    if s[i].isdigit() and s[i + 1].isalpha():
                        return False
                return True
    return False

main()

