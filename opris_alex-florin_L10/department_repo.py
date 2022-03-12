from domain.departments import Department
from domain.patients import Patient
from infrastructure.patient_repo import PatientRepository
from utils.SearchSortOp import mySort
from utils.SearchSortOp import mySearch
from utils.sorts import selection_sort

class DepartmentRepository:

    def __init__(self, dep_list, patient_repo: PatientRepository):
        self.__dep_list = dep_list
        self.__patient_repo = patient_repo

    def __len__(self):
        return len(self.__dep_list)

    def get_departments(self):
        """
        Returns all departments
        """
        return self.__dep_list

    def add_department(self, d):
        """
        Adds a new department
        :param d: the new department
        """
        ok = 1
        for i in range(0, len(self.__dep_list)):
            if self.__dep_list[i].get_id() == d.get_id():
                ok = 0

        if ok == 1:
            self.__dep_list.append(d)
        else:
            raise ValueError("Id already used!")

    def update_department(self, i, id, name, nr_beds, list_patients):
        """
        Updates a department at a given index
        :param i: the given index
        :param id: the new id
        :param name: the new name
        :param nr_beds: the new number of beds
        :param list_patients: the new list of patients
        """
        if i < 0 or i >= len(self.__dep_list):
            raise IndexError("Index not available")
        else:
            k = 1
            for i in range(0, len(self.__dep_list)):
                if self.__dep_list[i].get_id() == id:
                    k = 0
            if k == 0:
                raise ValueError("Id already used")
            else:
                self.__dep_list[i].set_id(id)
                self.__dep_list[i].set_name(name)
                self.__dep_list[i].set_nr_beds(nr_beds)
                self.__dep_list[i].set_list_patients(list_patients)


    def delete_department(self, i):
        """
        Deletes a department at a given index
        :param i: the given index
        """
        if i < 0 or i >= len(self.__dep_list):
            raise IndexError("Index not available")
        else:
            del self.__dep_list[i]

    def sort_patients_by_code(self):
        """
        Sorts the list of patients from the department by their code
        """
        mySort(self.__patient_repo, lambda x, y: x.get_personal_code() < y.get_personal_code())

    def sort_by_nr_patients(self):
        """
        Sorts the departments by the number of beds
        """
        mySort(self.__dep_list, lambda x, y: x.get_nr_patients() < y.get_nr_patients())

    def sort_patients_by_age(self):
        """
        Sorts the list of patients from a department by age
        """
        mySort(self.__patient_repo, lambda x, y: x.get_age() < y.get_age())

    def sort_dep_by_age_limit(self, a):
        """
        Sorts the list of departments by number of patients having an age limit
        """
        mySort(self.__dep_list, lambda x, y: x.get_patients_with_age_limit(a) < y.get_patients_with_age_limit(a))

    def sort_patients_alphabetically(self):
        """
        Sorts the patients from the department alphabetically
        """
        mySort(self.__patient_repo, lambda x, y: x.get_full_name() < y.get_full_name())

    def search_departments_with_patients_under_age(self, a):
        """
        Identifies the departments having patients under a given limit
        """
        return mySearch(self.__patient_repo, lambda x: x.getAge() < a)

    def search_patients_with_given_string(self, i, s):
        """
        Identifies the patients from a given department with name containing a given string
        :param i: the index of the department
        :param s: the given string
        """
        return mySearch(self.__dep_list[i], lambda x: x.get_full_name.find(s))

    def get_patients_with_name(self, name):
        """
        Identifies the departments which contain patietns with a given name
        :param name: the given name
        """
        l = []
        for i in range(len(self.__dep_list)):
            if self.__patient_repo.verify_patients_with_name(name) == 1:
                l.append(self.__dep_list[i])
        return l







