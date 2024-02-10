def main():
    items = {}
    while True:
        try:
            item = input().upper()
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
        except EOFError:
            break

    items = dict(sorted(items.items()))
    for item in items:
        print(str(items[item]) + " " + item)


if __name__ == "__main__":
    main()
