# import external libraries needed
from twttr import shorten
# define global variables

def main():
    test_single()
    test_sentence()
    test_no_vowels()


def test_single():
    assert shorten("Twitter") == "Twttr"

def test_sentence():
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_no_vowels():
    assert shorten("CS50") == "CS50"

def test_uppers():
    assert shorten("Up") == "p"


if __name__ == "__main__":
    main()
