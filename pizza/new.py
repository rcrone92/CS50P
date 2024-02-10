import csv
from tabulate import tabulate
"""
# check for right amount of arguments
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

# assign filepath a variable
file_path = sys.argv[1]

# check for .py file
if not check_file_valid(file_path):
    sys.exit("Not a CSV file.")

# check if openable
if not check_file_openable(file_path):
    sys.exit("File does not exist.")
"""

menus = []
file = "/workspaces/143379034/pizza/regular.csv"
with open(file) as f:
    reader = csv.reader(f)
    table = tabulate(reader, headers="firstrow", tablefmt="grid")
# print(menus)

# print(menus[0])

#table = tabulate(menus, tablefmt="grid")
print(table)
