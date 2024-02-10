# import libraries
# define global constants

def main():
    while True:
        frac = input("Fraction: ")
        percent = convert(frac)
        if isinstance(percent, int):
            break
        else:
            pass

    print(gauge(percent))


def convert(fraction):
    try:
        x = int(fraction.strip().split("/")[0])
        y = int(fraction.strip().split("/")[1])
        z = float(x / y)
        if (x > y) or 0 > (x / y) < 1:
            raise ValueError
        return round(z * 100)
    except ValueError:
        return "Try again."
    except ZeroDivisionError:
        return "Try again."


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
