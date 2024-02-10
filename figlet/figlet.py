from pyfiglet import Figlet
import random
import sys
import pyfiglet

def main():
    try:
        # phrase = input("Input: ")
        # print with two argv
        if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
            f = Figlet(font=sys.argv[2])
            phrase = input("Input: ")
            print(f.renderText(phrase))
            # print("if")
            # print with no argv
        elif len(sys.argv) == 1:
            fig = Figlet()
            av_fonts = fig.getFonts()
            ran_font = random.choice(av_fonts)
            f = Figlet(font=ran_font)
            phrase = input("Input: ")
            print(f.renderText(phrase))
            # print("elif")
        # catch any corner cases
        else:
            sys.exit("Invalid Usage")
    # catch IndexErrors and FontNotFound cases
    except IndexError:
        sys.exit("Invalid Usage")
    except pyfiglet.FontNotFound as e:
        sys.exit("Invalid Usage")

if __name__ == "__main__":
    main()
