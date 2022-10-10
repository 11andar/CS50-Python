# Define main()
def main():
    # Take input from user 
    plate = input("Plate: ")
    plate = plate.upper()
    
    # If plate is valid print 'Valid'
    if is_valid(plate) is True:
        print("Valid")
    
    # Else print 'Invalid'
    else:
        print("Invalid")

# Define is_valid()
def is_valid(p):
    for character in p:
        # Must start with at least two letters
        if p[0:2].isalpha():
            return True
        
        # Minimum 2 and maximum 6 characters
    
        
        # Numbers at the end

        
        # First number cannot be 0

        
        # No special signs
main()