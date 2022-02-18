from PIL import Image
import cv2
import numpy as np


def circle_detection(img_url):
    img = cv2.imread(img_url, cv2.IMREAD_GRAYSCALE)

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, dp=1.5, minDist=10,param1=45, param2=45, minRadius=20, maxRadius=50)

    color_img = cv2.imread(img_url)
    green = (0,255,0)
    if circles is not None:
        for circle in circles:
            for x, y, r in circle:
                cv2.circle(color_img, (int(x),int(y)), int(r), green, 2)
            

    cv2.imwrite('img/circle.png', color_img)
    return circles