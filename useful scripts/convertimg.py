#to convert image from png to jpeg

from PIL import Image

img = Image.open("x-res\\girlcomp.png")
rgb_im = img.convert('RGB')
rgb_im.save("output.jpg")
