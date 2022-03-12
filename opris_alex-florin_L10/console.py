from domain.patients import Patient
from domain.departments import Department
from infrastructure.patient_repo import PatientRepository
from infrastructure.department_repo import DepartmentRepository

class UI:

    def __init__(self, controller):
        self.__controller = controller

    @staticmethod
    def print_menu():
        print("0 - Exit")
        print("1 - Add a new department")
        print("2 - Get all departments")
        print("3 - Sort patients by their personal code")
        print("4 - Sort departments by the number of patients")
        print("5 - Sort departments by number of patients over an age limit")
        print("6 - Sort departments by the number of patients and patients alphabetically ")
        print("7 - Identify departments with patients under a given age")
        print("8 - Identify patients from a department for which the first name or last name contain a given string")
        print("9 - Identify departments where there are patients with a given first name")
        print("10 - Form groups of k patients from the same department and the same disease")
        print("11 - Form groups of k departments having at most p patients suffering from the same disease")

    @staticmethod
    def read_list_patients():

        l = []
        nr = int(input("Introduce number of patients:  "))
        for i in range(0, nr):
            print("Patient ", i+1, ": ")
            name1 = input("Introduce first name: ")
            name2 = input("Introduce second name: ")
            code = int(input("Introduce personal code: "))
            disease = input("Introduce disease: ")
            a = Patient(name1, name2, code, disease)
            l.append(a)
        return l

    @staticmethod
    def read_department():

        id = int(input("Introduce ID: "))
        name = input("Introduce name: ")
        beds= int(input("Introduce number of beds: "))
        l = UI.read_list_patients()
        d = Department(id, name, beds, l)
        return d

    def add_data(self):
        self.__controller.add(Department(32, "ENT", 10, [Patient("Smith", "James", 4932111990, "Ear ache"), Patient("Jones", "Karen", 9325121980, "Head ache")]))
        self.__controller.add(Department(77, "Cardiology", 6, [Patient("Williams", "Aaron", 5325321961, "Hearth attack")]))
        self.__controller.add(Department(91, "Neurology", 12, [Patient("Brown", "Emma", 9312232003, "Alzheimer"), Patient("Murphy", "Richard", 5423441998, "Schizophrenia"), Patient("Walsh", "Richard", 2342301967, "Alzheimer")]))


    def start(self):

        self.add_data()
        UI.print_menu()
        opt = ""
        while opt != "0":
            try:
                opt = input("Introduce option: ")
                if opt == "1":

                    d = UI.read_department()
                    self.__controller.add(d)

                elif opt == "2":

                    self.__controller.print_all_departments()

                elif opt == "3":

                    self.__controller.sort_by_code()

                elif opt == "4":

                    self.__controller.sort_by_patients()

                elif opt == "5":

                    a = int(input("Introduce the age limit: "))
                    self.__controller.sort_dep_by_patients_with_age_limit(a)

                elif opt == "6":

                    self.__controller.sort_by_patients()
                    self.__controller.sort_pat_alphabetically()

                elif opt == "7":

                    a = int(input("Introduce age limit: "))
                    p = self.__controller.get_deps_with_pats_under_age(a)
                    print(p)

                elif opt == "8":

                    i = int(input("Introduce the number of the department: "))
                    s = input("Introduce string: ")
                    p = self.__controller.get_patients_with_given_string(i, s)
                    print(p)

                elif opt =="9":

                    n = input("Introduce name: ")
                    l = self.__controller.get_deps_with_patients_with_name(n)
                    for i in range(len(l)):
                        print(l[i])

                elif opt == "10":
                    pass

                elif opt == "11":
                    pass

                elif opt == "0":

                    print("Exit")

                else:

                    print("Invalid value, try again")

            except IndexError as ie:
                print("Error:", ie)
            except AttributeError as ae:
                print("Error:", ae)
            except ValueError as ve:
                print("Error:", ve)
