from raytracer.tuples import Point, Vector, Tuple
from raytracer.intersection import Intersection
from raytracer.ray import Ray


class Computations:

    def __init__(self, t: int, object, point: Point, eyev: Vector, normalv: Vector, inside: bool):
        self.t = t
        self.object = object
        self.point = point
        self.eyev = eyev
        self.normalv = normalv
        self.inside = inside


def prepare_computations(i: Intersection, r: Ray):
    t = i.t
    object = i.object
    point = r.position(t)
    eyev = r.direction.scale(-1)
    normalv = object.normal_at(point)

    if Tuple.dot_product(normalv, eyev) < 0:
        inside = True
        normalv = normalv.scale(-1)
    else:
        inside = False

    comps = Computations(t,object,point,eyev,normalv,inside)
    return comps
