# import external libraries needed
import random
# define global variables


# Main game
def main():
    score = 0
    level = get_level()

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y

        for _ in range(3):
            ans = input(f"{x} + {y} = ")

            if ans == str(z):
                score += 1
                break
            else:
                print("EEE")

        if ans != str(z):
            print(f"{x} + {y} = {z}")

    print(f"Score: {score}")


# gets a level from 1-3
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


# randomly generates a non-negetive integer with level digits
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
