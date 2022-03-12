class Patient:
    """
    A patient is identified by its first name, last name, personal code and disease.
    """
    def __init__(self, first_name="", last_name="", personal_code=0, disease=""):
        """
        :param first_name: the first name of the patient
        :param last_name: the last name of the patient
        :param personal_code: the personal code of the patient
        :param disease: the disease of the patient
        """
        self.__first_name = first_name
        self.__last_name = last_name
        if personal_code > 9999999999 or personal_code < 1000000000:
            raise ValueError("Incorrect personal code")
        else:
            self.__personal_code = personal_code
        self.__disease = disease

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, name):
        self.__first_name = name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, name):
        self.__last_name = name

    def get_personal_code(self):
        return self.__personal_code

    def set_personal_code(self, personal_code):
        if personal_code > 9999999999 or personal_code < 1000000000:
            raise ValueError("Incorrect personal code")
        else:
            self.__personal_code = personal_code

    def get_disease(self):
        return self.__disease

    def set_disease(self, disease):
        self.__disease = disease

    def get_age(self):
        x = self.get_personal_code()
        x = x % 10000
        return 2020 - x

    def get_full_name(self):
        name = self.get_first_name() + self.get_last_name()
        return name

    def __str__(self):
        return "The patient with the personal code " + str(self.__personal_code) + " is named " + self.__last_name + " " + self.__first_name + " and suffers from " + self.__disease
