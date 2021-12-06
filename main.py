from src.selenium.screenshot import take_screenshot
from src.vc.binary import do_binary
from src.vc.crop import crop_image
from src.detection.detect_circles import circle_detection 
from src.detection.detect_lines import line_detection
from src.detection.detect_connections import connection_detection
from src.draw.draw_result import draw_result

import pytesseract as tes
from pytesseract import Output
import cv2

def main(orig_url, directory):

    # find circles and lines between the circles
    circles = circle_detection(orig_url, directory)
    lines = line_detection(orig_url, circles, directory)


    # Create Image for each circle 

    results = []

    for circle_list in circles:
        for index, circle in enumerate(circle_list):
            x = circle[0]
            y = circle[1]
            r = circle[2] 
            offset = 10 # offset to cut close to the actual number

            r = r - offset

            start_x = int(x - r)
            start_y = int(y - r)

            w = int(r * 2)
            h = int(r * 2)

            dst_url = "{}/circles/{}.png".format(directory, index)

            # cut every the original image to the circles and save them in img/circles
            circle_img_url = crop_image(orig_url, dst_url, start_x, start_y, w, h)

            # convert every circle image to a binary image 
            do_binary(circle_img_url, circle_img_url, 150)

            # do number detection on every circle image
            number = tes.image_to_string(circle_img_url,  config='--psm 10 --oem 1 -c tessedit_char_whitelist=-0123456789')
            
            # save number alongside circle coordinates and radius
            result = number.split(sep='\n')

            #print(number)
            
            if result[0] is not '\x0c':
                results.append({"number": result[0], "circle": circle})
            else:
                continue

    connections = connection_detection(results, lines)

    draw_result(connections, lines, orig_url, directory)

    data = {
        "connections": connections,
        "circles": circles,
        "lines": lines
    }

    return data



if __name__ == '__main__':
    url = "https://thedollargame.io/game/level/100/100/2"
    orig_url = take_screenshot(url) # take screenshot of game and return screenshot URL
    #orig_url = "img/screenshot.png"
    #orig_url = "test_img/test.png"

    directory = 'img'
    
    main(orig_url, directory)