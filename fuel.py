def main():
    
    # Keep running the program until user inputs correct values
    while True:     
        try:
        # Prompt user for fraction formatted as X/Y
            fraction = input("Fraction: ")
            
        # Assign first value to x and second value to y    
            x, y = fraction.split("/")

        # Convert values to ints
            x = int(x)
            y = int(y)
            
            divide = int((x/y) * 100)

        # If there is only 1% or less left output E
            if divide <= 1:
                print("E")
        # If there is 99% or more output F
            elif divide >= 99:
                print("F")
        # Else output how full is the tank (in %)
            else:
                print(f"Your tank is {divide}% full")
        
        # Break out of the loop if values are correct
            break
        
        # Ignore ValueError and ZeroDivisionError
        except (ValueError, ZeroDivisionError):
            pass


main()
