from domain.vector import MyVector
#import matplotlib as plt

class VectorRepository():

    colour_list = ["r", "g", "m", "b", "y"]
    def __init__(self, vector_list):
        self.__vector_list = vector_list

    def __len__(self):
        return len(self.__vector_list)

    def getVectors(self):
        """
        :return: returns all vectors from the list
        """
        return self.__vector_list

    def addVector(self, vector: MyVector):
        """
        Adds a new vector to the list
        :param vector: the given vector
        """
        k = 1
        for i in range(0, len(self.__vector_list)):
            if self.__vector_list[i].get_ID() == vector.get_ID():
                k = 0
        if k == 1:
            self.__vector_list.append(vector)
        else:
            raise ValueError("Id already used, try again")


    def getVectorAtIndex(self, index):
        """
        Returns a vector at a given index
        :param index: the given index
        """
        if index < 0 or index >= len(self.__vector_list):
            raise IndexError("Index not in list, try again")
        else:
            return self.__vector_list[index]

    def updateVectorAtIndex(self, index, c, t, v):
        """
        Updates a vector at a given index
        :param index: the given index
        :param id: the new id
        :param c: the new colour
        :param t: the new type
        :param v: the new values
        """
        if index < 0 or index >= len(self.__vector_list):
            raise IndexError("Index not in list, try again")
        else:
            self.__vector_list[index].set_Colour(c)
            self.__vector_list[index].set_Type(t)
            self.__vector_list[index].set_Values(v)

    def updateVectorById(self, id, c, t, v):
        """
        Updates a vector at a given id
        :param id: the given id
        :param c: the new colour
        :param t: the new type
        :param v: the new values
        """
        k = 0
        for i in range(0, len(self.__vector_list)):
            if self.__vector_list[i].get_ID() == id:
                self.__vector_list[i].set_Colour(c)
                self.__vector_list[i].set_Type(t)
                self.__vector_list[i].set_Values(v)
                k = 1
                break
        if k == 0:
            print("Id doesn't exist, try again")

    def deleteVectorAtIndex(self, index):
        """
        Deletes a vector from the list at a given index
        :param index: the given index
        """
        if index < 0 and index >= len(self.__vector_list):
            raise IndexError("Index not in list, try again")
        else:
            del self.__vector_list[index]

    def deleteVectorById(self, id):
        """
        Deletes a vector from the list by a given id
        :param id: the given id
        """
        k = 0
        for i in range(0, len(self.__vector_list)):
            if self.__vector_list[i].get_ID() == id:
                del self.__vector_list[i]
                k = 1
                break
        if k == 0:
            print("Id doesn't exist, try again")

    def plotVectors(self):
        """
        Plot all points in a chart
        """
        t = []
        u = []
        v = []
        m = []
        j1 = j2 = j3 = j4 = 1
        for i in range(len(self.__vector_list)):
            if self.__vector_list[i].type == 1:
                t.append(1)
                m.append("o")
            if self.__vector_list[i].type == 2:
                t.append(2)
                m.append("s")
            if self.__vector_list[i].type == 3:
                t.append(3)
                m.append("^")
            if self.__vector_list[i].type >= 4:
                t.append(4)
                m.append("D")
        for i in range(len(self.__vector_list)):
            if t[i] == 1:
                u.append(j1)
                j1 = j1 + 1
            if t[i] == 2:
                u.append(j2)
                j2 = j2 + 1
            if t[i] == 3:
                u.append(j3)
                j3 = j3 + 1
            if t[i] == 4:
                u.append(j4)
                j4 = j4 + 1
            v.append(self.__vector_list[i].color)
        for i in range(len(self.__vector_list)):
            plt.scatter(t[i], u[i], c=v[i], marker=m[i])
        plt.show()

    def updateColourByName_Id(self, id, c):
        """
        Updates the colour of a vector identified by name_id
        :param id: the given id
        :param c: the new colour
        """
        k = 0
        for i in range(0, len(self.__vector_list)):
            if self.__vector_list[i].get_ID() == id:
                self.__vector_list[i].set_Colour(c)
                k = 1
                break
        if k == 0:
            print("Id doesn't exist, try again")

    def deleteAllVectorWithMaxGiven(self, mx):
        """
        Deletes all vectors which have the maximum value the same as a given value
        :param mx: the maximum given value
        """
        for i in range(len(self.__vector_list)-1, -1, -1):
            if self.__vector_list[i].max_From_Vector() == mx:
                del self.__vector_list[i]
