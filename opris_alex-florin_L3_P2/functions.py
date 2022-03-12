def add_value(l,a):
    """
    Adds a value to the end of the list
    :param l: the given list
    :param a: element to add
    """

    if a < 0 or a > 100:
        print("Invalid value")
    else:
        l.append(a)

def insert_value(l, x, index):
    """
    Inserts a chosen value on a chosen position from the list
    :param l: the given list
    :param x: element to replace
    :param index: index
    """

    if x < 0 or x > 100:
        print("Invalid value")
    else:
        l.insert(index, x)

def remove_value(l, index):
    """
    Removes a value from a chosen position from the list
    :param l: the given list
    :param index: index
    """

    if index >= len(l):
        print("Position doesn't exist")
    else:
        l.pop(index)

def remove_from_a_to_b(l,a,b):
    """
    Removes all elements from the list from a chosen interval
    :param l: the given list
    :param a: start of interval
    :param b: end of interval
    """

    if a < 0 or b > len(l):
        print("Invalid interval")
    else:
        for i in range(a,b+1):
            l.pop(a)

def replace_value(l,x,index):
    """
    Replaces a value from a chosen index from the list
    :param l: the given list
    :param x: value to replace with
    :param index: index
    """

    if x < 0 or x > 100:
        print("Invalid value")
    elif index >= len(l):
        print("Position doesn't exist")
    else:
        l[index] = x

def print_less_n(l,n):
    """
    Prints all the elements less than 40
    :param l: the given list
    """

    for i in range(len(l)):
        if(l[i] < n):
            print(i," ")

def print_greater_n(l,n):
    """
    Prints all the elements greater than 90
    :param l: the given list
    """

    for i in range(len(l)):
        if l[i] > n:
            print(i," ")

def print_sorted(l):
    """
    Prints the list sorted
    :param l: the given list
    """

    if l == []:
        print("Emplty list")
    else:
        copy_list = l[:]
        for i in range(0,len(l)):
            mini = 100000
            k = 0
            for j in range(0,len(l)):
                if copy_list[j] < mini:
                    mini = l[j]
                    k = j
            print(k)
            copy_list[k] = 100000



def print_average(l,a,b):
    """
    Prints the average from a chosen interval
    :param l: the given list
    :param a: start of interval
    :param b: end of interval
    """
    if l == []:
        print("Empty list")
    elif a < 0 or b >= len(l) or a > b:
        print("Interval not available")
    else:
        avg = 0
        for i in range(a,b+1):
            avg = avg + l[i]
        avg = avg / (b + 1 - a)
        print(avg)

def print_minimum(l,a,b):
    """
    Prints the minimum from a chosen interval
    :param l: the given list
    :param a: start of interval
    :param b: end of interval
    """
    if l == []:
        print("Empty list")
    elif a < 0 or b >= len(l) or a > b:
        print("Interval not available")
    else:
        mini = 10000
        for i in range(a, b + 1):
            if l[i] < mini:
                mini = l[i]
        print(mini)

def print_mul_10(l,a,b):
    """
    Prints the elements which are multiples of 10
    :param l: the given list
    :param a: start of interval
    :param b: end of interval
    """
    if l == []:
        print("Empty list")
    elif a < 0 or b >= len(l) or a > b:
        print("Interval not available")
    else:
        for i in range(a, b + 1):
            if l[i] % 10 == 0:
                print(l[i])

def filter_mul_n(l, n):
    """
    Filters the scores which are multiples of n
    :param l: the given list
    """

    for i in range(len(l)-1,-1,-1):
        if l[i] % n != 0:
            del l[i]


def filter_higher_n(l,n):
    """
    Filters the scores which are higher than n
    :param l: the given list
    """

    for i in range(len(l) - 1, -1, -1):
        if l[i] < n:
            del l[i]

def undo(l,ol):
    l = ol[:]

def readFromFile(l):
    try:
        fin = open("input.txt", "r")
        for line in fin:
            nr = int(line)
            l.append(nr)
        fin.close()
    except IOError as ex:
        print("Reading file error", ex)

def writeInFile(l):
    try:
        fout = open("output.txt", "w")
        for i in l:
            fout.write(str(i))
            fout.write(" ")
        fout.close()
    except IOError as ex:
        print("Reading file error", ex)