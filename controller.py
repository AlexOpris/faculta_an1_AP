from domain.vector import MyVector
from infrastructure.repo import VectorRepository

class VectorController:

    def __init__(self, vector_repo: VectorRepository):
        self.__vector_repo = vector_repo


    def add(self, vector: MyVector):
        self.__vector_repo.addVector(vector)

    def print_all_vectors(self):
        """
        Prints all the vectors from the list
        """
        print("The vector list is:")
        for i in self.__vector_repo.getVectors():
            print(i)

    def get_vector_at_index(self, index):
        """
        Returns a vector at a given index
        :param index: the given index
        """
        return self.__vector_repo.getVectorAtIndex(index)

    def update_vector_at_index(self, index, c, t, v):
        """
        Updates a vector at a given index
        :param index: the given index
        :param id: the new id
        :param c: the new colour
        :param t: the new type
        :param v: the new values
        """
        self.__vector_repo.updateVectorAtIndex(index, c, t, v)

    def update_vector_by_id(self, id, c, t, v):
        """
        Updates a vector at a given id
        :param id: the given id
        :param c: the new colour
        :param t: the new type
        :param v: the new values
        """
        self.__vector_repo.updateVectorById(id, c, t, v)

    def delete_vector_at_index(self, i):
        """
        Deletes a vector from the list at a given index
        :param index: the given index
        """
        self.__vector_repo.deleteVectorAtIndex(i)

    def delete_vector_by_id(self, id):
        """
        Deletes a vector from the list by a given id
        :param id: the given id
        """
        self.__vector_repo.deleteVectorById(id)

    def plot_vectors(self):
        """
        Plots all vectors
        """
        self.__vector_repo.plotVectors()

    def update_colour_by_name_id(self, id, c):
        """
        Updates the colour of a vector identified by name_id
        :param id: the given id
        :param c: the new colour
        """
        self.__vector_repo.updateColourByName_Id(id, c)

    def delete_vectors_with_max(self, mx):
        """
        Deletes all vectors with a given max
        :param mx: the maximum value
        """
        self.__vector_repo.deleteAllVectorWithMaxGiven(mx)