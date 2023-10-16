from raytracer.tuples import Tuple

class Color(Tuple):
    def __init__(self,red,green,blue):
        super().__init__(red,green,blue,0)
    
    def red(self):
        return self.x
    def green(self):
        return self.y
    def blue(self):
        return self.z

    @staticmethod
    def hadamard_product(c1,c2):
        return Color(c1.red() * c2.red(), c1.green() * c2.green(), c1.blue() * c2.blue())

    
    def magnitude(self):
        raise ValueError("Magnitude is not defined for Color objects.")

    def normalize(self):
        raise ValueError("Normalize is not defined for Color objects.")

    @staticmethod
    def dot_product(c1,c2):
        raise ValueError("Dot product is not defined for Color objects.")
    
    @staticmethod
    def cross_product(v1, v2):
        raise ValueError("Dot product is not defined for Color objects.")
    


    
    def __repr__(self):
        return f"Color({self.x}, {self.y}, {self.z})"
    