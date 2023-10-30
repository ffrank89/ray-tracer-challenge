import unittest
from raytracer.tuples import *
from raytracer.ray import *
from raytracer.sphere import *
from raytracer.intersection import *
from raytracer.computations import *


class TestComputations(unittest.TestCase):
    
    def test_create_comps(self):
        r = Ray(Point(0,0,-5), Vector(0,0,1))
        i = Intersection(4, Sphere())

        comps = prepare_computations(i, r)
        self.assertEqual(comps.t, i.t)
        self.assertEqual(comps.object, i.object)
        self.assertEqual(comps.point, Point(0,0,-1))
        self.assertEqual(comps.eyev, Vector(0,0,-1))
        self.assertEqual(comps.normalv, Vector(0,0,-1))
    
    def test_intersection_outside(self):
        r = Ray(Point(0,0,-5), Vector(0,0,1))
        i = Intersection(4, Sphere())
        comps = prepare_computations(i, r)
        self.assertEqual(comps.inside, False)

    def test_intersection_inside(self):
        r = Ray(Point(0,0,0), Vector(0,0,1))
        i = Intersection(1, Sphere())

        comps = prepare_computations(i, r)
        self.assertEqual(comps.point, Point(0,0,1))
        self.assertEqual(comps.eyev, Vector(0,0,-1))
        self.assertEqual(comps.inside, True)

        #normal would have been (0,0,1) but it is inverted
        self.assertEqual(comps.normalv, Vector(0,0,-1))

    



if __name__ == "__main__":
    unittest.main()