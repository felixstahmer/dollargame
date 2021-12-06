from random import randint, seed
import math

def check_distance(circle, circles, x_boundary_low, x_boundary_high, y_boundary_low, y_boundary_high):

    if (circle["x"] < x_boundary_low or circle["x"] > x_boundary_high) or (circle["y"] < y_boundary_low or circle["y"] > y_boundary_high):
        return True

    for c_circle in circles: 
        compare_x = c_circle["x"]
        compare_y = c_circle["y"]

        d = math.sqrt(math.pow(compare_x - circle["x"],2) + math.pow(compare_y - circle["y"], 2))
        if d <= 100:
            return True
        else: 
            continue
    return False

def get_coordinates(cx, cy):
    #angle_list = [0,785398, 1,5708, -0,785398, 3,14159, -3,14159, -1,5708]
    angle_list = [45, 90, -45, 180, -90, -180, 360, 135, -135]
    angle_index = randint(0, len(angle_list)-1)
    angle = angle_list[angle_index]
    #print(angle)
    distance = randint(50, 250)

    x = int(cx - (distance * math.cos(angle)))
    y = int(cy - (distance * math.sin(angle)))
    
    return x, y

def generate_circles(img):
    height, width, channels = img.shape

    x_boundary_low = int(width/5)
    x_boundary_high = x_boundary_low*4

    y_boundary_low = int(height/5)
    y_boundary_high = y_boundary_low*4
    
    # start_value_x = randint(int(width/3), int(width/3)*2)
    # start_value_y = randint(int(height/3), int(height/3)*2)

    circles = []
    c_amount = randint(3, 5)
    for x in range(c_amount):

        cx, cy = get_coordinates(int(width/2),int(height/2))
        c_number = randint(-5,5)

        circle = {
            "x": cx,
            "y": cy,
            "number": c_number,
            "index": x
        }

        if len(circles) > 0:
            too_close = check_distance(circle, circles, x_boundary_low, x_boundary_high, y_boundary_low, y_boundary_high)
            
            while(too_close):
                cx_new, cy_new = get_coordinates(cx, cy)    
                circle["x"] = cx_new
                circle["y"] = cy_new

                too_close = check_distance(circle, circles, x_boundary_low, x_boundary_high, y_boundary_low, y_boundary_high)
            circles.append(circle)
        else: 
            circles = [circle]
    #print(circles)
    return circles