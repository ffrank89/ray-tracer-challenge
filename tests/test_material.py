import unittest
from raytracer.material import Material
from raytracer.tuples import *
from raytracer.sphere import *
from raytracer.matrix import *
from raytracer.color import *

class TestMaterial(unittest.TestCase):

    def test_default_material(self):
        m = Material()
        self.assertEqual(m.color, Color(1, 1, 1))
        self.assertEqual(m.ambient, .1)
        self.assertEqual(m.diffuse, .9)
        self.assertEqual(m.specular, .9)
        self.assertEqual(m.shininess, 200.0)
    
    def test_sphere_default_material(self):
        s = Sphere()
        m = s.material
        self.assertEqual(m, Material())

    def test_sphere_assigned_material(self):
        s = Sphere()
        m = Material(ambient=1)
        s.material = m
        self.assertEqual(s.material, m)
    
    def test_eye_between_light_and_surface(self):
        m = Material()
        position = Point(0,0,0)
        #
        eyev = Vector(0,0,-1)
        normalv = Vector(0,0,-1)
        light = Point(0,0,-10).point_light(Color(1,1,1))
        result = m.lighting(light, position, eyev, normalv)
        self.assertEqual(result, Color(1.9,1.9,1.9))

    def test_eye_between_light_and_surface_eye_offset_45degrees(self):
        m = Material()
        position = Point(0,0,0)
        eyev = Vector(0, sqrt(2)/2, sqrt(2)/2)
        normalv = Vector(0,0,-1)
        light = Point(0,0,-10).point_light(Color(1,1,1))
        result = m.lighting(light, position, eyev, normalv)
        self.assertEqual(result, Color(1.0,1.0,1.0))

    def test_eye_opposite_surface_light_offset_45degrees(self):
        m = Material()
        position = Point(0,0,0)
        eyev = Vector(0, 0, -1)
        normalv = Vector(0,0,-1)
        light = Point(0,10,-10).point_light(Color(1,1,1))
        result = m.lighting(light, position, eyev, normalv)
        self.assertEqual(result, Color(.7364,.7364,.7364))

    def test_eye_in_path_of_reflection_vector(self):
        m = Material()
        position = Point(0,0,0)
        eyev = Vector(0, -sqrt(2)/2, -sqrt(2)/2)
        normalv = Vector(0,0,-1)
        light = Point(0,10,-10).point_light(Color(1,1,1))
        result = m.lighting(light, position, eyev, normalv)
        self.assertEqual(result, Color(1.6364,1.6364,1.6364))

    def test_light_behind_surface(self):
        m = Material()
        position = Point(0,0,0)
        eyev = Vector(0, 0, -1)
        normalv = Vector(0,0,-1)
        light = Point(0,0,10).point_light(Color(1,1,1))
        result = m.lighting(light, position, eyev, normalv)
        self.assertEqual(result, Color(.1,.1,.1))

    def test_lighting_within_surface_of_shadow(self):
        m = Material()
        position = Point(0,0,0)
        eyev = Vector(0,0,-1)
        normalv = Vector(0,0,-1)
        light = Point(0,0,-10).point_light(Color(1,1,1))
        in_shadow = True
        result = m.lighting(light, position, eyev, normalv, in_shadow)
        self.assertEqual(result, Color(.1,.1,.1))

    


    





if __name__ == "__main__":
    unittest.main()