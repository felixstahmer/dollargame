import math
import numpy as np
import yaml

def find_unique_circles(connections):
    circles = []
    for key, value in connections.items(): 
        circle_1 = value["d_1"]
        circle_2 = value["d_2"]

        circles.append(circle_1)
        circles.append(circle_2)
    
    unique_circles = list({v['index']:v for v in circles}.values())
    
    return unique_circles

def get_unique_connections(connections):
    unique_connections = []
    for connection in connections: 
        if len(unique_connections) > 0:
            first_circle = connection["d_1"]["index"]
            second_circle = connection["d_2"]["index"]
            counter = 0
            if first_circle == second_circle: 
                continue

            for c_connection in unique_connections: 
                found = False
                c_first_circle = c_connection["d_1"]["index"]
                c_second_circle = c_connection["d_2"]["index"]

                if (c_first_circle == first_circle and c_second_circle == second_circle) or (c_first_circle == second_circle and c_second_circle == first_circle):
                    found = True
                else: 
                    continue
                    
            if found == True: 
                continue
            else:
                print(connection)
                print(first_circle, second_circle, c_first_circle, c_second_circle)
                unique_connections.append(connection)
        else: 
            #print(connection)
            unique_connections.append(connection)

    return unique_connections

def get_connection_list(circles):
    connection_list = []
    for index, circle in enumerate(circles): 
        circle["index"] = index

        lines = circle["lines"]
        for line in lines: 
            x = line["x2"]
            y = line["y2"]

            try: 
                other_circle = next(item for item in circles if item["x"] == x and item["y"] == y)
            
                item = {
                    "d_1": circle,
                    "d_2": other_circle
                }

                connection_list.append(item)
                #circles = [i for i in circles if not (i['x'] == x and i['y']==y)]
                
            
            except: 
                continue

    #print("Connections:")
    #print(len(connection_list))
    #print(connection_list)
    #unique_connections = get_unique_connections(connection_list)

    return connection_list

def check_results(connections, generated_circles, lines):
    found_circles = find_unique_circles(connections)

    correct_circles = []
    error_list = []
    for generated_circle in generated_circles: 
        x = generated_circle['x']
        y = generated_circle['y']
        number = generated_circle['number']

        for found_circle in found_circles: 

            c_x = found_circle["circle"][0]
            c_y = found_circle["circle"][1]
            r = found_circle["circle"][2]

            c_number = int(found_circle["number"])

            d = int(math.sqrt(math.pow(x - c_x,2) + math.pow(y - c_y, 2)))

            number_is_equal = number == c_number
            position_is_equal = d < 10

            if position_is_equal and number_is_equal:
                correct_circles.append(generated_circle)
            elif number_is_equal is not True and position_is_equal:
                error_item = generated_circle
                error_item["c_number"] = c_number
                error_list.append(generated_circle)

    if len(generated_circles) == len(correct_circles):
        print("The correct amount of circles was detected ({})".format(len(generated_circles)))
    else: 
        #difference = abs(len(generated_circles)-len(correct_circles))
        print("The algorithm detected {} circles with the right position and number instead of {} that were in the image.".format(len(correct_circles), len(generated_circles)))

    if len(error_list) > 0:
        for error in error_list: 
            x = error["x"]
            y = error["y"]
            number = error["number"]
            c_number = error["c_number"]
            message = "At the circle {}/{} the wrong number was detected {} instead of {}.".format(x,y,c_number,number)
            print(message)
    

    generated_connections = get_connection_list(generated_circles)
    
    found_connections = 0
    for key, value in connections.items(): 
        line_key = key
        
        first_circle = value["d_1"]
        second_circle = value["d_2"]
        x_1 = first_circle['circle'][0]
        y_1 = first_circle['circle'][1]

        x_2 = second_circle['circle'][0]
        y_2 = second_circle['circle'][1]
        
        for generated_connection in generated_connections:
            c_first_circle = generated_connection["d_1"]
            c_second_circle = generated_connection["d_2"]

            d_1 = int(math.sqrt(math.pow(x_1 - c_first_circle["x"],2) + math.pow(y_1 - c_first_circle["y"], 2)))
            d_2 = int(math.sqrt(math.pow(x_2 - c_second_circle["x"],2) + math.pow(y_2 - c_second_circle["y"], 2)))
            d_3 = int(math.sqrt(math.pow(x_1 - c_second_circle["x"],2) + math.pow(y_1 - c_second_circle["y"], 2)))
            d_4 = int(math.sqrt(math.pow(x_2 - c_first_circle["x"],2) + math.pow(y_2 - c_first_circle["y"], 2)))

            #print(d_1, d_2, d_3, d_4)
            
            if (d_1 < 10 and d_2 < 10) or (d_3 < 10 and d_4 < 10):
                found_connections = found_connections + 1
                
    print(found_connections)
    print(len(generated_connections))
    print(len(generated_connections) - found_connections)    

