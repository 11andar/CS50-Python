def main():
    frase = input("Frase: ")
    slow(frase)

def slow(n):
    n = n.replace(" ", "...")
    print(f"{n}")

main()


