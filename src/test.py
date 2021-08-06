import os
import cv2 as cv
from utils.numpy_to_img import numpy_to_img
from PIL import Image
import io

# Change working directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

img = cv.imread("images/airplane.jpg")

print(len(img))

print(numpy_to_img(img)[:30])

img2 = Image.fromarray(img)
img_byte_arr = io.BytesIO()

img2.save(img_byte_arr, format="JPEG")

print(img2.size)

print(img_byte_arr.getvalue()[:30])

with open("images/airplane.jpg", "rb") as image:
    f = image.read()
    print(f[:30])  # why is this different?
