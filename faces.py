#Define main fuction, get input from user

def main():
    frase = input("Input frase with 🙂 or 🙁: ")
    convert(frase)
    

#define convert fuction

def convert(n):
    n = n.replace(":)", "🙂").replace(":(", "🙁")
    print(n)
    


main()

