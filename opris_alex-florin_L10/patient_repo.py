from domain.patients import Patient

class PatientRepository:

    def __init__(self, patient_list):
        self.__patient_list = patient_list

    def __len__(self):
        return len(self.__patient_list)

    def get_patients(self):
        """
        Returns all the patients from the repo
        """
        return self.__patient_list

    def add_patient(self, p):
        """
        Adds a new patient
        :param p: the patient
        """
        k = 1
        for i in range(0, len(self.__patient_list)):
            if self.__patient_list[i].get_personal_code() == p.get_personal_code():
                k = 0

        if k == 1:
            self.__patient_list.append(p)
        else:
            raise ValueError("Code already used")

    def delete_patient(self, index):
        """
        Deletes a patient at a given index
        :param index: the given index
        """
        if index >= 0 and index < len(self.__patient_list):
            del self.__patient_list[index]
        else:
            raise IndexError("Index not available")

    def update_patient(self, i, fs_name, ls_name, code, disease):
        """
        Updates a patient at a given index
        :param i: the given index
        :param fs_name: first name of the patient
        :param ls_name: last name of the patient
        :param code: the code og the patient
        :param disease: the disease of the patient
        """
        if i < 0 or i >= len(self.__patient_list):
            raise IndexError("Index not available")
        else:
            k = 1
            for i in range(0, len(self.__patient_list)):
                if self.__patient_list[i].get_personal_code() == code:
                    k = 0

            if k == 0:
                raise ValueError("Code already used")
            else:
                self.__patient_list[i].set_first_name(fs_name)
                self.__patient_list[i].set_last_name(ls_name)
                self.__patient_list[i].set_personal_code(code)
                self.__patient_list[i].set_disease(disease)

    def verify_patients_with_name(self, name):
        """
        Verifies if the list contains any patient with a given name
        :param name: the given name
        """
        for i in range(len(self.__patient_list)):
            if self.__patient_list[i].get_first_name == name:
                return 1
        return 0