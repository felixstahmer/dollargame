from src.vc.crop import crop_image
from src.vc.binary import do_binary

import cv2
import numpy as np

def white_out_top_of_screen(img):
    height, width, channels = img.shape
    #get a quarter of the height to white that part out 
    white_out_edge = int(height/4)

    # white out the top of the screen
    for y in range(white_out_edge):
        for x in range(width):
            #set to background color
            img[y, x] = [184,194,66]

    return img

def white_out_circles(img_url, circles):
    img = cv2.imread(img_url, cv2.IMREAD_COLOR)
    rgbImage = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)

    # loop over all circles to white them out
    for circle_list in circles:
        for circle in circle_list:
            x = circle[0]
            y = circle[1]
            r = circle[2] 
            offset = 3 # offset to white out the whole circle

            r = r + offset

            start_x = int(x - r)
            start_y = int(y - r)

            w = int(r * 2)
            h = int(r * 2)
            
            # white out all the circles with the numbers inside
            for y_i in range(start_y, start_y + h):
                for x_i in range(start_x, start_x + w):
                    #set to background color
                    rgbImage[int(y_i), int(x_i)] = [184,194,66]

    finalImage = white_out_top_of_screen(rgbImage)
    # finalImage = cv2.cvtColor(finalImage, cv2.COLOR_RGB2RGBA)

    whited_out_url = 'img/whited_out.png'
    cv2.imwrite(whited_out_url, finalImage)

    return whited_out_url


# def cut_lines(lines):
#     lines_copy = np.copy(lines)
#     for i, line in enumerate(lines):
#         x1, y1, x2, y2 = line[0]

#         # offset for x and y values to compare to 
#         x_offset, y_offset = 20, 20

#         x_lower_boundaries = x1 - x_offset
#         x_upper_boundaries = x1 + x_offset

#         y_lower_boundaries = y1 - y_offset
#         y_upper_boundaries = y1 + y_offset
        
#         # look in other line elements for similar values and remove them
#         for index, compare_line in enumerate(lines):
#             cx1, cy1, cx2, cy2 = compare_line[0]
            
            

#             if (cx1 > x_lower_boundaries and cx1 < x_upper_boundaries) and (cy1 > y_lower_boundaries and cy1 < y_upper_boundaries):
#                 lines_copy[index][0] = [x1, y1, x2, y2]


#             # for y_comparator in range(cy1 - y_offset, cy1+y_offset):
#             #     for x_comparator in range(cx1 - x_offset, cx1 + x_offset):
#             #         for y2_comparator in range(cy2 - y_offset, cy2 + y_offset):
#             #             for x2_comparator in range(cx2 - x_offset, cx2 + x_offset):
#             #                 if x_comparator == x1 and y_comparator == y1 and y2_comparator == y2 and x2_comparator == x2:
#             #                     lines_copy[index][0] = [x1, y1, x2, y2]
        
#             np.delete(lines, index, axis=0)

#     unique_array = np.unique(lines_copy, axis=0)
#     return unique_array

def line_detection(img_url, circles):
    whited_out_url = white_out_circles(img_url, circles)

    binary_url = "img/binary-for-linedetection.png"
    do_binary(whited_out_url, binary_url, 150)
    im_bw = cv2.imread(binary_url)

    edges = cv2.Canny(im_bw,50,150,apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180,threshold=12, minLineLength=25, maxLineGap=50)    
    print(lines)
    if lines is not None:
        #thin out line array since it found too many lines
        #lines = cut_lines(lines)
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(im_bw, (x1, y1), (x2, y2), (255, 0, 0), 3)

    cv2.imwrite('img/lines.png', im_bw)
    return lines
    