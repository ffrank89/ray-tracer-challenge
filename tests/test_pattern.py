import unittest
from raytracer.shape import *
from raytracer.sphere import *
from raytracer.color import *
from raytracer.pattern import *
from raytracer.light import *
from raytracer.transformations import *



class TestPatterns(unittest.TestCase):
    

    def test_creating_stripe_pattern(self):
        BLACK = Color(0,0,0)
        WHITE = Color(1,1,1)
        pattern = StripePattern(WHITE, BLACK)
        self.assertEqual(pattern.a, WHITE)
        self.assertEqual(pattern.b, BLACK)

    def test_stripe_pattern_constant_in_y(self):
        BLACK = Color(0,0,0)
        WHITE = Color(1,1,1)
        pattern = StripePattern(WHITE, BLACK)
        self.assertEqual(pattern.pattern_at(Point(0,0,0)), WHITE)
        self.assertEqual(pattern.pattern_at(Point(0,1,0)), WHITE)
        self.assertEqual(pattern.pattern_at(Point(0,2,0)), WHITE)

    def test_stripe_pattern_constant_in_z(self):
        BLACK = Color(0,0,0)
        WHITE = Color(1,1,1)
        pattern = StripePattern(WHITE, BLACK)
        self.assertEqual(pattern.pattern_at(Point(0,0,0)), WHITE)
        self.assertEqual(pattern.pattern_at(Point(0,0,1)), WHITE)
        self.assertEqual(pattern.pattern_at(Point(0,0,2)), WHITE)

    def test_stripe_pattern_alternates_in_y(self):
        BLACK = Color(0,0,0)
        WHITE = Color(1,1,1)
        pattern = StripePattern(WHITE, BLACK)
        self.assertEqual(pattern.pattern_at(Point(0,0,0)), WHITE)
        self.assertEqual(pattern.pattern_at(Point(0.9,0,0)), WHITE)
        self.assertEqual(pattern.pattern_at(Point(1,0,0)), BLACK)
        self.assertEqual(pattern.pattern_at(Point(-.1,0,0)), BLACK)
        self.assertEqual(pattern.pattern_at(Point(-1,0,0)), BLACK)
        self.assertEqual(pattern.pattern_at(Point(-1.1,0,0)), WHITE)

    def test_lighting_with_pattern_applied(self):
        BLACK = Color(0,0,0)
        WHITE = Color(1,1,1)
        m = Material()
        m.pattern = StripePattern(WHITE, BLACK)
        m.ambient = 1
        m.diffuse = 0
        m.specular = 0
        eyev = Vector(0,0,-1)
        normalv = Vector(0,0,-1)
        light = Point(0,0,-10).point_light(Color(1,1,1))
        
        c1 = m.lighting(Sphere(), light, Point(.9,0,0), eyev, normalv, False)
        c2 = m.lighting(Sphere(), light, Point(1.1,0,0), eyev, normalv, False)

        self.assertEqual(c1, Color(1,1,1))
        self.assertEqual(c2, Color(0,0,0))
    
    def test_stripes_with_object_transformation(self):
        BLACK = Color(0,0,0)
        WHITE = Color(1,1,1)
        pattern = StripePattern(WHITE, BLACK)

        object = Sphere()
        object.set_transform(Scaling(2,2,2))
        c = pattern.pattern_at_shape(object, Point(1.5,0,0))
        self.assertEquals(c, WHITE)
    
    def test_stripes_with_pattern_transformation(self):
        BLACK = Color(0,0,0)
        WHITE = Color(1,1,1)
        pattern = StripePattern(WHITE, BLACK)
        pattern.set_pattern_transform(Scaling(2,2,2))

        object = Sphere()
        c = pattern.pattern_at_shape(object, Point(1.5,0,0))
        self.assertEquals(c, WHITE)

    def test_stripes_with_pattern_transformation(self):
        BLACK = Color(0,0,0)
        WHITE = Color(1,1,1)
        pattern = StripePattern(WHITE, BLACK)
        pattern.set_pattern_transform(Translation(.5,0,0))

        object = Sphere()
        object.set_transform(Scaling(2,2,2))

        c = pattern.pattern_at_shape(object, Point(1.5,0,0))
        self.assertEquals(c, WHITE)

    def test_default_pattern_transformation(self):
        pattern = TestPattern()
        self.assertEqual(pattern.transform, IDENTITY)
    
    def test_assigning_transformation(self):
        pattern = TestPattern()
        pattern.set_pattern_transform(Translation(1,2,3))
        self.assertEqual(pattern.transform, Translation(1,2,3))

    def test_pattern_with_object_transformation(self):
        shape = Sphere()
        shape.set_transform(Scaling(2,2,2))
        pattern = TestPattern()
        c = pattern.pattern_at_shape(shape, Point(2,3,4))
        self.assertEqual(c, Color(1,1.5,2))

    def test_pattern_with_pattern_transformation(self):
        shape = Sphere()
        pattern = TestPattern()
        pattern.set_pattern_transform(Scaling(2,2,2))
        c = pattern.pattern_at_shape(shape, Point(2,3,4))
        self.assertEqual(c, Color(1,1.5,2))

    def test_pattern_with_both_transformations(self):
        shape = Sphere()
        shape.set_transform(Scaling(2,2,2))
        pattern = TestPattern()
        pattern.set_pattern_transform(Translation(.5,1,1.5))
        c = pattern.pattern_at_shape(shape, Point(2.5,3,3.5))
        self.assertEqual(c, Color(.75,.5,.25))

    def test_linear_gradient(self):
        BLACK = Color(0,0,0)
        WHITE = Color(1,1,1)
        pattern = GradientPattern(WHITE, BLACK)
        self.assertEqual(pattern.pattern_at(Point(0,0,0)), WHITE)
        self.assertEqual(pattern.pattern_at(Point(0.25,0,0)), Color(.75,.75,.75))
        self.assertEqual(pattern.pattern_at(Point(0.5,0,0)), Color(.5,.5,.5))
        self.assertEqual(pattern.pattern_at(Point(0.75,0,0)), Color(.25,.25,.25))

    def test_ring_pattern(self):
        BLACK = Color(0,0,0)
        WHITE = Color(1,1,1)
        pattern = RingPattern(WHITE, BLACK)
        self.assertEqual(pattern.pattern_at(Point(0,0,0)), WHITE)
        self.assertEqual(pattern.pattern_at(Point(1,0,0)), BLACK)
        self.assertEqual(pattern.pattern_at(Point(0,0,1)), BLACK)
        self.assertEqual(pattern.pattern_at(Point(0.708,0,0.708)), BLACK)

    def test_3d_checker_pattern(self):
        BLACK = Color(0,0,0)
        WHITE = Color(1,1,1)
        pattern = Checker3DPattern(WHITE, BLACK)
        #checkers repeat in x
        self.assertEqual(pattern.pattern_at(Point(0,0,0)), WHITE)
        self.assertEqual(pattern.pattern_at(Point(.99,0,0)), WHITE)
        self.assertEqual(pattern.pattern_at(Point(1.01,0,0)), BLACK)

        #checkers repeat in y
        self.assertEqual(pattern.pattern_at(Point(0,0,0)), WHITE)
        self.assertEqual(pattern.pattern_at(Point(0,0.99,0)), WHITE)
        self.assertEqual(pattern.pattern_at(Point(0,1.01,0)), BLACK)

        #checkers repeat in z
        self.assertEqual(pattern.pattern_at(Point(0,0,0)), WHITE)
        self.assertEqual(pattern.pattern_at(Point(0,0,0.99)), WHITE)
        self.assertEqual(pattern.pattern_at(Point(0,0,1.01)), BLACK)
    
        




if __name__ == "__main__":
    unittest.main()