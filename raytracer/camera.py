from math import pi, tan
from raytracer.matrix import IDENTITY
from raytracer.tuples import Point
from raytracer.ray import Ray
from raytracer.canvas import *
from raytracer.world import *



class Camera():

    def __init__(self, hsize, vsize, field_of_view):
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        self.transform = IDENTITY

        half_view = tan(self.field_of_view / 2)
        aspect_ratio = self.hsize / self.vsize

        if aspect_ratio >= 1:
            self.half_width = half_view
            self.half_height = half_view / aspect_ratio
        else:
            self.half_width = half_view * aspect_ratio
            self.half_height = half_view
        
        self.pixel_size = (self.half_width * 2) / self.hsize

    
    def ray_for_pixel(self, px, py):

        #the offset from the edge of the canvas to the pixel's center
        xoffset = (px + .5) * self.pixel_size
        yoffset = (py + .5) * self.pixel_size

        #the untransformed coordinates of the pixel in world space
        #remember that the camera looks toward -z, so +x is to the left
        world_x = self.half_width - xoffset
        world_y = self.half_height - yoffset

        #using the camera matrix, transform the canvas point and the origin, 
        #and then compute the ray's direction vector
        #canvas is at z=-1
        pixel = self.transform.inverse().tuple_multiply(Point(world_x, world_y, -1))
        origin = self.transform.inverse().tuple_multiply(Point(0, 0, 0))
        direction = (pixel - origin).normalize()
        return Ray(origin, direction)
    
    def render(self, world: World):
        
        image = Canvas(self.hsize, self.vsize)

        for y in range(self.vsize):
            for x in range(self.hsize):
                ray = self.ray_for_pixel(x, y)
                color = world.color_at(ray)
                image.write_pixel(x, y, color)
        
        return image






    