import unittest
from raytracer.transformations import Translation, Scaling, Rotation_X, Rotation_Y, Rotation_Z, Shearing
from raytracer.tuples import Tuple, Vector, Point
from math import pi, sqrt
class TransformationTests(unittest.TestCase):

    def test_multiplying_by_translation_matrix(self):
        transform = Translation(5,-3,2)
        p = Point(-3,4,5)
        
        self.assertEqual(transform.tuple_multiply(p), Point(2,1,7))
    
    def test_inverse_translation_matrix(self):
        transform = Translation(5,-3,2)
        inv = transform.inverse()
        p = Point(-3,4,5)

        self.assertEqual(inv.tuple_multiply(p), Point(-8,7,3))

    def test_multiply_vector_by_translation_matrix(self):
        transform = Translation(5,-3,2)
        v = Vector(-3,4,5)

        self.assertEqual(transform.tuple_multiply(v), v)

    def test_scaling_matrix_applied_to_point(self):
        transform = Scaling(2,3,4)
        v = Point(-4,6,8)

        self.assertEqual(transform.tuple_multiply(v), Point(-8, 18, 32))

    def test_scaling_matrix_applied_to_vector(self):
        transform = Scaling(2,3,4)
        v = Vector(-4,6,8)

        self.assertEqual(transform.tuple_multiply(v), Vector(-8, 18, 32))

    def test_shrink_with_inverse_scaling_matrix(self):
        transform = Scaling(2,3,4)
        inv = transform.inverse()
        v = Vector(-4,6,8)

        self.assertEqual(inv.tuple_multiply(v), Vector(-2,2,2))
    
    def test_reflection(self):
        #reflection is scaling w a negative value
        transform = Scaling(-1,1,1)
        p = Point(2,3,4)
        
        self.assertEqual(transform.tuple_multiply(p), Point(-2,3,4))

    def test_x_rotation(self):
        p = Point(0,1,0)
        half_quarter = Rotation_X(pi/4)
        full_quarter = Rotation_X(pi/2)
        self.assertEqual(half_quarter.tuple_multiply(p), Point(0, sqrt(2)/2, sqrt(2)/2))
        self.assertEqual(full_quarter.tuple_multiply(p), Point(0, 0, 1))

    def test_x_rotation_inverse(self):
        p = Point(0,1,0)
        half_quarter = Rotation_X(pi/4)
        inv = half_quarter.inverse()
        self.assertEqual(inv.tuple_multiply(p), Point(0, sqrt(2)/2, -sqrt(2)/2))

    def test_y_rotation(self):
        p = Point(0,0,1)
        half_quarter = Rotation_Y(pi/4)
        full_quarter = Rotation_Y(pi/2)
        self.assertEqual(half_quarter.tuple_multiply(p), Point(sqrt(2)/2, 0, sqrt(2)/2))
        self.assertEqual(full_quarter.tuple_multiply(p), Point(1, 0, 0))

    def test_z_rotation(self):
        p = Point(0,1,0)
        half_quarter = Rotation_Z(pi/4)
        full_quarter = Rotation_Z(pi/2)
        self.assertEqual(half_quarter.tuple_multiply(p), Point(-sqrt(2)/2, sqrt(2)/2, 0))
        self.assertEqual(full_quarter.tuple_multiply(p), Point(-1, 0, 0))

    def test_shearing_x_proportionto_y(self):
        transform = Shearing(1,0,0,0,0,0)
        p = Point(2,3,4)
        self.assertEqual(transform.tuple_multiply(p), Point(5,3,4))

    def test_shearing_x_proportionto_z(self):
        transform = Shearing(0,1,0,0,0,0)
        p = Point(2,3,4)
        self.assertEqual(transform.tuple_multiply(p), Point(6,3,4))
        
    def test_shearing_y_proportionto_x(self):
        transform = Shearing(0,0,1,0,0,0)
        p = Point(2,3,4)
        self.assertEqual(transform.tuple_multiply(p), Point(2,5,4))

    def test_shearing_y_proportionto_z(self):
        transform = Shearing(0,0,0,1,0,0)
        p = Point(2,3,4)
        self.assertEqual(transform.tuple_multiply(p), Point(2,7,4))

    def test_shearing_z_proportionto_x(self):
        transform = Shearing(0,0,0,0,1,0)
        p = Point(2,3,4)
        self.assertEqual(transform.tuple_multiply(p), Point(2,3,6))

    def test_shearing_z_proportionto_y(self):
        transform = Shearing(0,0,0,0,0,1)
        p = Point(2,3,4)
        self.assertEqual(transform.tuple_multiply(p), Point(2,3,7))

    def test_sequence(self):
        p = Point(1,0,1)
        A = Rotation_X(pi/2)
        B = Scaling(5,5,5)
        C = Translation(10,5,7)

        p2 = A.tuple_multiply(p)
        self.assertEqual(p2,Point(1,-1,0))

        p3 = B.tuple_multiply(p2)
        self.assertEqual(p3,Point(5,-5,0))

        p4 = C.tuple_multiply(p3)
        self.assertEqual(p4,Point(15,0,7))

    def test_chained_apply_in_reverse(self):
        p = Point(1,0,1)
        A = Rotation_X(pi/2)
        B = Scaling(5,5,5)
        C = Translation(10,5,7)

        T = C.matrix_multiply(B).matrix_multiply(A)

        self.assertEqual(T.tuple_multiply(p), Point(15,0,7))

if __name__ == "__main__":
    unittest.main()