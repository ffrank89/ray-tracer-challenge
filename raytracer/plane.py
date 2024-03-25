from abc import ABC, abstractmethod
from raytracer.tuples import Point, Vector, Tuple
from raytracer.ray import Ray
from raytracer.intersection import Intersection
from raytracer.matrix import Matrix, IDENTITY
from raytracer.material import Material
from raytracer.shape import Shape


class Plane(Shape):

    def __init__(self, transform=None, material=None):
        # self.transform = transform if transform else IDENTITY
        # self.material = material if material else Material()

        super().__init__(transform, material)

    def local_normal_at(self, point: Point):
        return Vector(0,1,0)
    
    def local_intersect(self, ray: Ray):
        EPSILON = 0.000000000001
        if abs(ray.direction.y) < EPSILON:
            return []
        
        t = Intersection(-ray.origin.y / ray.direction.y, self)

        return Intersection.intersections(t)
        
        
