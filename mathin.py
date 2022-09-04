def main():
# prompt user for an arithmetic expression
    expression = input("Expression: ")

# assign values to variables x, y, z
    x,y,z = expression.split(" ")

# convert x and z into floats
    x = float(x)
    z = float(z)

# create lists of operators and mathematical operations
    operators = ["+", "-", "*", "/", "**", "%"]
    math_ops = [x + z, x - z, x * z, x / z, x ** z, x % z]
    error = "Unknown operation"

# output appropriate operations and their results
    if y == operators[0]:
        print(f"{x} + {z} = {math_ops[0]}")
    elif y == operators[1]:
        print(f"{x} - {z} = {math_ops[1]}")
    elif y == operators[2]:
        print(f"{x} * {z} = {math_ops[2]}")
    elif y == operators[3]:
        print(f"{x} / {z} = {math_ops[3]}")
    elif y == operators[4]:
        print(f"{x} ** {z} = {math_ops[4]}")
    elif y == operators[5]:
        print(f"{x} % {z} = {math_ops[5]}")
    else:
        print(error)
    

main() 