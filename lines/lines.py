# import necessary libraries
import sys

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    file_path = sys.argv[1]

    if not check_file_valid(file_path):
        sys.exit("Not a Python file.")

    if not check_file_openable(file_path):
        sys.exit("File does not exist.")

    print(count_lines(file_path))
    # print("main")


def check_file_valid(file_path):
    return file_path.endswith(".py")


def check_file_openable(file_path):
    try:
        with open(file_path, "r"):
            pass
        return True
    except FileNotFoundError:
        return False


def count_lines(file_path):
    count = 0
    with open(file_path, "r") as file:
        for line in file:
            if not line.strip().startswith("#") and line.strip():
                count += 1
    return count


if __name__ == "__main__":
    main()
