def main():
    in_str = input("Enter a string: ")
    fin_str = ""
    str_split = in_str.split(" ")
    #print(in_str.split(" "))
    #print(str_split)
    #print(len(in_str.split(" ")))

    for i in range(len(str_split)):
        if str_split[i] == ":)":
            str_split[i] = "🙂"
        elif str_split[i] == ":(":
            str_split[i] = "🙁"

        fin_str = fin_str + " " + str_split[i]

    #print(str_split)
    #print(fin_str)
    return fin_str

if __name__ == "__main__":
    print(main())
