# import external libraries needed
import sys
import requests
# import json
# define global variables

# main program
def main():
    # check to see if there are the right amount of and type of argv
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        try:
            arg_float = float(sys.argv[1])
            response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
            o = response.json()
            usd_price = o["bpi"]["USD"]["rate_float"]
            am = arg_float * usd_price
            am = "${:,.4f}".format(am)
            print(f"{am}")
        except ValueError:
            sys.exit("Command-line argument is not a number")


if __name__ == "__main__":
    main()
