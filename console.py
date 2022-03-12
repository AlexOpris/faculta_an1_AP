from domain.vector import MyVector
from infrastructure.repo import VectorRepository

class VectorUI:

    def __init__(self, controller):
        self.__controller = controller

    @staticmethod
    def printMenu():
        """
        Print the menu of the application
        """
        print("0 - Exit")
        print("1 - Add a new vector")
        print("2 - Get all vectors")
        print("3 - Get a vector at a given index")
        print("4 - Update vector at index")
        print("5 - Update vector by name_id")
        print("6 - Delete vector at index")
        print("7 - Delete vector by name_id")
        print("8 - Plot all vectors in a chart")
        print("9 - Update the colour of a vector identified by name_id")
        print("10 - Delete all vectors for which the max value is equal to a given value")

    def printAllVectors(self):
        """
        Prints all the vectors from the list
        """
        self.__controller.print_all_vectors()

    @staticmethod
    def readVector():
        """
        Reads a vector
        """
        v = []
        id = int(input("Introduce id:"))
        colour = input("Introduce colour from list: r, g, b, y, m:")
        t = int(input("Introduce type:"))
        i = int(input("Introduce the number of values:"))
        for j in range(0, i):
            a = int(input("Introduce value:"))
            v.append(a)
        return MyVector(id, colour, t, v)

    def start(self):

        VectorUI.printMenu()
        option = ""
        while option != "0":
            try:
                option = input("Select option: ")
                if option == "1":
                    x = VectorUI.readVector()
                    self.__controller.add(x)

                elif option == "2":
                    self.printAllVectors()

                elif option == "3":
                    i = int(input("Introduce index: "))
                    x = self.__controller.get_vector_at_index(i)
                    print(x)

                elif option == "4":
                    x = int(input("Introduce index: "))
                    colour = input("Introduce colour from list: r, g, b, y, m: ")
                    t = int(input("Introduce type: "))
                    i = int(input("Introduce the number of values: "))
                    v = []
                    for j in range(0, i):
                        a = int(input("Introduce value: "))
                        v.append(a)
                    self.__controller.update_vector_at_index(x, colour, t, v)

                elif option == "5":
                    id = int(input("Introduce id: "))
                    colour = input("Introduce colour from list: r, g, b, y, m: ")
                    t = int(input("Introduce type: "))
                    i = int(input("Introduce the number of values: "))
                    v = []
                    for j in range(0, i):
                        a = int(input("Introduce value: "))
                        v.append(a)
                    self.__controller.update_vector_by_id(id, colour, t, v)

                elif option == "6":
                    i = int(input("Introduce index: "))
                    self.__controller.delete_vector_at_index(i)

                elif option == "7":
                    i = int(input("Introduce ID: "))
                    self.__controller.delete_vector_by_id(i)

                elif option == "8":
                    self.__controller.plot_vectors()

                elif option == "9":
                    id = input("Introduce id: ")
                    c = input("Introduce new colour from list: r, g, b, y, m: ")
                    self.__controller.update_colour_by_name_id(id, c)

                elif option == "10":
                    mx = int(input("Introduce maximum value: "))
                    self.__controller.delete_vectors_with_max(mx)

                elif option == "0":
                    print("Exit")

                else:
                    print("Option doesn't exist, try again")

            except IndexError as ie:
                print("Error:", ie)
            except AttributeError as ae:
                print("Error:", ae)
            except ValueError as ve:
                print("Error:", ve)
