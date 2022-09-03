#Define main fuction, get input from user

def main():
    frase = input("Input frase with 🙂 or 🙁: ")
    convert(frase)
    

#Define convert fuction

def convert(n):
    n = n.replace(":)", "🙂").replace(":(", "🙁")
    print(n)
    

main()

