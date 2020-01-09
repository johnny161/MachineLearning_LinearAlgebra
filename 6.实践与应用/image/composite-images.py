import os 
from PIL import Image

image_names = [name for name in os.listdir('.') if os.path.splitext(name)[1] == ".png"]
image_names.sort()

to_image = Image.new('RGB', (640, 560))

for y in range(1, 5):
    for x in range(1, 5):
        from_image = Image.open(image_names[4*(y-1)+x-1]).resize((160,140),Image.ANTIALIAS)
        to_image.paste(from_image, ((x-1)*160, (y-1)*140))
        to_image.save('res.jpg')
