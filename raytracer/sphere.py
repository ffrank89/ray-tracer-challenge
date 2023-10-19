from raytracer.tuples import Point, Vector, Tuple
from raytracer.ray import Ray
from raytracer.intersection import Intersection
from raytracer.matrix import Matrix, IDENTITY

from math import sqrt
class Sphere:

    def __init__(self, center=None, radius=None, transform=None):
        self.center = center if center else Point(0, 0, 0)
        self.radius = radius if radius else 1.0
        self.transform = transform if transform else IDENTITY

    
    def set_transform(self, transform: Matrix):
        self.transform = transform

    def intersect(self, ray: Ray):
        ray = ray.transform(self.transform.inverse())

        sphere_to_ray = ray.origin - self.center
        a = Tuple.dot_product(ray.direction, ray.direction)
        b = 2 * Tuple.dot_product(ray.direction, sphere_to_ray)
        c = Tuple.dot_product(sphere_to_ray, sphere_to_ray) - 1

        discriminant = b**2 - 4 * a * c

        if discriminant < 0:
            return []

        t1 = Intersection((-b - sqrt(discriminant)) / (2*a), self)
        t2 = Intersection((-b + sqrt(discriminant)) / (2*a), self)

        return Intersection.intersections(t1, t2)
    
    def normal_at(self, point: Point):
        #you find the normal by taking the point in question and subtracting the origin of the sphere
        point - Point(0, 0, 0)
        return point.normalize()

        

