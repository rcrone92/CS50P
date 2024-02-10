from numb3rs import validate

def main():
    test_base()

def test_base():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("125.253.55.65") == True

def test_more():
    assert validate("256.256.255.255") == False


def test_less():
    assert validate("0") == False


def test_str():
    assert validate("cat") == False


def test_firstb():
    assert validate("512.512.512.512") == False

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("1.2.3.4") == True
    assert validate("11.99.22.88") == True
    assert validate("199.911.288.882") == False
    assert validate("249.249.249.249") == True


if __name__ == "__main__":
    main()

