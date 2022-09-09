def main():
    # Get name of a variable in camelCase from user
    camel_case = input("camelCase: ")

    # Print snake_case and call camel_to_snake()
    print(f"snake_case: {camel_to_snake(camel_case)}")
 
def camel_to_snake(c):
    # Iterate over each character of user's input to find uppercase letters
    for letter in c:
        if letter.isupper() is True:
            return True
            
        
    
    # Put "_" in every spot where lowercase meets uppercase in that particular order: lowercase_uppercase

    

main()

     