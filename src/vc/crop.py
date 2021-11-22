import cv2
from PIL import Image

def crop_image(img_url, dst_url, x, y, width, height):
    image = cv2.imread(img_url)
    crop = image[y:y+height, x:x+width]
    im = Image.fromarray(crop)
    im.save(dst_url)
    return dst_url