def main():
    # Get name of a variable in camelCase from user
    camel_case = input("camelCase: ")

    # Print snake_case 
    print("snake_case: ", end = "")

    # Call camel_to_snake()
    camel_to_snake(camel_case)
 
def camel_to_snake(c):
    # Iterate over each character of user's input to find uppercase letters
    for letter in c:
        if letter.isupper():
            
            # Loop goes through each letter and prints it unchanged if it's in lowercase 
            # but if the letter is in uppercase it prints "_" before the letter and converts it to lowercase
            print(f"_{letter.lower()}", end = "")

        else:
            print(letter, end = "")
    
    print()


main()

     