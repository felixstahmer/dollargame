import cv2
import numpy as np
import math

from src.vc.vc_controller import VisualComputingController
from src.game_elements.line.line import Line
from src.game_elements.line.line_list import LineList
from src.game_elements.node.node import Node
from src.game_elements.node.node_list import NodeList
from src.game_elements.connection.connection import Connection
from src.game_elements.connection.connection_list import ConnectionList




class DetectionController(): 
    def detect_connections(self, dst_directory, node_list, line_list):
        connection_list = ConnectionList()
        for line in line_list.line_list:
            connection = Connection(line)
            for node in node_list.node_list:
                offset = 25
                r = int(node.radius + offset)

                distance_1 = int(math.sqrt(math.pow(node.x - line.x1,2) + math.pow(node.y - line.y1, 2)))
                distance_2 = int(math.sqrt(math.pow(node.x - line.x2,2) + math.pow(node.y - line.y2, 2)))

                if (distance_1 < r or distance_2 < r):
                    connection.add_node(node)

            if len(connection.node_list) == 2:
                # print(connection.node_list[0].number, connection.node_list[1].number)
                # print(connection.node_list[0].index, connection.node_list[1].index)
                connection_list.add_connection(connection)
        return connection_list


    def detect_lines(self, img_url, dst_directory, node_list):
        vc_controller = VisualComputingController()
        img = cv2.imread(img_url)

        white_out_top_of_img = vc_controller.white_out_top_of_screen(img)
        whited_out_img = node_list.white_out_all_circles(white_out_top_of_img)

        whited_out_url = "{}/whited_out.png".format(dst_directory)
        cv2.imwrite(whited_out_url, whited_out_img)
        
        binary_url = "{}/binary_for_line_detection.png".format(dst_directory)
        vc_controller.do_binary(whited_out_url, binary_url, 180)

        im_bw = cv2.imread(binary_url)
        edges = cv2.Canny(im_bw,50,150,apertureSize=3)
        lines = cv2.HoughLinesP(edges, 1, np.pi/180,threshold=12, minLineLength=10, maxLineGap=20)

        line_list = LineList()
        if lines is not None:
            #thin out line array since it found too many lines
            #lines = cut_lines(lines)
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(im_bw, (x1, y1), (x2, y2), (255, 0, 0), 3)

                line_obj = Line(x1, y1, x2, y2)
                line_list.add_line(line_obj)
        
        dst_url = '{}/lines.png'.format(dst_directory)
        cv2.imwrite(dst_url, im_bw)
        
        return line_list
        

    def detect_nodes(self, img_url, dst_directory): 
        vc_controller = VisualComputingController()

        im = cv2.imread(img_url, cv2.IMREAD_GRAYSCALE)
        rgbImage = cv2.cvtColor(im, cv2.COLOR_RGBA2RGB)

        img = vc_controller.white_out_top_of_screen(rgbImage)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        nodes = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, dp=1.5, minDist=10,param1=45, param2=45, minRadius=20, maxRadius=50)

        color_img = cv2.imread(img_url)
        green = (0,255,0)

        node_list = NodeList()
        if nodes is not None:
            for nodelist in nodes:
                for index, node in enumerate(nodelist):
                    x = node[0]
                    y = node[1]
                    r = node[2]
                    
                    if r < 25 or r > 40: 
                        continue

                    node_directory = "{}/nodes/{}.png".format(dst_directory, index)
                    node_obj = Node(x, y, r, node_directory, index)
                    node_obj.save_img(img_url, 8)
                    vc_controller.improve_node_img(node_obj)
                    node_obj.detect_number(img_url)
                    

                    if node_obj.number != None:
                        node_list.add_node(node_obj)

                    #remove circles from the list that have radius that is too small or too big 
                    # if r < 20 or r > 40: 
                    #     continue
                    
                    cv2.circle(color_img, (int(x),int(y)), int(r), green, 2)

        dst_url = '{}/nodes.png'.format(dst_directory)
        cv2.imwrite(dst_url, color_img)

        return node_list
                    