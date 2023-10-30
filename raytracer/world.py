from raytracer.ray import Ray
from raytracer.intersection import Intersection
from raytracer.color import Color
from raytracer.tuples import *
from raytracer.light import *
from raytracer.sphere import *
from raytracer.computations import *
from raytracer.transformations import Scaling





class World:
    def __init__(self):
        self.objects = []
        self.light_source = None

    def contains(self, obj):
        return obj in self.objects
    
    def intersect_world(self, ray):
        xs = []
        for obj in self.objects:
            intersections = obj.intersect(ray)
            xs.extend(intersections)
        
        return sorted(xs, key=lambda x: x.t)
    
    def shade_hit(self, comps: Computations):
        return comps.object.material.lighting(self.light_source, comps.point, comps.eyev, comps.normalv)
    
    def color_at(self, ray):
        intersections = self.intersect_world(ray)
        hit = Intersection.hit(intersections)
        if hit is None:
            return Color(0,0,0)
        comps = prepare_computations(hit, ray)
        return self.shade_hit(comps)

def default_world():
    world = World()
    
    s1 = Sphere(material=Material(Color(.8,1.0,.6), diffuse=.7, specular=.2))
    s2 = Sphere(transform=Scaling(.5,.5,.5))

    world.objects = [s1,s2]

    world.light_source = Point(-10,10,-10).point_light(Color(1,1,1))

    return world
