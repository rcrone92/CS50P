import re

# define constants
months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
}
# patterns to match to
pattern = r'^[0-9]+[/]+[0-9]+[/]+[0-9]*$'
pattern1 = r'^[A-Z][a-z]+\s[0-9]{1,2},\s[0-9]{4}$'  # Corrected pattern

# define the main function
def main():
    # loop until an acceptable date form is given
    while True:
        date = input("Date: ").strip()
        # format for the first pattern x/x/xxxx
        if re.match(pattern, date):
            date = date.split("/")
            if 0 < int(date[0]) <= 12 and 0 < int(date[1]) <= 31 and 0 < int(date[2]) <= 9999:
                print(date[2].zfill(2) + "-" + date[0].zfill(2) + "-" + date[1].zfill(2))
                break
        # format for the second pattern month, x, xxxx
        elif re.match(pattern1, date):
            date = date.replace(",", "")
            month, day, year = date.split()
            if month in months and 0 < int(day) <= 31 and 0 < int(year) <= 9999:
                month = months[month]
                print(str(year).zfill(2) + "-" + str(month).zfill(2) + "-" + str(day).zfill(2))
                break

if __name__ == "__main__":
    main()
