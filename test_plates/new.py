import re

def num_seq(s):
    pattern = r'^[A-Z]+[1-9]+[0-9]*$'
    pattern1 = r'^[A-Z]+$'
    if re.match(pattern, s) or re.match(pattern1, s):
        return True
    else:
        return False

x = input("X: ")

print(num_seq(x))
