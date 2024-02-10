# import external libraries needed
from plates import is_valid
# define global variables


def test_valid():
    assert is_valid("RJ50") == True

def test_0_first():
    assert is_valid("RJ05") == False

def test_letter_last():
    assert is_valid("RJ50P") == False

def test_punctuation():
    assert is_valid("RJ10.1") == False

def test_single():
    assert is_valid("R") == False

def test_too_long():
    assert is_valid("WHYISTHIS") == False

def test_start():
    assert is_valid("1GUY") == False

def test_AA():
    assert is_valid("AA") == True

def test_A2():
    assert is_valid("A2") == False

def test_2A():
    assert is_valid("2A") == False

def test_22():
    assert is_valid("22") == False

def test_2():
    assert is_valid("2") == False
