import cv2
import numpy as np
from PIL import Image

class VisualComputingController(): 

    def do_binary(self, img_url, dst_url, threshold): 
        image = cv2.imread(img_url)
        gray_image = self.do_gray(image)
        ret, thresh1 = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY_INV)

        cv2.imwrite(dst_url, thresh1)

    def do_thin(self, img_url, dst_url):
        image = cv2.imread(img_url)
        thinned = cv2.ximgproc.thinning(cv2.cvtColor(image, cv2.COLOR_RGB2GRAY))
        cv2.imwrite(dst_url, thinned)

    def do_gray(self, image):
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return img_gray

    def crop_image(self, img_url, dst_url, x, y, width, height):
        image = cv2.imread(img_url)
        crop = image[y:y+height, x:x+width]
        im = Image.fromarray(crop)
        im.save(dst_url)

    def improve_node_img(self, node):
        img_url = node.directory
        im = cv2.imread(img_url, cv2.IMREAD_GRAYSCALE)
        rgbImage = cv2.cvtColor(im, cv2.COLOR_RGBA2RGB)
        height, width, channels = rgbImage.shape

        x_edge = int(width/4)
        y_edge = int(height/4)

        # white out the top of the screen
        for y in range(y_edge):
            for x in range(x_edge):
                #set to background color
                rgbImage[y, x] = [0,0,0]
                rgbImage[x, y] = [0,0,0]

        y_value = height - y_edge
        x_value = width - x_edge

        for y in range(y_value, height):
            for x in range(x_value, width):
                rgbImage[y, x] = [0,0,0]
                rgbImage[x, y] = [0,0,0]
        
        cv2.imwrite(img_url, rgbImage)

    def white_out_top_of_screen(self, img):
        height, width, channels = img.shape
        #get a quarter of the height to white that part out 
        white_out_edge = int(height/4)

        # white out the top of the screen
        for y in range(white_out_edge):
            for x in range(width):
                #set to background color
                img[y, x] = [184,194,66]

        return img