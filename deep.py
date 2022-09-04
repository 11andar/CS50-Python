def main():
    # get input from user
    answear = input("What's the answear? ").lower()
    check(answear)

# implement 'check' function
def check(a):
    a_list = ["42", "forty-two", "forty two"]
    
    # output "yes" if the answear is "42" "forty-two" or "forty two"
    if a == a_list[0]:
        print("Yes")
    elif a == a_list[1]:
        print("Yes")
    elif a == a_list[2]:
        print("Yes")
    
    # else output "no"

main()