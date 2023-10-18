from raytracer.tuples import Vector, Point
from raytracer.canvas import Canvas
from raytracer.color import Color
from raytracer.matrix import *
from raytracer.transformations import *
from math import pi

from exercises.projectiles import Projectile, Environment


    
def main():

    width = 250
    height = 250

    canvas = Canvas(width, height)

    center = Point(width/2,height/2,0)
    clock_radius = 3 * width / 8
    twelve = Point(clock_radius, 0, 0)

    for i in range(12):
        r = Rotation_Y(i * (pi/6))
        hour = r.tuple_multiply(twelve)
        canvas.write_pixel(int(center.x + hour.x), int(center.y + hour.z), Color(1,0,0))

    ppm_data = canvas.canvas_to_ppm()
    with open('output.ppm', 'w') as file:
        file.write(ppm_data)


if __name__ == "__main__":
    main()