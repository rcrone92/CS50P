def main():
    inp = input("Input: ")
    word = shorten(inp)
    print("Output: " + word)


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    outp = ""

    for char in word:
        if char in vowels:
            pass
        else:
            outp = outp + char

    return outp

if __name__ == "__main__":
    main()
