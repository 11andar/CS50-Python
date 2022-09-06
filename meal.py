def main():
    # prompt user for time
    time = input("What's the time? ")
    
    # assign values to hours and minutes
    hours, minutes = time.split(":")


    # call convert()
    convert(time)


def convert(time):
    # create list of meal times
    meal_time = ["breakfast time", "lunch time", "dinner time"]
    
    # convert hours and minutes to float
    
    
    # determine when it's time for each meal


if __name__ == "__main__":
    main()
