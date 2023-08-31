def ambreviator():
    word= str(input("Input "))
    result =""

    vowels = "AEIOUaeiou"

    for char in word:
        if char not in vowels:
            result += char
        
    print(f"Output: {result}")



ambreviator()    

