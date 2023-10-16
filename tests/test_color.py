from raytracer.color import Color
import unittest 

class ColorTests(unittest.TestCase):

    def test_color(self):
        c = Color(-.5,.4,1.7)
        self.assertTrue(c.red() == -.5)
        self.assertTrue(c.green() == .4)
        self.assertTrue(c.blue() == 1.7)

    def test_add_colors(self):
        c1 = Color(.9,.6,.75)
        c2 = Color(.7,.1,.25)
        self.assertEquals(c1+c2, Color(1.6,.7,1.0))

    def test_subtract_colors(self):
        c1 = Color(.9,.6,.75)
        c2 = Color(.7,.1,.25)
        self.assertEquals(c1-c2, Color(.2,.5,.5))

    def test_multiply_color_by_scalar(self):
        c1 = Color(.9,.6,.75)
        self.assertEquals(c1.scale(2), Color(1.8,1.2,1.5))

    def test_multiply_colors(self):
        c1 = Color(.9,1,.1)
        c2 = Color(1,.2,.4)
        self.assertEquals(Color.hadamard_product(c1,c2), Color(.9,.2,.04))
    
if __name__ == '__main__':
    unittest.main()