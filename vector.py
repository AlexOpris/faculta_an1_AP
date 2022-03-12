class MyVector:
    """
    A vector has an id, a colour, a type and some values given as a list of numbers
    """
    colour_list = ["r", "b", "m", "y", "g"]
    def __init__(self, id = 0, c = "r", t = 1, v = []):
        """
        :param id: the vector id
        :param c: the colour of the vector
        :param t: the type of the vector
        :param l: the list of values
        """
        self.__id = id
        if c in self.colour_list:
            self.__colour = c
        else:
            raise AttributeError("Colour not in list")
        if t >= 1:
            self.__type = t
        else:
            raise AttributeError("Type should be greater or equal to 1")
        self.__values = v

    def get_ID(self):
        return self.__id

    def set_ID(self, id):
        self.__id = id

    def get_Colour(self):
        return self.__colour

    def set_Colour(self, c):
        if c in self.colour_list:
            self.__colour = c
        else:
            raise AttributeError("Colour not in list")

    def get_Type(self):
        return self.__type

    def set_Type(self, t):
        if t >= 1:
            self.__type = t
        else:
            raise AttributeError("Type should be greater or equal to 1")

    def get_Values(self):
        return self.__values

    def set_Values(self, v):
        self.__values = v

    def __str__(self):
        return "The vector of id " + str(self.__id) + " and colour " + self.__colour + " is of type " + str(self.__type) + " and has the values: " + str(self.__values)

    def add_Scalar(self, k):
        """
        Adds a given scalar to all the values of the vector
        :param k: the given scalar
        """
        p = self.get_Values()
        for i in range(len(p)):
            p[i] += k
        self.set_Values(p)

    def add_Two_Vectors(self, a):
        """
        Adds the values of two vectors
        :param a: the other vector
        """
        p = self.get_Values()
        if len(p) != len(a):
            raise ValueError("The vectors don't have the same number of values")
        else:
            for i in range(len(p)):
                p[i] = a[i] + p[i]
            self.set_Values(p)

    def subtract_Two_Vectors(self, a):
        """
        Subtracts the values of 2 vectors
        :param a: the other vector
        """
        p = self.get_Values()
        if len(p) != len(a):
            raise ValueError("The vectors don't have the same number of values")
        else:
            for i in range(len(p)):
                p[i] = p[i] - a[i]
            self.set_Values(p)

    def multiply_Two_Vectors(self, a):
        """
        Multiplies the values of two vectors
        :param a: the other vector
        :return: the multiplication of the elements of the vectors
        """
        k = 0
        p = self.get_Values()
        if len(p) != len(a):
            raise ValueError("The vectors don't have the same number of values")
        else:
            for i in range(len(p)):
                k = k + p[i] * a[i]
            return k

    def sum_Elem_In_Vector(self):
        """
        Adds the elements of the vector
        :return: the sum of the elements of the vector
        """
        k = 0
        p = self.get_Values()
        if len(p) == 0:
            raise ValueError("The vector has 0 values")
        else:
            for i in p:
                k = k + i
            return k

    def product_Elem_In_Vector(self):
        """
        Multiplies the elements of the vector
        """
        k = 1
        p = self.get_Values()
        if len(p) == 0:
            raise ValueError("The vector has 0 values")
        else:
            for i in p:
                k = k * i
            return k

    def avg_Elem_In_Vector(self):
        """
        Calculates the avarage of the elements of the vector
        """
        k = 0
        p = self.get_Values()
        if len(p) == 0:
            raise ValueError("The vector has 0 values")
        else:
            for i in p:
                k = k + i
            return k / len(p)

    def min_From_Vector(self):
        """
        Calculates the minimum element from the vector
        """
        p = self.get_Values()
        if len(p) == 0:
            raise ValueError("The vector has 0 values")
        else:
            k = p[0]
            for i in range(1, len(p)):
                if p[i] < k:
                    k = p[i]
            return k

    def max_From_Vector(self):
        """
        Calculates the maximum element from the vector
        """
        p = self.get_Values()
        if len(p) == 0:
            raise ValueError("The vector has 0 values")
        else:
            k = p[0]
            for i in range(1, len(p)):
                if p[i] > k:
                    k = p[i]
            return k
