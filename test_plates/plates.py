# import external libraries needed
import re
# define global variables

def main():
    plate = input("Plate: ")
    if plate:
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if (leng(s) and first_sec(s) and no_punc(s) and num_seq(s)):
        return True
    else:
        return False

def first_sec(s):
    if (s[0].isalpha() and s[1].isalpha()):
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
        if not char.isalnum():
            return False
    return True

if __name__ == "__main__":
    main()
