from src.test.generate_img import generate_img, create_background_img
from src.test.check_results import check_results
from main import main

import sys
import os

amount_of_test_imgs = int(sys.argv[1])

print("Starting to generate {} images...".format(amount_of_test_imgs))
generated_circles = []
for i in range(amount_of_test_imgs):
    print("Image {} is being created...".format(i))
    directory_name = 'img_{}'.format(i)
    
    sub_directory = 'test_img/{}/'.format(directory_name)
    os.makedirs(sub_directory, exist_ok=True)

    circle_directory = '{}/circles/'.format(sub_directory)
    os.makedirs(circle_directory, exist_ok=True)

    background_url = 'test_img/{}/background.png'.format(directory_name)

    create_background_img(background_url)

    circle_data = generate_img(background_url, directory_name)
    generated_circles.append(circle_data)
    print("Done with image {}".format(i))


print("Please have a look in the test_img/ directory to see created images.\n")

print("Preparing to start image detection...")
found_connections = []
for i in range(amount_of_test_imgs):
    directory_name = 'img_{}'.format(i)
    sub_directory = 'test_img/{}'.format(directory_name)

    filename = '{}/test.png'.format(sub_directory)

    print('Executing image detection for image {}'.format(i))
    result = main(filename, sub_directory)
    found_connections.append(result)
    print('Finished image detection for image {}'.format(i))
    print('You can find the results in {}'.format(sub_directory))

print("Finished detection for all created images.")


sys.exit()
print("Checking results...")

for i in range(amount_of_test_imgs):
    result = found_connections[i]
    generated_circle_for_this_img = generated_circles[i]["circles"]

    connections = result["connections"]
    circles = result["circles"]
    lines = result["lines"]

    
    #print(connections)

    #print(circles)

    #print(generated_circle_for_this_img)
    
    check_results(connections, generated_circle_for_this_img, lines)


