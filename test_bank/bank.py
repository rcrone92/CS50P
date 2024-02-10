# import external libraries needed
# define global variables


def main():
    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting):
    if greeting.strip().upper()[0:5] == "HELLO":
        return "$0"
    elif greeting.strip().upper()[0] == "H":
        return "$20"
    else:
        return "$100"
    

if __name__ == "__main__":
    main()
