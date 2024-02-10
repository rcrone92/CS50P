def main ():
    ans = input("What is the Answer to the Great Question of life, the Univers, and Everything? ")
    match ans.upper().strip():
        case "FORTY TWO" | "FORTY-TWO" | "42" | "FORTYTWO":
            return "Yes"
        case _:
            return "No"

print(main())
