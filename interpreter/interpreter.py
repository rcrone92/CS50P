def main():
    expression = input("Expression: ")
    x = float(expression.split(" ")[0])
    y = expression.split(" ")[1]
    z = float(expression.split(" ")[2])
    if y == "+":
        return float(x + z)
    elif y == "-":
        return float(x - z)
    elif y == "*":
        return float(x * z)
    elif y == "/":
        return float(x / z)

if __name__ =="__main__":
    print(main())
