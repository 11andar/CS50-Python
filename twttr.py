# Define main() function
def main():
    
    # Take input from user
    word = input("Input: ")

    print("Output: ", end = "")
    short(word)

    print()

# Define short() function
def short(w):
    #Create list of vowels
    vowel = ["a", "e", "u", "i", "o"]
    # Iterate over each character of input to find vowels
    for letter in w:
        # Print letter if it's not a vowel
        if not letter.lower() in vowel:
            print(letter, end = "")
        # Continue looping if letter is a vowel
        elif letter in vowel:
            continue
    

main()