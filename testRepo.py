import unittest
from infrastructure.repo import VectorRepository
from domain.vector import MyVector


class TestVectorRepository(unittest.TestCase):

    def testCreator(self):

        l = []
        repo = VectorRepository(l)

        self.assertEqual(len(repo), 0)

    def testAddVector(self):

        l = []
        repo = VectorRepository(l)

        v1 = MyVector(4, "y", 3, [2, 5])
        repo.addVector(v1)
        self.assertEqual(len(l), 1)

        v2 = MyVector(1, "m", 23, [66, 4, 59])
        repo.addVector(v2)
        self.assertEqual(len(l), 2)

    def testGetVectorAtIndex(self):

        l = []
        repo = VectorRepository(l)
        v1 = MyVector(4, "y", 3, [2, 5])
        repo.addVector(v1)
        v2 = MyVector(1, "m", 23, [66, 4, 59])
        repo.addVector(v2)
        v3 = MyVector(2, "b", 9, [1, 34, 80])
        repo.addVector(v3)
        self.assertEqual(repo.getVectorAtIndex(1), v2)

        self.assertRaises(IndexError, repo.getVectorAtIndex, 7)

    def testUpdateVectorAtIndex(self):

        l = []
        repo = VectorRepository(l)
        v1 = MyVector(4, "y", 3, [2, 5])
        repo.addVector(v1)
        v2 = MyVector(1, "m", 23, [66, 4, 59])
        repo.addVector(v2)
        v3 = MyVector(2, "b", 9, [1, 34, 80])
        repo.addVector(v3)
        repo.updateVectorAtIndex(1, "r", 5, [3, 7])

        self.assertEqual(v2.get_Colour(), "r")

        self.assertEqual(v2.get_Type(), 5)

        self.assertEqual(v2.get_Values(), [3, 7])



    def testUpdateVectorById(self):

        l = []
        repo = VectorRepository(l)
        v1 = MyVector(4, "y", 3, [2, 5])
        repo.addVector(v1)
        v2 = MyVector(1, "m", 23, [66, 4, 59])
        repo.addVector(v2)
        v3 = MyVector(2, "b", 9, [1, 34, 80])
        repo.addVector(v3)
        repo.updateVectorById(2, "r", 5, [3, 7])

        self.assertEqual(v3.get_ID(), 2)

        self.assertEqual(v3.get_Colour(), "r")

        self.assertEqual(v3.get_Type(), 5)

        self.assertEqual(v3.get_Values(), [3, 7])

    def testDeleteVectorAtIndex(self):

        l = []
        repo = VectorRepository(l)
        v1 = MyVector(4, "y", 3, [2, 5])
        repo.addVector(v1)
        v2 = MyVector(1, "m", 23, [66, 4, 59])
        repo.addVector(v2)
        v3 = MyVector(2, "b", 9, [1, 34, 80])
        repo.addVector(v3)
        repo.deleteVectorAtIndex(0)

        self.assertEqual(len(l), 2)

        repo.deleteVectorAtIndex(1)

        self.assertEqual(len(l), 1)

        self.assertRaises(IndexError, repo.deleteVectorAtIndex, 6)

    def testDeleteVectorById(self):

        l = []
        repo = VectorRepository(l)
        v1 = MyVector(4, "y", 3, [2, 5])
        repo.addVector(v1)
        v2 = MyVector(1, "m", 23, [66, 4, 59])
        repo.addVector(v2)
        v3 = MyVector(2, "b", 9, [1, 34, 80])
        repo.addVector(v3)
        repo.deleteVectorById(1)

        self.assertEqual(len(l), 2)

        repo.deleteVectorById(2)

        self.assertEqual(len(l), 1)


if __name__ == '__main__':
    unittest.main()
