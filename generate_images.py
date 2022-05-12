from PIL import Image, ImageDraw
import random
random.seed(42)

def generate(px=128, color=(255,255,255)):
    image = Image.new("RGB", size=(px,px), color=(255,255,255))
    
    
    draw = ImageDraw.Draw(image)
    for i in range(20):
        x1= random.randint(0, px)
        y1= random.randint(0, px)
        x2= random.randint(0, px)
        y2= random.randint(0, px)
        draw.rectangle([(x1, y1), (x2, y2)], fill=(x1,y1*2-1,y2))

    image.save("test_image.png")

if __name__ == "__main__":
    generate(128, (255,255,255))