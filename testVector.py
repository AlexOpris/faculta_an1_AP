import unittest
from domain.vector import MyVector

class TestVector(unittest.TestCase):

    def testCreate(self):

        v = MyVector(2, "y", 4, [3, 5])

        self.assertEqual(v.get_ID(), 2)

        self.assertEqual(v.get_Colour(), "y")

        self.assertEqual(v.get_Type(), 4)

        self.assertEqual(v.get_Values(), [3, 5])

    def testAddScalar(self):

        v = MyVector(2, "y", 4, [3, 5])
        v.add_Scalar(5)
        self.assertEqual(v.get_Values(), [8, 10])

        v = MyVector(2, "y", 4, [6, 3, 11])
        v.add_Scalar(1)
        self.assertEqual(v.get_Values(), [7, 4, 12])

        v = MyVector(2, "b", 7, [8, 4, 15])
        v.add_Scalar(10)
        self.assertEqual(v.get_Values(), [18, 14, 25])

        v = MyVector(5, "y", 1, [0])
        v.add_Scalar(8)
        self.assertEqual(v.get_Values(), [8])

        v = MyVector(1, "m", 10, [])
        v.add_Scalar(5)
        self.assertEqual(v.get_Values(), [])

    def testAddTwoVectors(self):

        v = MyVector(2, "e", 4, [60, 15])
        v.add_Two_Vectors([10, 20])
        self.assertEqual(v.get_Values(), [70, 35])

        v = MyVector(2, "b", 4, [9, 1, 5])
        v.add_Two_Vectors([1, 2, 5])
        self.assertEqual(v.get_Values(), [10, 3, 10])

        v = MyVector(2, "r", 4, [6])
        v.add_Two_Vectors([90])
        self.assertEqual(v.get_Values(), [96])

        v = MyVector(2, "y", 4, [2, 5, 10, 7])
        v.add_Two_Vectors([10, 2, 5, 4])
        self.assertEqual(v.get_Values(), [12, 7, 15, 11])

        v = MyVector(2, "y", 4, [15])
        v.add_Two_Vectors([-20])
        self.assertEqual(v.get_Values(), [-5])

    def testSubtractTwoVectors(self):

        v = MyVector(3, "y", 1, [9])
        v.subtract_Two_Vectors([10])
        self.assertEqual(v.get_Values(), [-1])

        v = MyVector(22, "r", 7, [10, 36, 8])
        v.subtract_Two_Vectors([10, 4, 5])
        self.assertEqual(v.get_Values(), [0, 32, 3])

        v = MyVector(9, "m", 6, [5, 8])
        v.subtract_Two_Vectors([3, 9])
        self.assertEqual(v.get_Values(), [2, -1])

        v = MyVector(11, "b", 2, [40, 70, 33, 6])
        v.subtract_Two_Vectors([52, 32, 77, 8])
        self.assertEqual(v.get_Values(), [-12, 38, -44, -2])

        v = MyVector(6, "b", 14, [73])
        v.subtract_Two_Vectors([52])
        self.assertEqual(v.get_Values(), [21])

    def testMultiplyTwoVectors(self):

        v = MyVector(22, "r", 7, [10, 36, 8])
        k = v.multiply_Two_Vectors([3, 2, 5])
        self.assertEqual(k, 142)

        v = MyVector(7, "y", 3, [15])
        k = v.multiply_Two_Vectors([7])
        self.assertEqual(k, 105)

        v = MyVector(10, "m", 5, [63, 43, 5])
        k = v.multiply_Two_Vectors([5, 8, 2])
        self.assertEqual(k, 669)

        v = MyVector(40, "b", 2, [62, 16, 99])
        k = v.multiply_Two_Vectors([0, 7, 2])
        self.assertEqual(k, 310)

        v = MyVector(2, "b", 10, [13, 1, 73])
        k = v.multiply_Two_Vectors([47, 36, 4])
        self.assertEqual(k, 939)

    def testSumElemInVector(self):

        v = MyVector(22, "r", 7, [10, 36, 8])
        k = v.sum_Elem_In_Vector()
        self.assertEqual(k, 54)

        v = MyVector(22, "r", 7, [6, 23, 38, 10])
        k = v.sum_Elem_In_Vector()
        self.assertEqual(k, 77)

        v = MyVector(22, "r", 7, [1, 6, 18, 0])
        k = v.sum_Elem_In_Vector()
        self.assertEqual(k, 25)

        v = MyVector(22, "r", 7, [94, 6])
        k = v.sum_Elem_In_Vector()
        self.assertEqual(k, 100)

        v = MyVector(22, "r", 7, [55])
        k = v.sum_Elem_In_Vector()
        self.assertEqual(k, 55)

    def testProductElemInVector(self):

        v = MyVector(22, "r", 7, [87])
        k = v.product_Elem_In_Vector()
        self.assertEqual(k, 87)

        v = MyVector(22, "r", 7, [52, 34, 5])
        k = v.product_Elem_In_Vector()
        self.assertEqual(k, 8840)

        v = MyVector(22, "r", 7, [2, 6, 43, 71])
        k = v.product_Elem_In_Vector()
        self.assertEqual(k, 36636)

        v = MyVector(22, "r", 7, [4, 7])
        k = v.product_Elem_In_Vector()
        self.assertEqual(k, 28)

        v = MyVector(22, "r", 7, [4, 5, 2, 0])
        k = v.product_Elem_In_Vector()
        self.assertEqual(k, 0)

    def testAvgElemInVector(self):

        v = MyVector(22, "r", 7, [6, 25, 42, 10])
        k = v.avg_Elem_In_Vector()
        self.assertEqual(k, 20.75)

        v = MyVector(22, "r", 7, [4, 5, 2, 0])
        k = v.avg_Elem_In_Vector()
        self.assertEqual(k, 2.75)

        v = MyVector(22, "r", 7, [54, 88, 67])
        k = v.avg_Elem_In_Vector()
        self.assertEqual(k, 69.66666666666667)

        v = MyVector(22, "r", 7, [32, 73, 45])
        k = v.avg_Elem_In_Vector()
        self.assertEqual(k, 50.0)

        v = MyVector(22, "r", 7, [72, 46])
        k = v.avg_Elem_In_Vector()
        self.assertEqual(k, 59.0)

    def testMinFromVector(self):

        v = MyVector(22, "r", 7, [324, 7, 5])
        self.assertEqual(v.min_From_Vector(), 5)

        v = MyVector(22, "r", 7, [62, 42, 89, 53])
        self.assertEqual(v.min_From_Vector(), 42)

        v = MyVector(22, "r", 7, [100, 52, 63, 54, 22, 92])
        self.assertEqual(v.min_From_Vector(), 22)

        v = MyVector(22, "r", 7, [92, 90, 52, 1])
        self.assertEqual(v.min_From_Vector(), 1)

        v = MyVector(22, "r", 7, [83, 62])
        self.assertEqual(v.min_From_Vector(), 62)

    def testMaxFromVector(self):

        v = MyVector(22, "r", 7, [39, 80, 72, 52])
        self.assertEqual(v.max_From_Vector(), 80)

        v = MyVector(22, "r", 7, [92, 75, 33, 2])
        self.assertEqual(v.max_From_Vector(), 92)

        v = MyVector(22, "r", 7, [92, 55, 83, 100])
        self.assertEqual(v.max_From_Vector(), 100)

        v = MyVector(22, "r", 7, [17, 73, 4])
        self.assertEqual(v.max_From_Vector(), 73)

        v = MyVector(22, "r", 7, [5, 2, 3])
        self.assertEqual(v.max_From_Vector(), 5)








if __name__ == '__main__':
    unittest.main()
