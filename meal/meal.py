def main():
    cur = input("What time is it? ")
    con = convert(cur)
    if 7.0 <= con <= 8.0:
        print("breakfast time")
    elif 12.0 <= con <= 13.0:
        print("lunch time")
    elif 18.0 <= con <= 19.0:
        print("dinner time")


def convert(time):
    clean = time.lower().strip()
    if clean.endswith("p.m."):
        clean = clean.split(" ")[0]
        if clean.split(":")[0] == "12":
            hour = float(clean.split(":")[0])
        else:
            hour = float(clean.split(":")[0]) + 12
        mins = float(clean.split(":")[1]) / 60
    elif clean.endswith("a.m."):
        clean = clean.split(" ")[0]
        hour = float(clean.split(":")[0])
        mins = float(clean.split(":")[1]) / 60
    else:
        hour = float(time.split(":")[0])
        mins = float(time.split(":")[1]) / 60
    #print(clean)
    #print(hour + mins)
    return hour + mins


# main()
if __name__ == "__main__":
    main()
