__author__ = 'vaibhavt'

from PIL import Image

#convert to grayscale
pil_im = Image.open('lena.jpg').convert('L')
pil_im.show()

pil_im.save('lena_grayscale.png')
pil_im.save('lena_grayscale.pgm')
