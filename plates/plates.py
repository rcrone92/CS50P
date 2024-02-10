import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if leng(s):
        if first_sec(s) and num_seq(s) and no_punc(s):
            return True
    else:
        return False

def first_sec(s):
    if s[0].isalpha() and s[1].isalpha():
        return True
    else:
        return False

def leng(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def num_seq(s):
    pattern = r'^[A-Z]+[1-9]+[0-9]*$'
    pattern1 = r'^[A-Z]+$'
    if re.match(pattern, s) or re.match(pattern1, s):
        return True
    else:
        return False

def no_punc(s):
    for char in s:
        if char.isalnum():
            return True
        else:
            return False


if __name__== "__main__":
    main()
