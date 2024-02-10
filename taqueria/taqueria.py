def main():
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
    "": None
    }
    total = 0.0
    while True:
        # order = input("Item: ")
        # print(menu['Burger'])
        #if not order:
        #    con = False
        try:
            order = input("Item: ").title()
            total = total + menu[order]
            tot_out = format(total, '.2f')
            print(f'Total: ${tot_out}')
        except KeyError:
            pass
        except EOFError:
            break
    # print("Total")

if __name__ == "__main__":
    main()
