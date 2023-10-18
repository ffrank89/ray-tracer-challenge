from raytracer.tuples import Point, Vector
from raytracer.matrix import Matrix

class Ray:

    def __init__(self, origin: Point, direction: Vector):
        self.origin = origin
        self.direction = direction

    def position(self, t):
        return self.origin + self.direction.scale(t)
    
    def transform(self, matrix: Matrix):
        t_origin = matrix.tuple_multiply(self.origin)
        t_direction = matrix.tuple_multiply(self.direction)

        return Ray(t_origin, t_direction)

