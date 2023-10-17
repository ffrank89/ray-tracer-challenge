import unittest
from raytracer.matrix import Matrix, IDENTITY
from raytracer.tuples import Tuple


class TestMatrix(unittest.TestCase):

    def test_4x4(self):
        data = [
            [1,2,3,4],
            [5.5,6.5,7.5,8.5],
            [9,10,11,12],
            [13.5,14.5,15.5,16.5]
        ]
        m = Matrix(4, data)
        self.assertTrue(m.data[0][0] == 1)
        self.assertTrue(m.data[0][3] == 4)
        self.assertTrue(m.data[1][0] == 5.5)
        self.assertTrue(m.data[1][2] == 7.5)
        self.assertTrue(m.data[2][2] == 11)
        self.assertTrue(m.data[3][0] == 13.5)
        self.assertTrue(m.data[3][2] == 15.5)
    
    def test_2x2(self):
        data = [
            [-3,5],
            [1,-2]
        ]
        m = Matrix(2, data)
        self.assertTrue(m.data[1][1] == -2)
        self.assertTrue(m.data[0][0] == -3)
        self.assertTrue(m.data[1][0] == 1)
        self.assertTrue(m.data[0][1] == 5)
    
    def test_3x3(self):
        data = [
            [-3,5,0],
            [1,-2,-7],
            [0,1,1]
        ]
        m = Matrix(3, data)
        self.assertTrue(m.data[1][1] == -2)
        self.assertTrue(m.data[0][0] == -3)
        self.assertTrue(m.data[2][2] == 1)

    def test_4x4_equality(self):
        data = [
            [1,2,3,4],
            [5,6,7,8],
            [9,8,7,6],
            [5,4,3,2]
        ]
        m1 = Matrix(4, data)
        m2 = Matrix(4, data)
        data2 = [
            [1,2,3,4],
            [5,6,7,8],
            [9,8,7,6],
            [5,4,3,2]
        ]
        m3 = Matrix(4, data2)

        self.assertEqual(m1,m3)

    def test_4x4_inequality(self):
        data = [
            [1,2,3,4],
            [5,6,7,8],
            [9,8,7,6],
            [5,4,3,2]
        ]
        m1 = Matrix(4, data)

        data2 = [
            [2,2,3,4],
            [5,6,7,8],
            [9,8,7,6],
            [5,4,3,2]
        ]
        m2 = Matrix(4, data2)
        self.assertNotEqual(m1,m2)

    def test_4x4_matrix_multiplication(self):
        data = [
            [1,2,3,4],
            [5,6,7,8],
            [9,8,7,6],
            [5,4,3,2]
        ]
        m1 = Matrix(4, data)

        data2 = [
            [-2,1,2,3],
            [3,2,1,-1],
            [4,3,6,5],
            [1,2,7,8]
        ]
        m2 = Matrix(4, data2)

        result_data = [
            [20,22,50,48],
            [44,54,114,108],
            [40,58,110,102],
            [16,26,46,42]
        ]
        result = Matrix(4, result_data)
        self.assertTrue(result == m1.matrix_multiply(m2))

    def test_tuple_multiplication(self):
        data = [
            [1,2,3,4],
            [2,4,4,2],
            [8,6,4,1],
            [0,0,0,1]
        ]
        a = Matrix(4, data)
        b = Tuple(1,2,3,1)

        result = Tuple(18,24,33,1)
        self.assertEqual(a.tuple_multiply(b), result)

    def test_identity_mutliplication(self):
        data = [
            [1,2,3,4],
            [1,2,4,8],
            [2,4,8,16],
            [4,8,16,32]
        ]
        a = Matrix(4, data)

        self.assertEqual(a.matrix_multiply(IDENTITY), a)

    def test_identity_tuple_multiplication(self):
        t = Tuple(1,2,3,1)
        self.assertEqual(IDENTITY.tuple_multiply(t), t)

    def test_transpose(self):
        data = [
            [0,9,3,0],
            [9,8,0,8],
            [1,8,5,3],
            [0,0,5,8]
        ]
        a = Matrix(4, data)
        a = a.transpose()
        transposed_data = [
            [0,9,1,0],
            [9,8,8,0],
            [3,0,5,5],
            [0,8,3,8]
        ]
        self.assertEqual(a.data, transposed_data)
    
    def test_transpose_identity(self):
        a = IDENTITY
        a = a.transpose()
        self.assertEqual(a, IDENTITY)

    def test_2x2_determinant(self):
        data = [
            [1,5],
            [-3,2]
        ]
        a = Matrix(2, data)
        self.assertEquals(17, a.determinant())

    def test_3x3_submatrix(self):
        data_3x3 = [
            [1,5,0],
            [-3,2,7],
            [0,6,-3]
        ]
        a = Matrix(3, data_3x3)
        data_2x2 = [
            [-3,2],
            [0,6]
        ]
        s = Matrix(2,data_2x2)

        self.assertEquals(a.submatrix(0,2), s)


    def test_4x4_submatrix(self):
        data_4x4 = [
            [-6,1,1,6],
            [-8,5,8,6],
            [-1,0,8,2],
            [-7,1,-1,1]
        ]
        a = Matrix(4, data_4x4)

        data_3x3 = [
            [-6,1,6],
            [-8,8,6],
            [-7,-1,1]
        ]
        s = Matrix(3, data_3x3)
        self.assertEquals(a.submatrix(2,1), s)

    def test_manipulate_minors(self):
        data_3x3 = [
            [3,5,0],
            [2,-1,-7],
            [6,-1,5]
        ]
        a = Matrix(3, data_3x3)
        s = a.submatrix(1,0)
        self.assertEqual(s.determinant(), 25)
        self.assertEquals(a.minor(1,0), 25)

    def test_computing_cofactors(self):
        data_3x3 = [
            [3,5,0],
            [2,-1,-7],
            [6,-1,5]
        ]
        a = Matrix(3, data_3x3)
        self.assertEquals(a.minor(0,0), -12)
        self.assertEquals(a.cofactor(0,0), -12)
        self.assertEquals(a.minor(1,0), 25)
        self.assertEquals(a.cofactor(1,0), -25)

    def test_bringing_it_together_3x3(self):
        data_3x3 = [
            [1,2,6],
            [-5,8,-4],
            [2,6,4]
        ]
        a = Matrix(3, data_3x3)
        self.assertEqual(a.cofactor(0,0), 56)
        self.assertEqual(a.cofactor(0,1), 12)
        self.assertEqual(a.cofactor(0,2), -46)
        self.assertEqual(a.determinant(), -196)

    def test_bringing_it_together_4x4(self):
        data_4x4 = [
            [-2,-8,3,5],
            [-3,1,7,3],
            [1,2,-9,6],
            [-6,7,7,-9]
        ]
        a = Matrix(4, data_4x4)
        self.assertEqual(a.cofactor(0,0), 690)
        self.assertEqual(a.cofactor(0,1), 447)
        self.assertEqual(a.cofactor(0,2), 210)
        self.assertEqual(a.cofactor(0,3), 51)
        self.assertEqual(a.determinant(), -4071)

    def test_is_invertible(self):
        data_4x4 = [
            [6,4,4,4],
            [5,5,7,6],
            [4,-9,3,-7],
            [9,1,7,-6]
        ]
        a = Matrix(4, data_4x4)
        self.assertEqual(a.determinant(), -2120)
        self.assertTrue(a.is_invertible())
    
    def test_not_is_invertible(self):
        data_4x4_zero_det = [
            [-4,2,-2,-3],
            [9,6,2,6],
            [0,-5,1,-5],
            [0,0,0,0]
        ]
        b = Matrix(4, data_4x4_zero_det)
        self.assertEqual(b.determinant(), 0)
        self.assertFalse(b.is_invertible())
    
    def test_inverse(self):
        data_4x4 = [
            [-5,2,6,-8],
            [1,-5,1,8],
            [7,7,-6,-7],
            [1,-3,7,4]
        ]
        a = Matrix(4, data_4x4)
        b = a.inverse()

        self.assertEqual(a.determinant(), 532)
        self.assertEqual(a.cofactor(2,3), -160)
        self.assertEqual(b.data[3][2], -160/532)
        self.assertEqual(a.cofactor(3,2), 105)
        self.assertEqual(b.data[2][3], 105/532)

        b_data = [
            [.21805,.45113,.24060,-.04511],
            [-.80827,-1.45677,-.44361,.52068],
            [-.07895,-.22368,-.05263,.19737],
            [-.52256,-.81391,-.30075,.30639]
        ]
        b_copy = Matrix(4, b_data)
        self.assertEqual(b, b_copy)

    def test_inverse_again(self):
        data_4x4 = [
            [8,-5,9,2],
            [7,5,6,1],
            [-6,0,9,6],
            [-3,0,-9,-4]
        ]

        a = Matrix(4, data_4x4)

        inverse_data = [
            [-0.15385, -0.15385, -0.28205, -0.53846], 
            [-0.07692, 0.12308, 0.02564, 0.03077], 
            [0.35897, 0.35897, 0.43590, 0.92308], 
            [-0.69231, -0.69231, -0.76923, -1.92308]
        ]
        i = Matrix(4, inverse_data)
        self.assertEqual(i, a.inverse())

    
    def test_multiply_product_by_inverse(self):
        a_data = [
            [3,-9,7,3],
            [3,-8,2,-9],
            [-4,4,4,1],
            [-6,5,-1,1]
        ]
        a = Matrix(4, a_data)

        b_data = [
            [8,2,2,2],
            [3,-1,7,0],
            [7,0,5,4],
            [6,-2,0,5]
        ]
        b = Matrix(4, b_data)
        c = a.matrix_multiply(b)
        self.assertEquals(c.matrix_multiply(b.inverse()), a)



    



if __name__ == "__main__":
    unittest.main()