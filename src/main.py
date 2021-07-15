from utils.numpy_to_img import numpy_to_img
from webserver import webserver
import cv2 as cv

import os

# Change working directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

img = cv.imread("images/IMG_2150.jpeg")

# print(streamer._img)
# print(cv.imencode(".jpeg", img)[1].tostring())
cv_webserver = webserver()
cv_webserver.set_img(numpy_to_img(img))

if __name__ == '__main__':
    cv_webserver.start()