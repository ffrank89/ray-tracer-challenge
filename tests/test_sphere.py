import unittest
from raytracer.tuples import Point, Vector
from raytracer.ray import Ray
from raytracer.sphere import Sphere
from raytracer.intersection import Intersection
from raytracer.transformations import Translation, Scaling, Rotation_Z, Rotation_Y, Rotation_X
from raytracer.matrix import IDENTITY

from math import sqrt, pi

class SphereTests(unittest.TestCase):

    def test_normal_at_x_axis_point(self):
        s = Sphere()
        n = s.normal_at(Point(1,0,0))
        self.assertEqual(n, Vector(1,0,0))
    
    def test_normal_at_y_axis_point(self):
        s = Sphere()
        n = s.normal_at(Point(0,1,0))
        self.assertEqual(n, Vector(0,1,0))

    def test_normal_at_y_axis_point(self):
        s = Sphere()
        n = s.normal_at(Point(0,0,1))
        self.assertEqual(n, Vector(0,0,1))

    def test_normal_on_sphere_at_nonaxial_point(self):
        s = Sphere()
        n = s.normal_at(Point(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3))
        self.assertEqual(n, Vector(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3))

    def test_normal_is_normalized(self):
        s = Sphere()
        n = s.normal_at(Point(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3))
        self.assertTrue(n, n.normalize())

    def test_compute_normal_on_translated_sphere(self):
        s = Sphere()
        s.set_transform(Translation(0,1,0))
        n = s.normal_at(Point(0, 1.70711, -0.70711))
        self.assertEqual(n, Vector(0, 0.70711, -0.70711))

    def test_compute_normal_on_transformed_sphere(self):
        s = Sphere()
        m = Scaling(1, 0.5, 1).matrix_multiply(Rotation_Z(pi/5))
    
        s.set_transform(m)

        n = s.normal_at(Point(0, sqrt(2)/2, -sqrt(2)/2))
        self.assertEqual(n, Vector(0, .97014, -.24254))

    
    
if __name__ == "__main__":
    unittest.main()