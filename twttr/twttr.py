def main():
    inp = input("Input: ")
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    outp = ""
    for char in inp:
        if char in vowels:
            pass
        else:
            outp = outp + char

    print("Output: " + outp)

if __name__ == "__main__":
    main()
