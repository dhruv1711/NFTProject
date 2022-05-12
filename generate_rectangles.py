import random
from PIL import Image, ImageDraw
import colorsys
from python_utils import to_int


class ImageGenerator:
    def __init__(self, width, height, color = None):
        self.width = width
        self.height = height
        if color is None:
            color = self.random_color()
        self.image = Image.new('RGB', (self.width, self.height), color)

    def random_color(self, is_bright = False):
        if is_bright:
            float_color = colorsys.hsv_to_rgb(random.random(), 1, 1)
            color = tuple([int(i*255) for i in float_color])
            return color
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return color

    def gradient(self, start_color, end_color):
        base =  Image.new('RGB', (self.width, self.height), start_color)
        top = Image.new('RGB', (self.width, self.height), end_color)
        mask = Image.new('L', (self.width, self.height))
        mask_data = []
        for y in range(self.height):
            mask_data.extend([to_int(255 * (y / self.height))] * self.width)
        mask.putdata(mask_data)
        base.paste(top, (0, 0), mask)
        self.image = base
        
    def generate_rect(self, fill_color=None, outline_color=None):
        if fill_color is None:
            fill_color = self.random_color()
        if outline_color is None:
            outline_color = self.random_color()
        image = self.image
        draw = ImageDraw.Draw(image)
        for _ in range(20):
            x1= random.randint(0, to_int(self.width))
            y1= random.randint(0, to_int(self.height))
            x2= random.randint(0, to_int(self.width))
            y2= random.randint(0, to_int(self.height))
            draw.rectangle([(x1, y1), (x2, y2)], fill=self.random_color(is_bright=True), width = random.randint(1,5), outline=self.random_color())
        self.image = image

    def save_image(self, filename):
        self.image.save(filename)

if __name__ == "__main__":
    image1 = ImageGenerator(128, 128)
    image1.generate_rect()
    image1.save_image("test_image3.png")
    image2 = ImageGenerator(324, 324)
    image2.gradient(image2.random_color(), image2.random_color())
    image2.generate_rect()
    image2.save_image("gradient_image.png")