import os
import time
import threading

import cv2 as cv
from websocket import WebSocketApp, create_connection, enableTrace

from utils.numpy_to_img import numpy_to_img


class cvThread(threading.Thread):
    def __init__(self, ws):
        threading.Thread.__init__(self)
        self.ws = ws

    def run(self):

        for i in range(30):
            time.sleep(1)
            img = cv.imread("images/airplane.jpg")
            self.ws.send(numpy_to_img(img), opcode=0x2)
            time.sleep(1)
            img = cv.imread("images/IMG_2150.jpeg")
            self.ws.send(numpy_to_img(img), opcode=0x2)

        time.sleep(1)

        self.ws.close()
        print("thread terminating...")


def on_message(ws, message):
    pass


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    thread = cvThread(ws)

    thread.start()


def start():
    print("Connecting...")

    # enableTrace(True)
    ws = WebSocketApp(
        "ws://127.0.0.1:5000/video_in",
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )

    ws.run_forever()


if __name__ == "__main__":
    # Change working directory
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    start()
