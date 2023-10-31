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
from raytracer.camera import *
from raytracer.computations import *
from raytracer.world import *

from math import pi

def main():

    #floor is an extremely flattened sphere with a matte texture
    floor = Sphere(transform=Scaling(10,.01,10), material=Material(color=Color(1, .9, .9), specular=0))

    #left_wall has the same scale and color as the floor, but is also rotated and translated into place
    lwt = Translation(0,0,5).matrix_multiply(Rotation_Y(-pi/4)).matrix_multiply(Rotation_X(pi/2)).matrix_multiply(Scaling(10,.01,10))
    left_wall = Sphere(material=floor.material, transform=lwt)

    #right wall same deal but opposite rotation
    rwt = Translation(0,0,5).matrix_multiply(Rotation_Y(pi/4)).matrix_multiply(Rotation_X(pi/2)).matrix_multiply(Scaling(10,.01,10))
    right_wall = Sphere(material=floor.material, transform=rwt)

    #middle sphere is unit sphere translated upward and colored green
    middle = Sphere(transform=Translation(-.5,1,.5), material=Material(color=Color(.1,1,.5), diffuse=.7, specular=.3))

    #Smaller green sphere on the right is scaled in half
    right = Sphere(transform=Translation(1.5,.5,-.5).matrix_multiply(Scaling(.5,.5,.5)), material=Material(color=Color(.5,1,.1), diffuse=.7, specular=.3))

    #smallest sphere is scaled by a third before being translated
    left = Sphere(transform=Translation(-1.5,.33,-.75).matrix_multiply(Scaling(.33,.33,.33)), material=Material(color=Color(1,.8,.1), diffuse=.7, specular=.3))

    objects = []
    objects.append(floor)
    objects.append(left_wall)
    objects.append(right_wall)
    objects.append(middle)
    objects.append(right)
    objects.append(left)

    light_source = Point(-10,10,-10).point_light(Color(1,1,1))
    world = World()
    world.objects = objects
    world.light_source = light_source
    camera = Camera(200, 200, pi/3)

    camera.transform = view_transform(Point(0, 1.5, -5), Point(0,1,0), Vector(0,1,0))

    canvas = camera.render(world)

    ppm_data = canvas.canvas_to_ppm()
    with open('output.ppm', 'w') as file:
        file.write(ppm_data)


if __name__ == "__main__":
    main()