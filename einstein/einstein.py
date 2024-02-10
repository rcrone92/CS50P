def main ():
    m = input("Enter a mass: ")
    return formula(m)

def formula(mass):
    mass = int(mass)
    return int(mass * 300000000 * 300000000)

print(main())
