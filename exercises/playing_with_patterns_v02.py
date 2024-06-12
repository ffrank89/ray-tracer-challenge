from raytracer.canvas import *
from raytracer.camera import *
from raytracer.light import *
from raytracer.material import *
from raytracer.matrix import *
from raytracer.ray import *
from raytracer.shape import *
from raytracer.tuples import *
from raytracer.world import *
from raytracer.pattern import *
from raytracer.plane import *
from raytracer.transformations import *

import math

def main():
    world = World()

    # Light Source
    light_position = Point(-5, 10, -5)
    light_color = Color(1, 1, 1)
    world.light_source = light_position.point_light(light_color)

    # Floor
    floor = Plane()
    floor.material.pattern = Checker3DPattern(Color(0.5, 0.5, 0.5), Color(0.75, 0.75, 0.75))
    floor.material.pattern.set_pattern_transform(Scaling(0.5, 0.5, 0.5))
    world.objects.append(floor)

    # Sphere 1
    sphere1 = Sphere()
    sphere1.set_transform(Translation(-0.5, 1, 0.5))
    sphere1.material.pattern = StripePattern(Color(1, 0, 0), Color(0, 1, 0))
    sphere1.material.pattern.set_pattern_transform(Scaling(0.1, 0.1, 0.1).matrix_multiply(Rotation_Y(math.pi / 4)))
    world.objects.append(sphere1)

    # Sphere 2
    sphere2 = Sphere()
    sphere2.set_transform(Translation(2.5, 1.0, -0.5).matrix_multiply(Scaling(0.5, 0.5, 0.5)))
    sphere2.material.pattern = GradientPattern(Color(0, 0, 1), Color(1, 1, 0))
    #sphere2.material.pattern.set_pattern_transform(Translation(0, 0, 1))
    world.objects.append(sphere2)

    # Sphere 3
    sphere3 = Sphere()
    sphere3.set_transform(Translation(1, 1, -1.8).matrix_multiply(Scaling(.9, 0.9, 0.9)))
    sphere3.material.pattern = RingPattern(Color(0, .5, 1), Color(0, .1, 0))
    #sphere2.material.pattern.set_pattern_transform(Translation(0, 0, 1))
    world.objects.append(sphere3)

    # Configure Camera
    camera = Camera(100, 100, math.pi / 3)
    camera.transform = view_transform(Point(0, 1.5, -5), Point(0, 1, 0), Vector(0, 1, 0))

    # Render the Scene
    canvas = camera.render(world)

    # Save the image
    ppm_data = canvas.canvas_to_ppm()
    with open('output.ppm', 'w') as file:
        file.write(ppm_data)

if __name__ == "__main__":
    main()