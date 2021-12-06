import math


def find_closest(distances, circles): 
    pass    
    # min1, min2 = distances[0]["distance"], distances[1]["distance"]
    # i1, i2 = distances[0]["index"], distances[1]["index"]
    # for index, distance in enumerate(distances):
    #     d = distance["distance"]
    #     i = distance["index"]
    #     if d < min1 or d < min2:
    #         min2 = min1
    #         min1 = d
    #         if i != i1: 
    #             i2 = i1
    #             i1 = i
    #         else: 
    #             if d < min2:
    #                 i2 = i
    
    #print(i1, i2)
    # if randint(-10, 10) > 0: 
    #     return [circles[i1]]
    # else: 
    #     return [circles[i1], circles[i2]]
    
    #return [circles[i1], circles[i2]] 


def does_connection_exist(circles, line): 
    found = False
    for circle in circles: 
        if "lines" in circle:
            lines = circle["lines"]
            for c_line in lines: 
                # shared_items = {k: c_line[k] for k in c_line if k in line and c_line[k] == line[k]}
                # print(len(shared_items))
                # if len(shared_items) > 0:
                #     print(shared_items)
                #     print(line, c_line)
                if (c_line["x1"] == line["x1"] and c_line["x2"] == line["x2"] and c_line["y1"] == line["y1"] and c_line["y2"] == line["y2"]) or (c_line["x1"] == line["x2"] and c_line["x2"] == line["x1"] and c_line["y1"] == line["y1"]):
                    found = True
                else: 
                    continue
        else:
            continue
    return found 

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
