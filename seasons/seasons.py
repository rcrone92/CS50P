# import external libraries needed
from datetime import date
import sys
import inflect
# define global variables


def main():
    try:
        dateOfBirth = input("Date of Birth: ")
        timePeriod = date.today() - date.fromisoformat(dateOfBirth)
        days = timePeriod.days
        print(daysToMins_numbersToWords(days))

    except:
        sys.exit("Invalid input format")


def daysToMins_numbersToWords(days):
    minutes = int(days) * 24 * 60
    p = inflect.engine()
    return f"{p.number_to_words(minutes, andword="").capitalize()} minutes"


if __name__ == "__main__":
    main()
