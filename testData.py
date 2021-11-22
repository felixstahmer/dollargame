from src.test.generate_img import generate_img, create_background_img

import sys

amount_of_test_imgs = int(sys.argv[1])
background_url = 'test_img/background.png'

create_background_img(background_url)

generate_img(amount_of_test_imgs, background_url)



