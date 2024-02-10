from um import count

def main():
    test_works()

def test_works():
    assert count("um") == 1
    assert count("number") == 0
    assert count("um, hello, um hi") == 2
    assert count("UM, um, uM, number") == 3

if __name__ == "__main__":
    main()
