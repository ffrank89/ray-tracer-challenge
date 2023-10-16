import math
from raytracer.tuples import Tuple
from raytracer.color import Color

class Canvas:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[Color(0,0,0) for _ in range(width)] for _ in range(height)]

    def display(self):
        for row in self.pixels:
            for pixel in row:
                if pixel == Color(0, 0, 0):
                    print(". ", end='')
                else:
                    print("* ", end='')
            print()  # New line at the end of each row

    def write_pixel(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y][x] = color
        else:
            raise ValueError(f"x({x}) and/or y({y}) are out of canvas range.")
        
            
    def pixel_at(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.pixels[y][x]
        else:
            raise ValueError(f"x({x}) and/or y({y}) are out of canvas range.")
        
    def clamp_color_value(self, value):
        return max(0, min(255, int(value * 256)))

    def canvas_to_ppm(self):
        lines = ['P3', f'{self.width} {self.height}', '255']
        
        for row in self.pixels:
            row_data = []
            for color in row:
                red = self.clamp_color_value(color.x)
                green = self.clamp_color_value(color.y)
                blue = self.clamp_color_value(color.z)
                row_data.extend([str(red), str(green), str(blue)])
            
            line = ' '.join(row_data)
            while line:
                # If appending the next value exceeds 70 characters, we need to split at the last space
                if len(line) > 70:
                    split_index = line.rfind(' ', 0, 70)
                    lines.append(line[:split_index])
                    line = line[split_index+1:]
                else:
                    lines.append(line)
                    line = ''

        return '\n'.join(lines) + '\n'
    
    
