import unittest
from math import pi, tan, sqrt
from raytracer.tuples import Point, Vector
from raytracer.matrix import IDENTITY
from raytracer.transformations import Rotation_Y, Translation, view_transform
from raytracer.world import *
from raytracer.camera import *


class Test_Camera(unittest.TestCase):
    
    def test_creating_camera(self):
        hsize = 160
        vsize = 120
        field_of_view = pi / 2
        c = Camera(hsize,vsize,field_of_view)
        self.assertEqual(c.hsize, 160)
        self.assertEqual(c.vsize, 120)
        self.assertEqual(c.field_of_view, pi/2)
        self.assertEqual(c.transform, IDENTITY)
    
    def test_horizontal_canvas(self):
        c = Camera(200,125,pi/2)
        self.assertAlmostEqual(c.pixel_size, 0.01)
    
    def test_vertical_canvas(self):
        c = Camera(125,200,pi/2)
        self.assertAlmostEqual(c.pixel_size, 0.01)

    def test_ray_through_center_of_canvas(self):
        c = Camera(201,101, pi/2)
        r = c.ray_for_pixel(100,50)
        self.assertEqual(r.origin, Point(0,0,0))
        self.assertEqual(r.direction, Vector(0,0,-1))
    
    def test_ray_through_corner_of_canvas(self):
        c = Camera(201,101, pi/2)
        r = c.ray_for_pixel(0,0)
        self.assertEqual(r.origin, Point(0,0,0))
        self.assertEqual(r.direction, Vector(0.66519,0.33259,-.66851))

    def test_ray_when_camera_is_transformed(self):
        c = Camera(201,101, pi/2)
        c.transform = Rotation_Y(pi/4).matrix_multiply(Translation(0, -2, 5))
        r = c.ray_for_pixel(100,50)
        self.assertEqual(r.origin, Point(0,2,-5))
        self.assertEqual(r.direction, Vector(sqrt(2)/2,0,-sqrt(2)/2))

    def test_rendering_a_world_with_a_camera(self):
        w = default_world()
        c = Camera(11,11,pi/2)
        fromm = Point(0,0,-5)
        to = Point(0,0,0)
        up = Vector(0,1,0)
        c.transform = view_transform(fromm, to, up)
        image = c.render(w)
        self.assertEqual(image.pixel_at(5, 5), Color(.38066,.47583,.2855))
    





if __name__ == "__main__":
    unittest.main()