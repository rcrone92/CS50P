# import external libraries needed
from seasons import daysToMins_numbersToWords
# define global variables


def main():
    print(numbersToWords(10477))
    test_works()


def test_works():
    assert daysToMins_numbersToWords(10477) == "Fifteen million, eighty-six thousand, eight hundred eighty minutes"
    assert daysToMins_numbersToWords(365) == "Five hundred twenty-five thousand, six hundred minutes"

if __name__ == "__main__":
    main()
