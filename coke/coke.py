def main():
    am_due = 50
    coin_in = 0
    # print("Amount Due: " + am_due)
    while am_due > 0:
        print(f"Amount Due: {am_due}")
        coin_in = input("Insert Coin: ")
        if coin_in == "25" or coin_in == "10" or coin_in == "5":
            am_due = am_due - int(coin_in)
            # print(am_due)
        else:
            pass
    change = abs(am_due)
    print(f"Change Owed: {change}")


main()
