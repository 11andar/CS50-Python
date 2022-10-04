# Print ammount due and prompt user for inserting a coin
# Each time user inserts a coin inform him about ammount due left and prompt for a coin again

prize = 50

while prize > 0:
    print(f"Ammount Due: {prize}")

# User can only insert 25, 10 or 5 cents
    insert = int(input("Insert Coin [25, 10, 5]: "))

    prize = prize - insert
 

# Print change owed at the end