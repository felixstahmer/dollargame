import cv2
import pytesseract as tes
import numpy as np

from src.vc.vc_controller import VisualComputingController

class Node():
    def __init__(self, x, y, radius, directory, index):
        self.x = x
        self.y = y
        self.radius = radius
        self.directory = directory
        self.index = index
        self.number = None
        self.constraint_list = []

    def add_constraint(self, node):
        self.constraint_list.append(node)

    def detect_number(self, img_url):
        vc_controller = VisualComputingController()
        
        threshold = 190
        tesseract_config_string = "--psm 10 --oem 1 -c tessedit_char_whitelist=-0123456789"
        tries = 0
        while(self.number == None and threshold < 210):
            vc_controller.do_binary(self.directory, self.directory, threshold)
            # im_bw = cv2.imread(self.directory)
            # edges = cv2.Canny(im_bw,100,200,apertureSize=7)
            # cv2.imwrite(self.directory, edges)
            # vc_controller.do_thin(self.directory, self.directory)
            # kernel = np.ones((3, 3), np.uint8)
            # img = cv2.dilate(im_bw, kernel, iterations=1)
            # cv2.imwrite(self.directory, img)
            result = tes.image_to_string(self.directory,  config=tesseract_config_string)  
            number = result.split(sep='\n')
            if number[0] is not '\x0c':
                print("Number detected: {}".format(number[0]))
                number_to_check = str(number[0])
                isNegative = number_to_check[0] == "-"
                if isNegative == True:
                    if len(number_to_check[1:]) < 2: 
                        self.number = number[0]
                    else: 
                        self.number = None
                else: 
                    if len(number_to_check) < 2:
                        self.number = number[0]
                    else: 
                        self.number = None
                    if number_to_check == "41":
                        self.number = "1"
                # if number_to_check == "4" and tries == 0: 
                    # tesseract_config_string = "--psm 10 --oem 1 -c tessedit_char_whitelist=-0123456789"
                    # tries = tries + 1
                    # self.save_img(img_url, )
                    # self.number = None
                    # if threshold == 230:
                    #     self.number = 4
                
                if number_to_check == "-" or self.number == "-":
                    self.number = None
                    # threshold = 170
            else: 
                self.number = None
            threshold += 5
        print("Final Number: {}".format(self.number))

    def save_img(self, img_url, offset):
        vc_controller = VisualComputingController()

        r = self.radius - offset
        # r = self.radius - 8
        
        start_x = int(self.x - r)
        start_y = int(self.y - r)

        w = int(r * 2)
        h = int(r * 2)

        vc_controller.crop_image(img_url, self.directory, start_x, start_y, w, h)

    # whites out the circle on a specific image
    def white_out(self, img):
        rgbImage = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)

        offset = 2 # to white out the whole circle on specific image
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