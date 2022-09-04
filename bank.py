def main():
# prompt user for greeting
    greeting = input("Greeting: ")
    check(greeting)

# implement function which checks greeting
def check(g):
    pay_list = ["$0", "$20", "$100"]

# output $0 if the greeting contains "hello"
    if "hello" in g:
        print(pay_list[0])

# output $20 if the greeting startswith "h" but not "hello"
    elif g.startswith("h"):
        print(pay_list[1])

# output $100 if it's other greeting

main()