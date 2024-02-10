def main():
    while True:
        try:
            frac_str = input("Fraction: ")
            num_str, den_str = frac_str.split("/")
            num = int(num_str)
            den = int(den_str)
            fuel_lvl = num / den
            if is_float(fuel_lvl):
                if 0 <= fuel_lvl <= 1:
                    break
                else:
                    print("Try again.")
        except ValueError:
            print("Try again.")
        except ZeroDivisionError:
            print("Try again.")


    if 0 <= fuel_lvl < .02:
        print("E")
    elif .01 < fuel_lvl < .98:
        percent = int(float(format((float(num / den)), '.2f')) * 100)
        print(f'{percent}%')
    else:
        print("F")


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()
"""
nu = 4
de = 10
print(float(2/3))
print(float(2/3) * 100)
print(int(float(2/3) * 100))
print(format((float(2/3)), '.2f'))
print(float(nu / de) * 100)
print(format((float(nu / de)), '.2f'))
fin = int(float(format((float(nu / de)), '.2f')) * 100)
print(fin)"""
