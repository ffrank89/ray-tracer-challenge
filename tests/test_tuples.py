import unittest
import math
from raytracer.tuples import Tuple, Point, Vector

class TupleTests(unittest.TestCase):

    def test_tuple_is_point(self):
        a = Tuple(4.3, -4.2, 3.1, 1.0)
        self.assertTrue(a.w == 1.0)
        self.assertTrue(a.isPoint())
        self.assertFalse(a.isVector())

    def test_tuple_is_vector(self):
        a = Tuple(4.3, -4.2, 3.1, 0.0)
        self.assertTrue(a.w == 0.0)
        self.assertTrue(a.isVector())
        self.assertFalse(a.isPoint())

    def test_point_creates_point(self):
        p = Point(4,-4,3)
        self.assertTrue(p == Tuple(4,-4,3,1))
        self.assertTrue(p.isPoint())
        self.assertFalse(p.isVector())

    def test_vector_creates_vector(self):
        v = Vector(4,-4,3)
        self.assertTrue(v == Tuple(4,-4,3,0))
        self.assertTrue(v.isVector())
        self.assertFalse(v.isPoint())

    def test_adding_two_tuples(self):
        a1 = Tuple(3,-2,5,1)
        a2 = Tuple(-2,3,1,0)

        self.assertTrue(a1 + a2 == Tuple(1,1,6,1))
        #should we add more test cases?
        #should we prevent point+point addition? (So w stays below 2)?

    def test_subtracting_two_points(self):
        p1 = Point(3,2,1)
        p2 = Point(5,6,7)
        self.assertTrue(p1 - p2 == Vector(-2,-4,-6))

    def test_subtracting_vector_from_point(self):
        p = Point(3,2,1)
        v = Vector(5,6,7)
        self.assertTrue(p - v == Point(-2,-4,-6))

    def test_subtracting_two_vectors(self):
        v1 = Vector(3,2,1)
        v2 = Vector(5,6,7)
        self.assertTrue(v1 - v2 == Vector(-2,-4,-6))

    def test_negating_tuple(self):
        #to find the opposite of some vector
        v = Vector(1,-2,3)
        self.assertTrue(v.negate() == Vector(-1,2,-3))
        a = Tuple(1,-2,3,-4)
        self.assertTrue(a.negate() == Tuple(-1,2,-3,4))

    def test_multiply_tuple_by_scalar(self):
        a = Tuple(1,-2,3,-4)
        self.assertTrue(a.scale(3.5) == Tuple(3.5,-7,10.5,-14))

    def test_multiply_tuple_by_fraction(self):
        a = Tuple(1,-2,3,-4)
        self.assertTrue(a.scale(.5) == Tuple(.5,-1,1.5,-2))

    def test_compute_magnitude(self):
        v = Vector(1,0,0)
        self.assertTrue(v.magnitude() == 1)
        v = Vector(0,1,0)
        self.assertTrue(v.magnitude() == 1)
        v = Vector(0,0,1)
        self.assertTrue(v.magnitude() == 1)
        v = Vector(1,2,3)
        self.assertTrue(v.magnitude() == math.sqrt(14))
        v = Vector(-1,-2,-3)
        self.assertTrue(v.magnitude() == math.sqrt(14))

    def test_normalization(self):
        v = Vector(4,0,0)
        self.assertTrue(v.normalize() == Vector(1,0,0))

        v = Vector(1,2,3)
        self.assertTrue(v.normalize() == Vector(.2672612419124244,.5345224838248488,.8017837257372732))

    def test_dot_product(self):
        v1 = Vector(1,2,3)
        v2 = Vector(2,3,4)
        self.assertTrue(Tuple.dot_product(v1, v2) == 20)
    
    def test_cross_product(self):
        v1 = Vector(1,2,3)
        v2 = Vector(2,3,4)
        self.assertTrue(Tuple.cross_product(v1, v2) == Vector(-1,2,-1))
        self.assertTrue(Tuple.cross_product(v2, v1) == Vector(1,-2,1))

    

    


if __name__ == '__main__':
    unittest.main()