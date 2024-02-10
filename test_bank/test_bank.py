# import external libraries needed
from bank import value
# define global variables

def main():
    test_hello()
    test_h()
    test_else()
    test_punctuation()

def test_hello():
    assert value("hello") == "$0"
    assert value("Hello") == "$0"

def test_h():
    assert value("hey") == "$20"

def test_else():
    assert value("What's happening?") == "$100"

def test_punctuation():
    assert value("!!!") == "$100"


if __name__ == "__main__":
    main()
