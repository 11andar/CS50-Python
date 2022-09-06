def main():
    # prompt user for time
    time = input("What's the time? ")
    
    
    


    # call convert()
    convert(time)


def convert(time):
    # create list of meal times
    meal_time = ["breakfast time", "lunch time", "dinner time"]

    # assign values to hours and minutes
    hours, minutes = time.split(":")
    
    # convert hours and minutes to float
    new_hours = float(hours)
    new_minutes = float(minutes) / 60

    print(new_hours + new_minutes)
    
    # determine when it's time for each meal
    

if __name__ == "__main__":
    main()
