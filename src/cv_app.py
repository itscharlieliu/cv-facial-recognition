import os
import time
from utils.numpy_to_img import numpy_to_img
from websocket import create_connection, enableTrace, WebSocketApp
import cv2 as cv


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        ws.send("1")
        time.sleep(1)
        img = cv.imread("images/airplane.jpg")
        ws.send(numpy_to_img(img))
        time.sleep(1)
        ws.close()
        print("thread terminating...")

    run()


def start():
    print("Connecting...")

    enableTrace(True)
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
