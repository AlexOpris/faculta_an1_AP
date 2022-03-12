import functions
import tests


def print_menu():
    print("Press 1 to add a value")
    print("Press 2 to insert a value")
    print("Press 3 to remove a value")
    print("Press 4 to remove values from a to b")
    print("Press 5 to replace a value")
    print("Press 6 to see properties of participants")
    print("Press 7 to see characteristics")
    print("Press 8 to filter the scores which are multiples of n")
    print("Press 9 to filter the scores which are higher than n")
    print("Press 10 to undo the last operation")
    print("Press 0 to exit")

def showList(l):
    """
    Display the list on the screen.
    Input: 1 - alist of numbers
    """

    s = ""
    for elem in l:
        s += str(elem) + " "
    print(s)


def start():

    my_list = [4,52,77,34,51,22,63,100]
    old_list = my_list[:]
    print("Start")
    option = ""
    while option != "0":
        print_menu()
        option = input("Enter command:")
        if option == "1":
            old_list = my_list[:]
            elem = int(input("Enter the value you want to add:"))
            functions.add_value(my_list, elem)
            showList(my_list)
        elif option == "2":
            old_list = my_list[:]
            x = int(input("Enter the value you want to add:"))
            index = int(input("Enter the position you want to add the value:"))
            functions.insert_value(my_list, x, index)
            showList(my_list)
        elif option == "3":
            old_list = my_list[:]
            index = int(input("Enter the position of the value you want to remove:"))
            functions.remove_value(my_list, index)
            showList(my_list)
        elif option == "4":
            old_list = my_list[:]
            a = int(input("Enter the position you want to begin:"))
            b = int(input("Enter the position you want to end:"))
            functions.remove_from_a_to_b(my_list,a,b)
            showList(my_list)
        elif option == "5":
            old_list = my_list[:]
            x = int(input("Enter the number you want to replace:"))
            index = int(input("Enter the position of the number you want to replace:"))
            functions.replace_value(my_list, x, index)
            showList(my_list)
        elif option == "6":
            old_list = my_list[:]
            print("Participants with scores less than n:")
            n = int(input("Introduce n:"))
            functions.print_less_n(my_list,n)
            print("Participants with scores greater than m:")
            m = int(input("Introduce m:"))
            functions.print_greater_n(my_list,m)
            print("Participants sorted:")
            functions.print_sorted(my_list)
        elif option == "7":
            old_list = my_list[:]
            print("Introduce interval values")
            a = int(input("First participant:"))
            b = int(input("Last participant:"))
            print("The avarage of these participants is:")
            functions.print_average(my_list, a, b)
            print("The minimum of these scores is:")
            functions.print_minimum(my_list, a, b)
            print("Scores which are multiples of 10:")
            functions.print_mul_10(my_list,a,b)
        elif option == "8":
            old_list = my_list[:]
            n = int(input("Introduce n:"))
            print("Scores multiples of n:")
            functions.filter_mul_n(my_list,n)
            showList(my_list)
        elif option == "9":
            old_list = my_list[:]
            n = int(input("Introduce n:"))
            print("Scores higher than n:")
            functions.filter_higher_n(my_list,n)
            showList(my_list)
        elif option == "10":
            print("Operation undone")
            my_list = old_list[:]
            showList(my_list)
        elif option == "0":
            print("Exit...")
        else:
            print("Option doesn't exist")


tests.test_all()
start()



