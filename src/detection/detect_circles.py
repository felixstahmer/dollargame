from src.detection.detect_lines import white_out_top_of_screen

from PIL import Image
import cv2
import numpy as np


def circle_detection(img_url):
    im = cv2.imread(img_url, cv2.IMREAD_GRAYSCALE)
    rgbImage = cv2.cvtColor(im, cv2.COLOR_RGBA2RGB)

    img = white_out_top_of_screen(rgbImage)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, dp=1.5, minDist=10,param1=45, param2=45, minRadius=20, maxRadius=50)

    color_img = cv2.imread(img_url)
    green = (0,255,0)
    if circles is not None:
        for circle in circles:
            for x, y, r in circle:
                cv2.circle(color_img, (int(x),int(y)), int(r), green, 2)
            

    cv2.imwrite('img/circle.png', color_img)
    return circles