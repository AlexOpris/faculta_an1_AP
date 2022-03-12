from domain.departments import Department
from infrastructure.department_repo import DepartmentRepository

class Controller:

    def __init__(self, dep_repo: DepartmentRepository):
        self.__dep_repo = dep_repo

    def add(self, dep: Department):
        self.__dep_repo.add_department(dep)

    def print_all_departments(self):
        for i in self.__dep_repo.get_departments():
            print(i)

    def sort_by_code(self):
        self.__dep_repo.sort_patients_by_code()

    def sort_by_patients(self):
        self.__dep_repo.sort_by_nr_patients()

    def sort_by_age(self):
        self.__dep_repo.sort_patients_by_age()

    def sort_dep_by_patients_with_age_limit(self, a):
        self.__dep_repo.sort_dep_by_age_limit(a)

    def sort_pat_alphabetically(self):
        self.__dep_repo.sort_patients_alphabetically()

    def get_deps_with_pats_under_age(self,a ):
        return self.__dep_repo.search_departments_with_patients_under_age(a)

    def get_patients_with_given_string(self, i, s):
        return self.__dep_repo.search_patients_with_given_string(i, s)

    def get_deps_with_patients_with_name(self, name):
        return self.__dep_repo.get_patients_with_name(name)