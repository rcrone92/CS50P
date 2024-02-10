import re
date = input("K: ")
pattern = r'^[A-Z][a-z]+\s[0-9]{1,2},\s[0-9]{4}$'


if re.match(pattern, date):
    print("true")

date = date.replace(",", "")
print(date)
