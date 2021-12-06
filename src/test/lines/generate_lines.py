from .distances import get_distances, find_closest, does_connection_exist

import cv2
import numpy as np 
import math

def draw_lines(lines, index_list, img, i):
    
    for index in index_list: 
        line = lines[index['line']]
        x1 = line["x1"]
        y1 = line["y1"]
        x2 = line["x2"]
        y2 = line["y2"]
        cv2.line(img, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 255), 2)

    dst_url = 'test_img/{}/test.png'.format(i)
    cv2.imwrite(dst_url, img)

def make_unique(index_list):
    unique_list = []
    #remove all the unneccessary connections between two circles
    for index in index_list: 
        circle1_i = index["circle1"]
        circle2_i = index["circle2"]

        if len(unique_list) > 1: 
            found = False
            for index_i in unique_list:
                c_circle1_i = index_i["circle1"]
                c_circle2_i = index_i["circle2"]

                if (circle1_i == c_circle2_i and circle2_i == c_circle1_i):
                    found = True
                else: 
                    continue
            if found: 
                continue
            else: 
                unique_list.append(index)
        else:
            unique_list.append(index)
    return unique_list

def cut_index_list(index_list, circles, lines):
    cleaned_up_list = []
    index_list = make_unique(index_list)
    for item in index_list: 
        circle1_i = item["circle1"]
        circle2_i = item["circle2"]

        circle1 = circles[circle1_i]
        circle2 = circles[circle2_i]
        
        found = False
        for circle in circles: 
            c_x = circle["x"]
            c_y = circle["y"]
            c_r = 45
            c_i = circle["index"]

            if c_i == circle1_i or c_i == circle2_i:
                continue

            p1=np.array([circle1["x"],circle1["y"]])
            p2=np.array([circle2["x"],circle2["y"]])
            p3=np.array([c_x,c_y])

            d=abs(np.cross(p2-p1,p3-p1)/np.linalg.norm(p2-p1))

            d_1 = math.sqrt(math.pow(circle1["x"] - circle2["x"],2) + math.pow(circle1["y"] - circle2["y"], 2))
            d_2 = math.sqrt(math.pow(c_x - circle1["x"],2) + math.pow(c_y - circle1["y"], 2))
            d_3 = math.sqrt(math.pow(c_x - circle2["x"],2) + math.pow(c_y - circle2["y"], 2))

            if (d < c_r) and (d_1 > d_2 and d_1 > d_3): 
                found = True
            else: 
                continue

        if found:
            continue
        else: 
            cleaned_up_list.append(item)
    print(len(cleaned_up_list))
    return cleaned_up_list

def generate_lines(circles, img, i):
    amount_of_lines = int(len(circles) * 1.5)
    lines = []
    index_list = []
    line_index = 0
    
    for circle in circles: 
        x = circle["x"]
        y = circle["y"]
        
        distances = get_distances(x, y, circles)

        sorted_distances = sorted(distances, key= lambda d: d['distance'])
        
        circle1_index = sorted_distances[0]["index"]
        circle1 = circles[circle1_index]
        
        circle2_index = sorted_distances[1]["index"]
        circle2 = circles[circle2_index]
        
        lineItem1 = {
            "x1": x,
            "y1": y,
            "x2": circle1["x"],
            "y2": circle1["y"]
        }


        lineItem2 = {
            "x1": x,
            "y1": y,
            "x2": circle2["x"],
            "y2": circle2["y"]
        }

        lines.append(lineItem1)
        lines.append(lineItem2)

        line_index_item = {
            "line": line_index,
            "circle1": circle["index"],
            "circle2": circle1["index"]
        }

        index_list.append(line_index_item)

        line_index_item2 = {
            "line": line_index + 1,
            "circle1": circle["index"],
            "circle2": circle2["index"]
        }

        index_list.append(line_index_item2)

        line_index = line_index + 2
            
    unique_index_list = cut_index_list(index_list, circles, lines)
    
    draw_lines(lines, unique_index_list, img, i)



# def generate_lines(circles, img, i):
#     amount_of_lines = int(len(circles) * 1.5)
#     lines = []
#     for iterator in range(amount_of_lines):
#         for circle in circles: 
#             x = circle["x"]
#             y = circle["y"]

#             distances = get_distances(x, y, circles)
            
#             closest_circles = find_closest(distances, circles)

#             cx = closest_circles[0]["x"]
#             cy = closest_circles[0]["y"]

#             cx2 = closest_circles[1]["x"]
#             cy2 = closest_circles[1]["y"]
            

#             line1 = {
#                 "x1": x,
#                 "y1": y,
#                 "x2": cx,
#                 "y2": cy,
#                 "index": iterator
#             }

#             finalItem = {
#                 "line": iterator,
#                 "d_1": closest_circles[0]["index"],
#                 "d_2": closest_circles[1]["index"],
#             }
            
#             lines.append(finalItem)
#             # already_exists = does_connection_exist(circles, line)
            
#             # if already_exists: 
#             #     print("in here")
#             #     continue
#             # else:
#             #     lines.append(line)

#             #circle["lines"] = lines
        

#         draw_lines(circles, lines,img, i)

#     return circles
