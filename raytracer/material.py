from raytracer.color import Color
from raytracer.tuples import *
class Material:

    EPSILON = 1e-9
    BLACK = Color(0,0,0)
    def __init__(self, color=None, ambient=None, diffuse=None, specular=None, shininess=None):
        self.color = color if color else Color(1, 1, 1)
        self.ambient = ambient if ambient else 0.1
        self.diffuse = diffuse if diffuse else 0.9
        self.specular = specular if specular else 0.9
        #10 = large headlight 200 = small headlight
        self.shininess = shininess if shininess else 200.0

    def __eq__(self, other):
        if not isinstance(other, Material):
            return False
        return (self.color == other.color and 
                abs(self.ambient - other.ambient) < Material.EPSILON and
                abs(self.diffuse - other.diffuse) < Material.EPSILON and
                abs(self.specular - other.specular) < Material.EPSILON and
                abs(self.shininess - other.shininess) < Material.EPSILON)
    
    def lighting(self, light, point, eyev, normalv):
        #combine the surface color with the light's color / intensity
        effective_color = Color.hadamard_product(self.color, light.intensity)

        #find the direction to the light source
        lightv = (light.position - point).normalize()
        
        #compute the ambient contribution
        ambient = effective_color.scale(self.ambient)

        #light_dot_normal represents the cosine of the angle between the light vector and the normal vector
        #a negative number means the light is on the other side of the surface
        light_dot_normal = Tuple.dot_product(lightv, normalv)
        if light_dot_normal < 0:
            diffuse = Material.BLACK
            specular = Material.BLACK

        else:
            #compute the diffuse contribution
            diffuse = effective_color.scale(self.diffuse).scale(light_dot_normal)

            #reflect_dot_eye represents the cosine of the angle between the reflection vector and the eye vector
            #a negative number means the light reflects away from the eye
            reflectv = (lightv.scale(-1)).reflect(normalv)
            reflect_dot_eye = Tuple.dot_product(eyev, reflectv)
            if reflect_dot_eye <= 0:
                specular = Material.BLACK
            else:
                #compute the specular contribution
                factor = pow(reflect_dot_eye, self.shininess)
                specular = light.intensity.scale(self.specular).scale(factor)
        #add the three contributions together to get the final
        return ambient + diffuse + specular

    