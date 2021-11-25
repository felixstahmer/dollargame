from src.test.generate_img import generate_img, create_background_img
from main import main

import sys
import os

amount_of_test_imgs = int(sys.argv[1])

print("Starting to generate {} images...".format(amount_of_test_imgs))
for i in range(amount_of_test_imgs):
    print("Image {} is being created...".format(i))
    directory_name = 'img_{}'.format(i)
    
    sub_directory = 'test_img/{}/'.format(directory_name)
    os.makedirs(sub_directory, exist_ok=True)

    circle_directory = '{}/circles/'.format(sub_directory)
    os.makedirs(circle_directory, exist_ok=True)

    background_url = 'test_img/{}/background.png'.format(directory_name)

    create_background_img(background_url)

    generate_img(background_url, directory_name)
    print("Done with image {}".format(i))


print("Please have a look in the test_img/ directory to see created images.\n To start up the algorithm for image detection type: ")

print("Preparing to start image detection...")

for i in range(amount_of_test_imgs):
    directory_name = 'img_{}'.format(i)
    sub_directory = 'test_img/{}'.format(directory_name)

    filename = '{}/test.png'.format(sub_directory)

    print('Executing image detection for image {}'.format(i))
    main(filename, sub_directory)
    print('Finished image detection for image {}'.format(i))
    print('You can find the results in {}'.format(sub_directory))

print("Finished detection for all created images.")
