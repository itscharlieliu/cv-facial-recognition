import time
from webserver import app
from utils.numpy_to_img import numpy_to_img
from websocket import create_connection
import multiprocessing
import cv2 as cv

import os


def main():
    # Communicate with the webserver
    ws = create_connection(f"ws://127.0.0.1:5000/video_in")

    img = cv.imread("images/IMG_2150.jpeg")

    ws.send(b"1")


if __name__ == "__main__":
    # Change working directory
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    webserver = multiprocessing.Process(
        target=app.run, kwargs={"host": "0.0.0.0", "debug": True}
    )

    webserver.start()
    time.sleep(1)  # Wait for webserver to start

    main()

    webserver.join()
