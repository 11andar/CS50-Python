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

    time = new_hours + new_minutes
    
    # determine when it's time for each meal
    
    if  7 <= time <= 8:
        print(meal_time[0])
    elif 12 <= time <= 13:
        print(meal_time[1])
    elif 18 <= time <= 19:
        print(meal_time[2])
    else:
        print("It's not the time for a meal")


if __name__ == "__main__":
    main()
