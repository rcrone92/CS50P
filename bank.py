def main():
    greet = input("Greeting: ")
    # print(greet[0:5])
    if greet.strip().upper()[0:5] == "HELLO":
        print("$0")
    elif greet.strip().upper()[0] == "H":
        print("$20")
    else:
        print("$100")

main()
