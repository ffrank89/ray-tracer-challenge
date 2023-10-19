import unittest
from raytracer.tuples import Point, Vector
from raytracer.ray import Ray
from raytracer.sphere import Sphere
from raytracer.intersection import Intersection
from raytracer.transformations import Translation, Scaling
from raytracer.matrix import IDENTITY



class RayTests(unittest.TestCase):
    
    def test_create_and_query_ray(self):
        origin = Point(1,2,3)
        direction = Vector(4,5,6)

        ray = Ray(origin, direction)
        self.assertEqual(ray.origin, origin)
        self.assertEqual(ray.direction, direction)
    
    def test_compute_point_from_distance(self):
        r = Ray(Point(2,3,4), Vector(1,0,0))

        self.assertEqual(r.position(0), Point(2,3,4))
        self.assertEqual(r.position(1), Point(3,3,4))
        self.assertEqual(r.position(-1), Point(1,3,4))
        self.assertEqual(r.position(2.5), Point(4.5,3,4))

    def test_ray_intersect_sphere_at_two_points(self):
        #if the ray originates at 0,0,-5 and passes through the origin
        #it will intersect the unit sphere at (0,0,1) 4 and 6 units away from the rays origin
        r = Ray(Point(0,0,-5), Vector(0,0,1))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 4.0)
        self.assertEqual(xs[1].t, 6.0)

    def test_ray_intersect_sphere_at_tangent(self):
        #hits the top point of the sphere (intersects at one point)
        r = Ray(Point(0,1,-5), Vector(0,0,1))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 5.0)
        self.assertEqual(xs[1].t, 5.0)

    def test_ray_misses_sphere(self):
        r = Ray(Point(0,2,-5), Vector(0,0,1))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(len(xs), 0)
    
    def test_ray_originates_inside_sphere(self):
        r = Ray(Point(0,0,0), Vector(0,0,1))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, -1.0)
        self.assertEqual(xs[1].t, 1.0)
    
    def test_sphere_behind_ray(self):
        #you will still see two intersections, each with a negative value
        r = Ray(Point(0,0,5), Vector(0,0,1))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, -6.0)
        self.assertEqual(xs[1].t, -4.0)

    def test_create_intersection(self):
        s = Sphere()
        i = Intersection(3.5, s)
        self.assertEqual(i.t, 3.5)
        self.assertEqual(i.object, s)
        
    def test_aggregate_intersections(self):
        s = Sphere()
        i1 = Intersection(1, s)
        i2 = Intersection(2, s)
        xs = Intersection.intersections(i1, i2)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 1)
        self.assertEqual(xs[1].t, 2)

    def test_hit_all_intersections_have_positive_t(self):
        s = Sphere()
        i1 = Intersection(1, s)
        i2 = Intersection(2, s)
        xs = Intersection.intersections(i1, i2)
        i = Intersection.hit(xs)
        self.assertEqual(i, i1)

    def test_hit_some_intersections_have_negative_t(self):
        s = Sphere()
        i1 = Intersection(-1, s)
        i2 = Intersection(1, s)
        xs = Intersection.intersections(i1, i2)
        i = Intersection.hit(xs)
        self.assertEqual(i, i2)

    def test_hit_all_intersections_have_negative_t(self):
        s = Sphere()
        i1 = Intersection(-1, s)
        i2 = Intersection(-21, s)
        xs = Intersection.intersections(i1, i2)
        i = Intersection.hit(xs)
        self.assertEqual(i, None)

    def test_hit_always_lowest_nonnegative_intersection(self):
        s = Sphere()
        i1 = Intersection(5, s)
        i2 = Intersection(7, s)
        i3 = Intersection(-3, s)
        i4 = Intersection(2, s)
        xs = Intersection.intersections(i1, i2, i3, i4)
        i = Intersection.hit(xs)
        self.assertEqual(i, i4)

    def test_translating_a_ray(self):
        r = Ray(Point(1,2,3), Vector(0,1,0))
        m = Translation(3,4,5)
        r2 = r.transform(m)
        self.assertEqual(r2.origin, Point(4,6,8))
        self.assertEqual(r2.direction, Vector(0,1,0))

    def test_scaling_a_ray(self):
        r = Ray(Point(1,2,3), Vector(0,1,0))
        m = Scaling(2,3,4)
        r2 = r.transform(m)
        self.assertEqual(r2.origin, Point(2,6,12))
        self.assertEqual(r2.direction, Vector(0,3,0))

    def test_sphere_default_transformation(self):
        s = Sphere()
        self.assertEqual(s.transform, IDENTITY)

    def test_changing_spheres_transformation(self):
        s = Sphere()
        t = Translation(2,3,4)
        s.set_transform(t)
        self.assertEqual(s.transform, t)
    
    def test_intersecting_scaled_sphere_with_ray(self):
        r = Ray(Point(0,0,-5), Vector(0,0,1))
        s = Sphere()
        s.set_transform(Scaling(2,2,2))
        xs = s.intersect(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 3)
        self.assertEqual(xs[1].t, 7)
    
    def test_intersecting_translated_sphere_with_ray(self):
        r = Ray(Point(0,0,-5), Vector(0,0,1))
        s = Sphere()
        s.set_transform(Translation(5,0,0))

        xs = s.intersect(r)
        self.assertEqual(len(xs), 0)

    



if __name__ == "__main__":
    unittest.main()
