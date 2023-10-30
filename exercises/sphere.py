from raytracer.tuples import *
from raytracer.canvas import *
from raytracer.color import *
from raytracer.matrix import *
from raytracer.transformations import *
from raytracer.sphere import *
from raytracer.ray import *
from raytracer.intersection import *
from raytracer.material import *
from raytracer.light import *
from math import pi

def main():

    
    
    ray_origin = Point(0, 0, -5)
    wall_z = 10
    wall_size = 7.0

    canvas_pixels = 20

    pixel_size = wall_size / canvas_pixels

    #half wall
    half = wall_size / 2
    #half variable describes the minimum and maximum x and y coordinates of your wall

    canvas = Canvas(canvas_pixels, canvas_pixels)

    shape = Sphere()

    shape.material.color = Color(1,.2,1)
    
    light_position = Point(-10, 10, -10)
    light_color = Color(1,1,1)
    light = light_position.point_light(light_color)

    #for each row of pixels in the canvas
    for y in range(canvas_pixels):
        #compute the world y coordinate
        world_y = half - pixel_size * y
        #for each pixel in the row
        for x in range(canvas_pixels):
            #compute the world x coordinate
            world_x = -half + pixel_size * x

            position = Point(world_x, world_y, wall_z)
            position = position - ray_origin
            r = Ray(ray_origin, position.normalize())

            #shape.transform = Scaling(1, .5, 1)

            xs = shape.intersect(r)

            if Intersection.hit(xs):
                hit = Intersection.hit(xs)
                point = r.position(hit.t)
                normal = hit.object.normal_at(point)
                eye = r.direction.scale(-1)
                color = hit.object.material.lighting(light, point, eye, normal)
                canvas.write_pixel(x, y, color)
        


    ppm_data = canvas.canvas_to_ppm()
    with open('output.ppm', 'w') as file:
        file.write(ppm_data)


if __name__ == "__main__":
    main()