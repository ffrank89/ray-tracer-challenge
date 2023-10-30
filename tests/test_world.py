import unittest
from raytracer.world import *
from raytracer.computations import *

class TestWorld(unittest.TestCase):
    def test_world(self):
        w = World()
        self.assertEqual(w.objects, [])
        self.assertEquals(w.light_source, None)
    
    def test_default_world(self):

        light = Point(-10,10,-10).point_light(Color(1,1,1))
        s1 = Sphere()
        material = Material(Color(.8,1.0,.6), diffuse=.7, specular=.2)
        s1.material = material

        s2 = Sphere()
        transform = Scaling(.5,.5,.5)
        s2.transform = transform

        w = default_world()
        self.assertEqual(w.light_source, light)
        self.assertTrue(w.contains(s1))
        self.assertTrue(w.contains(s2))
    
    def test_intersect_default_with_ray(self):
        w = default_world()
        r = Ray(Point(0,0,-5), Vector(0,0,1))
        xs = w.intersect_world(r)
        self.assertEqual(len(xs), 4)
        self.assertEqual(xs[0].t, 4)
        self.assertEqual(xs[1].t, 4.5)
        self.assertEqual(xs[2].t, 5.5)
        self.assertEqual(xs[3].t, 6)

    def test_shading_intersection(self):
        w = default_world()
        r = Ray(Point(0,0,-5), Vector(0,0,1))
        shape = w.objects[0]
        i = Intersection(4, shape)

        comps = prepare_computations(i,r)
        c = w.shade_hit(comps)
        self.assertEqual(c, Color(.38066,.47583,.2855))

    def test_shading_intersection_from_inside(self):
        w = default_world()
        w.light_source = Point(0,.25,0).point_light(Color(1,1,1))
        r = Ray(Point(0,0,0), Vector(0,0,1))
        shape = w.objects[1]
        i = Intersection(.5, shape)

        comps = prepare_computations(i,r)
        c = w.shade_hit(comps)
        self.assertEqual(c, Color(.90498,.90498,.90498))

    def test_color_at_ray_miss(self):
        w = default_world()
        r = Ray(Point(0,0,-5), Vector(0,1,0))
        c = w.color_at(r)
        self.assertEquals(c, Color(0,0,0))

    def test_color_at_ray_hit(self):
        w = default_world()
        r = Ray(Point(0,0,-5), Vector(0,0,1))
        c = w.color_at(r)
        self.assertEquals(c, Color(0.38066,0.47583,0.2855))

    def test_color_with_intersection_behind_ray(self):
        w = default_world()

        outer = w.objects[0]
        outer.material.ambient = 1
        inner = w.objects[1]
        inner.material.ambient = 1

        r = Ray(Point(0,0,.75), Vector(0,0,-1))
        c = w.color_at(r)
        self.assertEquals(c, inner.material.color)
    




if __name__ == "__main__":
    unittest.main()