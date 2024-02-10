# import external libraries needed
import random
# define constants
guess_cont = True

def main():
    # loop to find the level
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl > 0:
                break
            else:
                pass
        except ValueError:
            continue
    # find a random number to find
    win = random.randint(1, lvl)
    # play the game
    while guess_cont:
        try:
            guess = int(input("Guess: "))
            if guess == win:
                print("Just right!")
                break
            elif guess > win:
                print("Too large!")
            else:
                print("Too small!")

        except ValueError:
            continue


if __name__ == "__main__":
    main()
