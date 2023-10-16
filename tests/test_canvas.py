import unittest
import math
from raytracer.canvas import Canvas
from raytracer.color import Color


class CanvasTests(unittest.TestCase):

    def test_create_canvas(self):
        c = Canvas(10,20)
        self.assertTrue(c.width == 10)
        self.assertTrue(c.height == 20)

        for col in range(c.width):
            for row in range(c.height):
                self.assertTrue(c.pixels[row][col] == Color(0,0,0))

    def test_write_pixels_to_canvas(self):
        c = Canvas(10,20)
        red = Color(1,0,0)

        c.write_pixel(2,3,red)

        self.assertTrue(c.pixel_at(2,3) == red)

    def test_canvas_to_ppm_header(self):
        c = Canvas(5, 3)
        ppm = c.canvas_to_ppm().splitlines()  # Split the PPM string into lines

        self.assertEqual(ppm[0], "P3")
        self.assertEqual(ppm[1], "5 3")
        self.assertEqual(ppm[2], "255")

    def test_canvas_to_ppm_body(self):
        c = Canvas(5,3)
        c1 = Color(1.5,0,0)
        c2 = Color(0,0.5,0)
        c3 = Color(-0.5,0,1)
        c.write_pixel(0,0,c1)
        c.write_pixel(2,1,c2)
        c.write_pixel(4,2,c3)
        ppm = c.canvas_to_ppm().splitlines()
        self.assertEqual(ppm[3], "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0")
        self.assertEqual(ppm[4], "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0")
        self.assertEqual(ppm[5], "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255")

    def test_canvas_to_ppm_body_length_wrap(self):
        c = Canvas(10, 2)
        color = Color(1, .8, .6)
        
        for x in range(c.width):
            for y in range(c.height):
                c.write_pixel(x, y, color)
                
        ppm = c.canvas_to_ppm().splitlines()

        self.assertEqual(ppm[3], "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204")
        self.assertEqual(ppm[4], "153 255 204 153 255 204 153 255 204 153 255 204 153")
        self.assertEqual(ppm[5], "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204")
        self.assertEqual(ppm[6], "153 255 204 153 255 204 153 255 204 153 255 204 153")


    def test_ppm_newline_ending(self):
        canvas = Canvas(5, 3)
        ppm_output = canvas.canvas_to_ppm()
        self.assertTrue(ppm_output.endswith('\n'), "PPM output does not end with a newline character!")




    def test_canvas_to_ppm_line_length(self):
        c = Canvas(20, 10)
        color = Color(1, .8, .6)
        
        # Fill the canvas with the random color to maximize the chances of getting long lines
        for x in range(c.width):
            for y in range(c.height):
                c.write_pixel(x, y, color)
        
        ppm_output = c.canvas_to_ppm()
        lines = ppm_output.split("\n")

        # Check that no line (excluding the last) exceeds 70 characters
        for line in lines[:-1]:  # Excluding the last line, which is often an empty string
            self.assertTrue(len(line) <= 70, f"Line '{line}' exceeds 70 characters.")





if __name__ == '__main__':
    unittest.main()