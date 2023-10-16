from raytracer.tuples import Tuple, Point, Vector

class Projectile:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def __str__(self):
        return f"Position: {self.position}, Velocity: {self.velocity}"
    
    def tick(self, env):
        self.position = self.position + self.velocity
        self.velocity = self.velocity + env.gravity + env.wind
    
class Environment:
    def __init__(self, gravity, wind):
        self.gravity = gravity
        self.wind = wind
    
    
def main():
    # projectile starts one unit above the origin (0,0)
    # velocity is normalized to one unit/tick
    starting_position = Point(0,1,0)
    starting_velocity = Vector(1,1,0).normalize()
    p = Projectile(starting_position, starting_velocity)

    # gravity -0.1 unit/tick and wind is -0.01 unit/tick
    gravity = Vector(0,-0.1,0)
    wind = Vector(-0.01,0,0)
    e = Environment(gravity, wind)

    tick_count = 0
    while p.position.y > 0:
        print(f"Tick #{tick_count}: {p}")
        print(p)
        p.tick(e)
        tick_count+=1


if __name__ == "__main__":
    main()