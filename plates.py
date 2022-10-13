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
        if p[0].isalpha() == False or p[1].isalpha == False:
            return False
        
         # Minimum 2 and maximum 6 characters
        if len(p) < 2 or len(p) > 6:
            return False
        
        # Numbers at the end
        if p[-1].isalpha():
            return False
        
        # First number cannot be 0
       

        
        # No special signs allowed
        


main()