from raytracer.matrix import *
from raytracer.tuples import Point, Vector

from math import sin, cos


class Translation(Matrix):

    def __init__(self, x, y, z):
        super().__init__(4, None)
        translation_matrix = [
            [1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]
        ]
        self.data = translation_matrix

class Scaling(Matrix):
    def __init__(self, x, y, z):
        super().__init__(4, None)
        translation_matrix = [
            [x, 0, 0, 0],
            [0, y, 0, 0],
            [0, 0, z, 0],
            [0, 0, 0, 1]
        ]
        self.data = translation_matrix

class Rotation_X(Matrix):
    def __init__(self, radians):
        super().__init__(4, None)
        translation_matrix = [
            [1, 0, 0, 0],
            [0, cos(radians), -sin(radians), 0],
            [0, sin(radians), cos(radians), 0],
            [0, 0, 0, 1]
        ]
        self.data = translation_matrix

class Rotation_Y(Matrix):
    def __init__(self, radians):
        super().__init__(4, None)
        translation_matrix = [
            [cos(radians), 0, sin(radians), 0],
            [0, 1, 0, 0],
            [-sin(radians), 0, cos(radians), 0],
            [0, 0, 0, 1]
        ]
        self.data = translation_matrix

class Rotation_Z(Matrix):
    def __init__(self, radians):
        super().__init__(4, None)
        translation_matrix = [
            [cos(radians), -sin(radians), 0, 0],
            [sin(radians), cos(radians), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
        self.data = translation_matrix

class Shearing(Matrix):
    def __init__(self, xy, xz, yx, yz, zx, zy):
        super().__init__(4, None)
        translation_matrix = [
            [1, xy, xz, 0],
            [yx, 1, yz, 0],
            [zx, zy, 1, 0],
            [0, 0, 0, 1]
        ]
        self.data = translation_matrix

def view_transform(fromm: Point, to: Point, up: Vector):
    forward = (to - fromm).normalize()
    upn = up.normalize()
    left = Tuple.cross_product(forward, upn)
    true_up = Tuple.cross_product(left, forward)
    orientation_data = [
        [left.x, left.y, left.z, 0],
        [true_up.x, true_up.y, true_up.z, 0],
        [-forward.x, -forward.y, -forward.z, 0],
        [0, 0, 0, 1]
    ]
    orientation = Matrix(4, orientation_data)
    return orientation.matrix_multiply(Translation(-fromm.x,-fromm.y,-fromm.z))