def main():

    # Get input from user (meal prize and tip percentage)
    dollars = dollars_to_float(input("Prize: "))
    percent = percent_to_float(input("Percentage of the tip: "))

    # Calculate tip
    tip = dollars * percent

    # Output tip value
    print(f"${tip:.2f}")


def dollars_to_float(d):

    # remove '$' and return amout as a float
    d = d.replace("$", "")
    return float(d)

def percent_to_float(p):

    # remove "%" and return as a float
    p = p.replace("%", "")
    return float(p) / 100

main()