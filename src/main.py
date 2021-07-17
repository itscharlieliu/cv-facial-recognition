from utils.numpy_to_img import numpy_to_img
from websocket import create_connection
import cv2 as cv

import os

# Change working directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Communicate with the webserver
ws = create_connection(f"ws://127.0.0.1:5000/video_in")


img = cv.imread("images/IMG_2150.jpeg")

# print(streamer._img)
# print(cv.imencode(".jpeg", img)[1].tostring())
ws.send(numpy_to_img(img))
# ws.send("hello")

if __name__ == "__main__":
    print("Got here")
