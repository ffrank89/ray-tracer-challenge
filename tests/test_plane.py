import unittest
from raytracer.plane import Plane
from raytracer.tuples import *
from raytracer.ray import *


class TestPlane(unittest.TestCase):

    def test_normal_is_constant(self):
        p = Plane()

        n1 = p.local_normal_at(Point(0,0,0))
        n2 = p.local_normal_at(Point(10,0,-10))
        n3 = p.local_normal_at(Point(-5,0,150))

        self.assertEqual(n1, Vector(0,1,0))
        self.assertEqual(n2, Vector(0,1,0))
        self.assertEqual(n3, Vector(0,1,0))

    def test_intersect_parallel_ray(self):
        p = Plane()
        r = Ray(Point(0,10,0), Vector(0,0,1))
        xs = p.local_intersect(r)
        self.assertEqual(xs, [])

    def test_intersect_above_ray(self):
        p = Plane()
        r = Ray(Point(0,1,0), Vector(0,-1,0))
        xs = p.local_intersect(r)
        print(xs)
        print(xs[0])

        self.assertEqual(1, len(xs))
        self.assertEqual(1, xs[0].t)
        self.assertEqual(p, xs[0].object)

    


if __name__ == "__main__":
    unittest.main()