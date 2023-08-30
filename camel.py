def main():
    word=input("Enter the word in CamelCase: ")
    snake_case_word = camel_to_snake(word)
    print("Snake case:", snake_case_word)

def camel_to_snake(camel_case_string):
    result = []
    for char in camel_case_string:
        if char.isupper():
            result.append("_")
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)
            
main()

