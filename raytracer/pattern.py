from abc import ABC, abstractmethod
from raytracer.tuples import Point
from raytracer.color import Color
from raytracer.shape import IDENTITY, Matrix

import math

class Pattern(ABC):

    def __init__(self, a: Color, b: Color, transform=None):
        self.a = a
        self.b = b
        self.transform = transform if transform else IDENTITY

    def set_pattern_transform(self, transform: Matrix):
        self.transform = transform

    @abstractmethod
    def pattern_at(self, point: Point):
        pass

    def pattern_at_shape(self, object, point: Point):
        object_point = object.transform.inverse().tuple_multiply(point)
        pattern_point = self.transform.inverse().tuple_multiply(object_point)

        return self.pattern_at(pattern_point)



class TestPattern(Pattern):

    BLACK = Color(0,0,0)
    WHITE = Color(1,1,1)

    def __init__(self, a=WHITE, b=BLACK):
        super().__init__(a, b)
        
    
    def pattern_at(self, point: Point) -> Color:
        return Color(point.x, point.y, point.z)


class StripePattern(Pattern):

    def __init__(self, a: Color, b: Color):
        super().__init__(a, b)

    def pattern_at(self, point: Point):
        if math.floor(point.x) % 2 == 0:
            return self.a
        else:
            return self.b
        
class GradientPattern(Pattern):
    def __init__(self, a: Color, b: Color):
        super().__init__(a, b)

    def pattern_at(self, point: Point):
        distance = self.b - self.a
        fraction = point.x - math.floor(point.x)
        return self.a + distance.scale(fraction)
    
class RingPattern(Pattern):
    def __init__(self, a: Color, b: Color):
        super().__init__(a, b)

    def pattern_at(self, point: Point):
        if math.floor(math.sqrt(point.x**2+point.z**2)) % 2 == 0:
            return self.a
        else:
            return self.b

class Checker3DPattern(Pattern):
    def __init__(self, a: Color, b: Color):
        super().__init__(a, b)

    def pattern_at(self, point: Point):
        if (math.floor(point.x) + math.floor(point.y) + math.floor(point.z)) % 2 == 0:
            return self.a
        else:
            return self.b
        
class SolidPattern(Pattern):
    def __init__(self, a: Color, b=Color(0,0,0)):
        super().__init__(a, b)

    def pattern_at(self, point: Point):
        return self.a
