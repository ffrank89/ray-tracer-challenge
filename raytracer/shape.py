from abc import ABC, abstractmethod
from raytracer.tuples import Point, Vector
from raytracer.ray import Ray
from raytracer.matrix import Matrix, IDENTITY
from raytracer.material import Material

class Shape(ABC):

    def __init__(self, transform=None, material=None):
        self.transform = transform if transform else IDENTITY
        self.material = material if material else Material()

    def intersect(self, ray: Ray):
        local_ray = ray.transform(self.transform.inverse())
        return self.local_intersect(local_ray)
    
    def normal_at(self, point: Point):
        local_point = self.transform.inverse().tuple_multiply(point)
        local_normal = self.local_normal_at(local_point)
        world_normal = self.transform.inverse().transpose().tuple_multiply(local_normal)
        world_normal.w = 0
        return world_normal.normalize()

    @abstractmethod
    def local_normal_at(self, point: Point):
        pass

    @abstractmethod
    def local_intersect(self, local_ray):
        pass

    def set_transform(self, transform: Matrix):
        self.transform = transform


class TestShape(Shape):

    def __init__(self, transform=None, material=None):
        super().__init__(transform, material)
        self.saved_ray = None

    def local_intersect(self, local_ray):
        # Implement intersection logic for a sphere here
        self.saved_ray = local_ray
        return
    
    def local_normal_at(self, point: Point):
        return Vector(point.x, point.y, point.z)