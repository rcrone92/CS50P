# import necessary libraries
import sys, csv

def main():
    # check for right amount of arguments
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    # assign filepaths variables
    file_one = sys.argv[1]
    file_two = sys.argv[2]

    # check if it is a CSV file
    if not file_one.endswith(".csv") or not file_two.endswith(".csv"):
        sys.exit("Not a CSV file.")

    # check if it is
    try:
        with open(file_one, "r"):
            pass
    except FileNotFoundError:
        sys.exit("File does not exist.")

    rewrite_files(file_one, file_two)


def rewrite_files(f_one, f_two):
    with open(f_one) as f_one:
            reader = csv.DictReader(f_one)
            with open(f_two, "w") as f_two:
                header = ["first", "last", "house"]
                writer = csv.DictWriter(f_two, fieldnames = header)
                writer.writeheader()
                for student in reader:
                    last, first = student["name"].split(", ")
                    house = student["house"]
                    writer.writerow({"first": first, "last": last, "house": house})



if __name__ == "__main__":
    main()
