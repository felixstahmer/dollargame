import cv2
import numpy as np
from random import randint, seed
import time
import math

from .circles.generate_circles import generate_circles
from .lines.generate_lines import generate_lines


def color_circle(x, y, r, img): 
    rgbImage = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
    for y_i in range(y-r, y+r):
        for x_i in range(x-r, x+r):
            rgbImage[int(y_i), int(x_i)] = [184,194,66]
    return rgbImage

def draw_circles(circles, img, i):
    for circle in circles: 
        x = circle["x"]
        y = circle["y"]
        r = 35
        number = circle["number"]

        font = cv2.FONT_HERSHEY_DUPLEX
        thickness = 2
        if number < 0: 
            color = (39, 49, 187)
            #color = (0, 0, 0)
            img = color_circle(int(x), int(y), int(r), img) 
            cv2.circle(img, (int(x),int(y)), int(r), color, thickness=2, lineType=8, shift=0)
            offset = 25
            cv2.putText(img, str(number), (x-offset,y+offset-15), font, 1, (255,255,255), thickness, cv2.LINE_AA)
        else:
            img = color_circle(int(x), int(y), int(r), img)  
            cv2.circle(img, (int(x),int(y)), int(r), (255,255,255), thickness=2, lineType=8, shift=0)
            offset = 20
            cv2.putText(img, str(number), (x-offset+10,y+offset-10), font, 1, (255,255,255), thickness, cv2.LINE_AA)      
    
    dst_url = 'test_img/{}/test.png'.format(i)
    cv2.imwrite(dst_url, img)


def generate_img(background_url, i): 
    seed(time.clock())
    img = cv2.imread(background_url)
    
    circles = generate_circles(img)
    
    circles_with_lines = generate_lines(circles, img, i)
    draw_circles(circles, img, i)

    data = {
        "circles": circles_with_lines
    }

    return data

def create_background_img(background_url): 
    width = 1440
    height = 789

    color = [184,194,66]

    """Create new image(numpy array) filled with certain color in RGB"""
    image = np.zeros((height, width, 3), np.uint8)

    image[:] = color

    cv2.imwrite(background_url, image)
