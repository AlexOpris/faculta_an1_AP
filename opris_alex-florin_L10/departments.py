from domain.patients import Patient
from infrastructure.patient_repo import PatientRepository

class Department:
    """
    A department has an id, a name, a number of beds and a list of patients
    """
    def __init__(self, id = 0, name = "", nr_beds = 0, list_patients = []):
        """
        :param id: the id of the department
        :param name: the name of the department
        :param nr_beds: the numbers of beds
        :param list_patients: the list of patients
        """
        self.__id = id
        self.__name = name
        if nr_beds < 0:
            raise ValueError("Number of beds must be possitive")
        else:
            self.__nr_beds = nr_beds
        self.__list_patients = list_patients

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_nr_beds(self):
        return self.__nr_beds

    def set_nr_beds(self, nr_beds):
        if nr_beds < 0:
            raise ValueError("Number of beds must be possitive")
        else:
            self.__nr_beds = nr_beds

    def get_list_patients(self):
        return self.__list_patients

    def set_list_patients(self, list_patients):
        self.__list_patients = list_patients

    def get_nr_patients(self):
        return len(self.__list_patients)

    def __str__(self):
        return "The department " + self.__name + " with id " + str(self.__id) + " has " + str(self.__nr_beds) + " beds and the patients are: " + str(self.__list_patients)

    def delete_patient_at_index(self, index):
        l = self.get_list_patients()
        del l[index]
        self.set_list_patients(l)

    def update_patient_at_index(self, index, first_name, last_name, code, disease):
        l = self.get_list_patients()
        l[index].set_first_name(first_name)
        l[index].set_last_name(last_name)
        l[index].set_personal_code(code)
        l[index].set_disease(disease)

    def get_patient_at_index(self, index):
        l = self.get_list_patients()
        return l[index]


    def get_patients_with_age_limit(self, a):
        """
        Gives the number of patients having the age over a given limit
        :param a: the age limit
        :return: the number of patients
        """
        k = 0
        for i in range(0, len(self.__list_patients)):
            if self.__list_patients[i].get_age() > a:
                k += 1
        return k

