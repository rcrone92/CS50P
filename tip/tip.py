def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    d_final = ""
    for char in d:
        if char.isalnum() or char == '.':
            d_final += char
        else:
            continue
    # print(d_final)
    return float(d_final)



def percent_to_float(p):
    # TODO
    p_final = ""
    for char in p:
        if char.isalnum() or char == '.':
            p_final += char
        else:
            continue
    # print(p_final)
    return float(p_final) / 100.0


if __name__ == "__main__":
    main()
