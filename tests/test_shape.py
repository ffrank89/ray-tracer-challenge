import unittest
from raytracer.shape import *
from raytracer.material import *
from raytracer.transformations import *
from raytracer.ray import Ray
from math import pi, sqrt



class TestShapes(unittest.TestCase):

    def test_default_transformation(self):
        s = TestShape()
        self.assertEqual(s.transform, IDENTITY)

    def test_default_material(self):
        s = TestShape()
        self.assertEqual(s.material, Material())
        
    def test_assigning_material(self):
        s = TestShape()
        m = Material()
        m.ambient = 1
        s.material = m
        self.assertEqual(s.material, m)

    def test_intersecting_scaled_shape_with_ray(self):
        r = Ray(Point(0,0,-5), Vector(0,0,1))
        s = TestShape()
        s.set_transform(Scaling(2,2,2))
        s.intersect(r)
        self.assertEqual(s.saved_ray.origin, Point(0,0,-2.5))
        self.assertEqual(s.saved_ray.direction, Vector(0,0,.5))

    def test_intersecting_translated_shape_with_ray(self):
        r = Ray(Point(0,0,-5), Vector(0,0,1))
        s = TestShape()
        s.set_transform(Translation(5,0,0))
        s.intersect(r)
        self.assertEqual(s.saved_ray.origin, Point(-5,0,-5))
        self.assertEqual(s.saved_ray.direction, Vector(0,0,1))

    def test_normal_on_translated_shape(self):
        s = TestShape()
        s.set_transform(Translation(0,1,0))
        n = s.normal_at(Point(0,1.70711,-.70711))
        self.assertEqual(n, Vector(0,.70711,-.70711))

    def test_normal_on_transformed_shape(self):
        s = TestShape()
        m = Scaling(1,.5,1).matrix_multiply(Rotation_Z(pi/5))
        s.set_transform(m)
        n = s.normal_at(Point(0,(sqrt(2)/2),-(sqrt(2)/2)))
        self.assertEqual(n, Vector(0,.97014,-.24254))



if __name__ == "__main__":
    unittest.main()