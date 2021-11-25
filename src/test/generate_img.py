import cv2
import numpy as np
from random import randint, seed
import time
import math

def get_coordinates(x_boundary_low, x_boundary_high, y_boundary_low, y_boundary_high):
    cx = randint(x_boundary_low, x_boundary_high)
    cy = randint(y_boundary_low, y_boundary_high)

    return cx, cy

def check_distance(circle, circles):
    too_close = False

    for c_circle in circles: 
        compare_x = c_circle["x"]
        compare_y = c_circle["y"]

        d = math.sqrt(math.pow(compare_x - circle["x"],2) + math.pow(compare_y - circle["y"], 2))

        if d <= (2 * 32 + 35):
            too_close = True
            return too_close
        else: 
            continue
    return too_close

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

def get_distances(x, y, circles):
    distances = []
    for index, circles in enumerate(circles): 
        c_x = circles["x"]
        c_y = circles["y"]

        if c_x == x and c_y == y: 
            continue

        d = math.sqrt(math.pow(x - c_x,2) + math.pow(y - c_y, 2))

        distance = {
            "distance": int(d),
            "index": index
        }
        if len(distances) > 0:
            distances.append(distance)
        else: 
            distances = [distance]

    return distances

def find_closest(distances, circles): 
    min1, min2 = distances[0]["distance"], distances[1]["distance"]
    i1, i2 = distances[0]["index"], distances[1]["index"]
    for index, distance in enumerate(distances):
        d = distance["distance"]
        i = distance["index"]
        if d < min1 or d < min2:
            min2 = min1
            min1 = d
            if i != i1: 
                i2 = i1
                i1 = i
            else: 
                if d < min2:
                    i2 = i
    #print(i1, i2)
    return [circles[i1], circles[i2]]

def draw_lines(circles, img, i):
    for circle in circles: 
        lines = circle["lines"]
        for line in lines: 
            #print(line)
            x1 = line["x1"]
            y1 = line["y1"]
            x2 = line["x2"]
            y2 = line["y2"]
            cv2.line(img, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 255), 2)

    dst_url = 'test_img/{}/test.png'.format(i)
    cv2.imwrite(dst_url, img)

def generate_lines(circles, img, i):
    for circle in circles: 
        x = circle["x"]
        y = circle["y"]

        distances = get_distances(x, y, circles)
        closest_circles = find_closest(distances, circles)
        # print(circle, closest_circles[0]["number"], closest_circles[2])
        # print(circle, closest_circles[1]["number"], closest_circles[3])
        # print(distances)
        lines = []
        for closest_circle in closest_circles: 
            cx = closest_circle["x"]
            cy = closest_circle["y"]

            # delta_x = x - cx
            # delta_y = y - cy

            # theta_radians = math.atan2(delta_y, delta_x)
            # theta_degrees = math.degrees(theta_radians)
            # print(theta_degrees)

            # start_x = x+(32 * math.cos(theta_degrees))
            # start_y = y+(32 * math.sin(theta_degrees))

            # end_x = cx+(32 * math.cos(theta_degrees))
            # end_y = cy+(32 * math.sin(theta_degrees))

            line = {
                "x1": x,
                "y1": y,
                "x2": cx,
                "y2": cy
            }

            lines.append(line)
        circle["lines"] = lines
    draw_lines(circles, img, i)


def generate_img(background_url, i): 
    seed(time.clock())
    img = cv2.imread(background_url)
    height, width, channels = img.shape

    x_boundary_low = int(width/3)
    x_boundary_high = x_boundary_low*2

    y_boundary_low = int(height/3)
    y_boundary_high = y_boundary_low*2

    circles = []
    c_amount = randint(3, 5)
    for x in range(c_amount):
        cx, cy = get_coordinates(x_boundary_low, x_boundary_high, y_boundary_low, y_boundary_high)
        c_number = randint(-5,5)

        circle = {
            "x": cx,
            "y": cy,
            "number": c_number
        }

        if len(circles) > 0:
            too_close = check_distance(circle, circles)

            while(too_close):
                cx, cy = get_coordinates(x_boundary_low, x_boundary_high, y_boundary_low, y_boundary_high)    
                circle["x"] = cx
                circle["y"] = cy

                too_close = check_distance(circle, circles)
            circles.append(circle)
        else: 
            circles = [circle]

    generate_lines(circles, img, i)
    draw_circles(circles, img, i)


def create_background_img(background_url): 
    width = 1440
    height = 789

    color = [184,194,66]

    """Create new image(numpy array) filled with certain color in RGB"""
    image = np.zeros((height, width, 3), np.uint8)

    image[:] = color

    cv2.imwrite(background_url, image)
