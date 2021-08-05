import os
import cv2 as cv
from utils.numpy_to_img import numpy_to_img

# Change working directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

img = cv.imread("images/airplane.jpg")
print(numpy_to_img(img)[:20])

with open("images/airplane.jpg", "rb") as image:
    f = image.read()
    print(f[:20])  # why is this different?
