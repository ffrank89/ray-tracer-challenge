from raytracer.tuples import Vector, Point
from raytracer.canvas import Canvas
from raytracer.color import Color
from exercises.projectiles import Projectile, Environment


    
def main():


    #Canvas
    canvas = Canvas(1500, 600)

    # projectile starts one unit above the origin (0,0)
    # velocity is normalized to one unit/tick
    starting_position = Point(0,1,0)
    starting_velocity = Vector(1,1,0).normalize().scale(11.25)
    p = Projectile(starting_position, starting_velocity)

    # gravity -0.1 unit/tick and wind is -0.01 unit/tick
    gravity = Vector(0,-0.1,0)
    wind = Vector(-0.01,0,0)
    e = Environment(gravity, wind)

    tick_count = 0
    while p.position.y > 0:
        
        print(f"Tick #{tick_count}: {p}")
        print(p)

        canvas.write_pixel(int(p.position.x), canvas.height - int(p.position.y), Color(1,0,0))
        p.tick(e)

        tick_count+=1

    ppm_data = canvas.canvas_to_ppm()
    with open('output.ppm', 'w') as file:
        file.write(ppm_data)


if __name__ == "__main__":
    main()