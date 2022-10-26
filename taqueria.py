from asyncio.proactor_events import _ProactorDuplexPipeTransport


def main():
    
    print()
    
    # Create a dictionary (producuct : cost)
    products = {
    
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    
    }

    

    # Display products and their cost
    for product in products:
        
        p = float(products[product])

        print(f"{product}: {p:.2f}")

    print()

    # Run the product choice in a loop
    total = 0
    while True:
        # try
        
        try:
            # Get an item from user
            item = input("Item: ")
            # Convert input to titlecase() 
            item = item.title()
            # Calculate total cost
        
            total = total + products[item]
            
            # Display total cost formatted to two decimal points
            # Prefix total cost with '$'
            print(f"Total: ${total:.2f}")

        # except
        # Ignore KeyError
        # Ignore products that are not in the dictionary
        except (ValueError, KeyError):
            pass
        # End the program using ctrl+D
        except EOFError:
            print()
            break

main()