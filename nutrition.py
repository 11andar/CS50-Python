def main():
    # Ask user for fruit
    choice = input("Fruit: ")

    if show_calories(choice) == True:
        print("Calories: ")
    else:
        print()
    
# Define 'show_calories' function
def show_calories(c): 
    
    # Create a dictionary which assigns calories to fruits
    fruits = {
        "Apple" : 130,
        "Avocado" : 50,
        "Banana" : 110,
        "Cantaloupe" : 50,
        "Grapefruit" : 60,
        "Grapes" : 90,
        "Honeydew Melon" : 50,
        "Kiwifruit" : 90,
        "Lemon" : 15,
        "Lime" : 20,
        "Nectarine" : 60,
        "Orange" : 80,
        "Peach" : 60,
        "Pear" : 100,
        "Pineapple" : 50,
        "Plums" : 70,
        "Strawberries" : 50,
        "Sweet Cherries" : 100,
        "Tangerine" : 50,
        "Watermelon" : 80,
    }

    # Create a loop that prints amount of calories of fruit which user chose
    for fruit in fruits:
        if c == fruit:
            return True
        else:
            return False

main() 