import cv2
import numpy as np

def draw_result(connections, img_url, directory):
    # read screenshot
    color_img = cv2.imread(img_url)
    solution_img = cv2.imread(img_url)
    for connection in connections.connection_list:
        for node in connection.node_list:
            cv2.circle(color_img, (int(node.x),int(node.y)), int(node.radius), (0,0,0), 2)

            writing_offset = 30
            start_x = int(node.x - writing_offset)
            start_y = int(node.y - writing_offset)
            color = (0, 0, 0)
            amount_of_clicks = str(node.amount_of_clicks)
            font = cv2.FONT_HERSHEY_SIMPLEX 
            cv2.putText(solution_img, amount_of_clicks,(start_x, start_y), font, 2, color, 3, 2)
        #draw line
        line  = connection.line
        cv2.line(color_img, (line.x1, line.y1), (line.x2, line.y2), (0, 0, 0), 3)

    # write to image  
    dst_url = '{}/result.png'.format(directory) 
    solution_url = '{}/solution.png'.format(directory)
    cv2.imwrite(solution_url, solution_img)
    cv2.imwrite(dst_url, color_img)


