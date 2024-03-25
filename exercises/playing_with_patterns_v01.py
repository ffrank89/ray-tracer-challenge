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
from raytracer.plane import *
from raytracer.pattern import *

from math import pi

def create_hexagonal_wall(angle, distance):

    wall = Plane()
    pattern = StripePattern(Color(0,0,0), Color(1,1,1))
    wall_transform = Translation(0, 0, distance) \
        .matrix_multiply(Rotation_Y(angle)) \
        .matrix_multiply(Rotation_X(-pi/2))
    wall.set_transform(wall_transform)
    wall.material = Material(color=Color(1, 0.9, 0.9), specular=0, pattern=pattern)  # Wall material
    return wall

def main():

    #floor is an extremely flattened sphere with a matte texture
    floor = Plane(transform=Scaling(10,.01,10), material=Material(color=Color(1, .9, .9), specular=0))

    #middle sphere is unit sphere translated upward and colored green
    middle = Sphere(transform=Translation(-.5,1,.5), material=Material(color=Color(.1,1,.5), diffuse=.7, specular=.3))

    #Smaller green sphere on the right is scaled in half
    right = Sphere(transform=Translation(1.5,.5,-.5).matrix_multiply(Scaling(.5,.5,.5)), material=Material(color=Color(.5,1,.1), diffuse=.7, specular=.3))

    #smallest sphere is scaled by a third before being translated
    left = Sphere(transform=Translation(-1.5,.33,-.75).matrix_multiply(Scaling(.33,.33,.33)), material=Material(color=Color(1,.8,.1), diffuse=.7, specular=.3))

    hexagon_walls = []
    wall_distance = 10  # Adjusted for visibility
    for i in range(6):
        angle = i * pi / 3  # 60 degrees in radians
        wall = create_hexagonal_wall(angle, wall_distance)
        hexagon_walls.append(wall)

    objects = [floor, middle, right, left] + hexagon_walls

    # Adjusted light source position
    light_source = Point(0, 10, 0).point_light(Color(1, 1, 1))  # Position the light above the scene

    world = World()
    world.objects = objects
    world.light_source = light_source

    # Adjusted camera settings
    camera = Camera(100, 100, pi / 4) 
    camera.transform = view_transform(Point(0, 10, -10), Point(0, 0, 0), Vector(0, 1, 0))  # Camera looking down

    canvas = camera.render(world)

    ppm_data = canvas.canvas_to_ppm()
    with open('output.ppm', 'w') as file:
        file.write(ppm_data)


if __name__ == "__main__":
    main()