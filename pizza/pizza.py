# import necessary libraries
import sys, csv
from tabulate import tabulate

# define the main function
def main():
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

    # convert csv into a usable format for tabulate
    data = convert_csv(file_path)

    # tabulate the table and print
    print(data)


# define a function for openable
def check_file_openable(file_path):
    try:
        with open(file_path, "r"):
            pass
        return True
    except FileNotFoundError:
        return False


# check for .py file
def check_file_valid(file_path):
    return file_path.endswith(".csv")

# function to extract csv data and formulate into tabulate usable form
def convert_csv(file_path):
    with open(file_path) as f:
        reader = csv.reader(f)
        table = tabulate(reader, headers="firstrow", tablefmt="grid")
    return table


# call main() using proper notation
if __name__ == "__main__":
    main()
