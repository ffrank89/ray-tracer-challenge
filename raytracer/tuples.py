import math

class Tuple:

    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    
    def isPoint(self):
        return self.w == 1.0

    def isVector(self):
        return self.w == 0.0
    
    def __eq__(self, other: object) -> bool:
        return (self.x == other.x and 
                self.y == other.y and 
                self.z == other.z and 
                self.w == other.w)
    
    def __add__(self, other):
        new_w = self.w + other.w
        if new_w > 1:
            raise ValueError("Operation not allowed: Adding two points is against da law.")
        return Tuple(self.x + other.x, self.y + other.y, self.z + other.z, new_w)

    def __sub__(self, other):
        new_w = self.w - other.w
        if new_w < 0:
            raise ValueError("Operation not allowed: Subtracting a point from a vector is not meaningful.")
        
        return Tuple(self.x - other.x, self.y - other.y, self.z - other.z, new_w)
    
    def __repr__(self):
        return f"Tuple({self.x}, {self.y}, {self.z}, {self.w})"

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z}, {self.w})"
    
    def scale(self, scalar):
        return Tuple(self.x * scalar, self.y * scalar, self.z * scalar, self.w * scalar)
    
    def negate(self):
        other = Tuple(0,0,0,0)
        return Tuple(other.x - self.x, other.y - self.y, other.z - self.z, other.w - self.w)
    
    def magnitude(self):
        #magnitude is the distance represented by a vector
        if self.w != 0:
            raise ValueError("Magnitude is only defined for vectors, not points.")
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normalize(self):
        # Normalization is the process of taking an arbitrary vector and converting it into a unit vector.
        # It will keep calculations anchored to a common scale (the unit vector).
        if self.w != 0:
            raise ValueError("Normalize is only defined for vectors, not points.")
        
        mag = self.magnitude()
        
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        
        return Vector(self.x / mag, self.y / mag, self.z / mag)
    
    @staticmethod
    def dot_product(v1, v2):
        if v1.w != 0 or v2.w != 0:
            raise ValueError("Dot Product is only defined for vectors, not points.")
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z
    
    @staticmethod
    def cross_prodct(v1, v2):
        if v1.w != 0 or v2.w != 0:
            raise ValueError("Dot Product is only defined for vectors, not points.")
        return Vector(
            v1.y * v2.z - v1.z * v2.y,
            v1.z * v2.x - v1.x * v2.z,
            v1.x * v2.y - v1.y * v2.x
        )



def Point(x, y, z):
    return Tuple(x, y, z, 1.0)

def Vector(x, y, z):
    return Tuple(x, y, z, 0.0)
    