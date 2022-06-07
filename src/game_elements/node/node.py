import cv2
import pytesseract as tes
import numpy as np

from src.vc.vc_controller import VisualComputingController

class Node():
    def __init__(self, x, y, radius, directory):
        self.x = x
        self.y = y
        self.radius = radius
        self.directory = directory
        self.index = None
        self.number = None
        self.neighbors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def save_img(self, img_url, offset):
        vc_controller = VisualComputingController()

        r = self.radius - offset
        
        start_x = int(self.x - r)
        start_y = int(self.y - r)

        w = int(r * 2)
        h = int(r * 2)

        vc_controller.crop_image(img_url, self.directory, start_x, start_y, w, h)

    # whites out the circle on a specific image
    def white_out(self, img_url):
        rgbImage = cv2.cvtColor(img_url, cv2.COLOR_RGBA2RGB)

        offset = 1 # to white out the whole circle on specific image
        r = self.radius + offset

        start_x = int(self.x - r)
        start_y = int(self.y - r)

        w = int(r * 2)
        h = int(r * 2)
        
        # white out all the circles with the numbers inside
        for y_i in range(start_y, start_y + h):
            for x_i in range(start_x, start_x + w):
                #set to background color
                try:
                    rgbImage[int(y_i), int(x_i)] = [184,194,66]
                except IndexError:
                    break
                
        return rgbImage