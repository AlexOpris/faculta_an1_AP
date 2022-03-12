import functions

def print_menu():

    print("0 - Exit")
    print("1 - Compute the greatest common divisor of 2 given numbers")
    print("2 - Compute the given power of a given number")


def start():

    print_menu()
    opt = ''
    while opt != "0":
        try:
            opt = input("Introduce option: ")
            if opt == "1":

                a = int(input("Introduce the first number: "))
                b = int(input("Introduce the second number: "))
                print(functions.gcd(a, b))

            elif opt == "2":

                a = int(input("Introduce the number: "))
                x = int(input("Introduce the power:"))
                print(functions.power(a, x))

            elif opt == "0":

                print("Exit...")

            else:

                print("Invalid value, try again")

        except ValueError as er:
            print("Error:", er)
