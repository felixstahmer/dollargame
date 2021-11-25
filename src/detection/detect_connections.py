import cv2
import numpy as np
import math


def cleanup_connections(connections):
    cleanedup_connections = {}
    # loop over dict of connections to find duplicates
    for key in connections: 
        connection = connections[key]
        
        d_1_circle = connection["d_1"]
        d_2_circle = connection["d_2"]

        d_1_index = d_1_circle["index"]
        d_2_index = d_2_circle["index"]

        if len(cleanedup_connections) > 0:
            found = False
            for ckey in cleanedup_connections:
                c_connection = cleanedup_connections[ckey]

                c_d_1_circle = c_connection["d_1"]
                c_d_2_circle = c_connection["d_2"]

                c_d_1_index = c_d_1_circle["index"]
                c_d_2_index = c_d_2_circle["index"]

                # if a connection between two circles already exists mark found as true
                if (d_1_index == c_d_1_index and d_2_index == c_d_2_index) or (d_1_index == c_d_2_index and d_2_index == c_d_1_index):
                    found = True

                if d_1_index == d_2_index: 
                    found = True

            # if true ignore this connection, if not put it in the cleaned up dict
            if found == True: 
                continue
            else: 
                print(d_1_circle["number"],d_2_circle["number"])    
                cleanedup_connections[key] = connection        
        else: 
            print(d_1_circle["number"],d_2_circle["number"])
            cleanedup_connections[key] = connection
    return cleanedup_connections



def connection_detection(circles, lines):
    #print(circles)
    connections = {}
    for index, line in enumerate(lines):
        l_x1, l_y1, l_x2, l_y2 = line[0]
        for i, circle in enumerate(circles): 
            c_x = circle["circle"][0]
            c_y = circle["circle"][1]
            c_r = circle["circle"][2]
            circle["index"] = i
            #del circle["dtype"]

            offset = 30

            r = c_r + offset

            d_1 = math.sqrt(math.pow(c_x - l_x1,2) + math.pow(c_y - l_y1, 2))
            d_2 = math.sqrt(math.pow(c_x - l_x2,2) + math.pow(c_y - l_y2, 2))

            if d_1 < r:
                hit = {"d_1": circle}
                if index in connections:
                    connections[index].update(hit)
                else:
                    connections[index] = hit

            if d_2 < r:
                hit = {"d_2": circle}
                if index in connections:
                    connections[index].update(hit)
                else:
                    connections[index] = hit
        
        # if only one or no circles where found per line delete them from dict
        if index in connections:
            if len(connections[index]) <= 1:
                del connections[index] 
    
    clean_connections = cleanup_connections(connections)

    return clean_connections
        