import cv2
import numpy as np

def draw_result(connections, img_url, directory):
    # read screenshot
    color_img = cv2.imread(img_url)
    for connection in connections.connection_list:
        for node in connection.node_list:
            cv2.circle(color_img, (int(node.x),int(node.y)), int(node.radius), (0,0,0), 2)

        #draw line
        line  = connection.line
        cv2.line(color_img, (line.x1, line.y1), (line.x2, line.y2), (0, 0, 0), 3)

    # write to image  
    dst_url = '{}/result.png'.format(directory) 
    cv2.imwrite(dst_url, color_img)


