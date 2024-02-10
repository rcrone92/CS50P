# import external libraries needed
# define constants
names = []
out_str = ""

def main():
    # get the list of names until EOF
    while True:
        try:
            name = input("Name: ").strip()
            names.append(name)
        # break out of loop with EOFError
        except EOFError:
            break
    # print out the names in the prescribed
    if len(names) == 1:
        farewell = "Adieu, adieu, to " + names[0]
    elif len(names) == 2:
        farewell = "Adieu, adieu, to " + " and ".join(names)
    else:
        farewell = "Adieu, adieu, to " + ", ".join(names[:-1]) + ", and " + names[-1]

    print("\n" + farewell)


if __name__ == "__main__":
    main()
