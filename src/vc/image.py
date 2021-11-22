from PIL import Image
import numpy as np

def detect_numbers(): 
    
    im = Image.open('img/screenshot.png')

    pixels = list(im.getdata())
    width, height = im.size

    start_index = -2
    end_index = 6
    for iterator in range(start_index, end_index):
        template_path = "img/numbers/{}.png".format(iterator)

        print("Get template data of {}".format(template_path))
        template_img = Image.open(template_path)
        template_pixels = list(template_img.getdata())
        template_width, template_height = template_img.size

        print("Finished getting template data")

        distance_map = np.zeros(((width-template_width), (height-template_height)))

        print("Calculating distance map for {}...".format(template_path))
        for y in range(height - template_height):
            for x in range(width - template_width):

                difference = 0.0

                for i in range(template_height):
                    for j in range(template_width):
                        pos = i * template_width + j
                        c = template_pixels[pos] 
                        r = c[0]
                        g = c[1]
                        b = c[2]

                        template_color = (r + g + b) / 3

                        newX = x + j
                        newY = y + i

                        imagePos = newX * template_width + newY
                        image_c = pixels[imagePos]
                        im_r = image_c[0]
                        im_g = image_c[1]
                        im_b = image_c[2]

                        image_color = (im_r + im_g + im_b) / 3

                        difference += abs(image_color - template_color)

                difference = difference / (template_width * template_height)
                if difference <= 70:
                    print(difference)
                distance_map[x][y] = difference
        print("Finished distance map for {}".format(template_path))
        print(distance_map)



                

