import cv2
import numpy as np

def draw_result(connections, lines, img_url, directory):
    # read screenshot
    color_img = cv2.imread(img_url)
    for key in connections: 
        connection = connections[key]

        #draw circles
        d_1_circle = connection["d_1"]["circle"]
        d_2_circle = connection["d_2"]["circle"]

        cx1 = d_1_circle[0]
        cy1 = d_1_circle[1]
        cr1 = d_1_circle[2]

        cx2 = d_2_circle[0]
        cy2 = d_2_circle[1]
        cr2 = d_2_circle[2]

        cv2.circle(color_img, (int(cx1),int(cy1)), int(cr1), (0,0,0), 2)
        cv2.circle(color_img, (int(cx2),int(cy2)), int(cr2), (0,0,0), 2)

        #draw line
        line  = lines[key]
        lx1, ly1, lx2, ly2 = line[0]
        cv2.line(color_img, (lx1, ly1), (lx2, ly2), (0, 0, 0), 3)

    # write to image  
    dst_url = '{}/result.png'.format(directory) 
    cv2.imwrite(dst_url, color_img)


