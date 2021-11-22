from PIL import Image
import numpy as np

def do_grey(): 
    
    im = Image.open('img/screenshot.png')

    pixels = list(im.getdata())
    width, height = im.size

    final_pixels = np.empty(width*height, dtype=object)

    for y in range(height):
        for x in range(width):

            pos = y * width + x
            c = pixels[pos] 
            r = c[0]
            g = c[1]
            b = c[2]

            final_color = int((r + g + b) / 3)

            final_pixels[pos] = (final_color , final_color, final_color)

    new_image = Image.new('RGB', (width, height))
    new_image.putdata(final_pixels)
    new_image.save('img/grey.png')

