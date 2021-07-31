import time
from utils.numpy_to_img import numpy_to_img
from websocket import create_connection
import cv2 as cv


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")


def start():
    print("Connecting...")

    # Communicate with the webserver
    ws = create_connection(f"ws://127.0.0.1:5000/video_in")

    img = cv.imread("images/airplane.jpg")

    # print(numpy_to_img(img))
    time.sleep(1)

    ws.send(b"1")

    ws.send(numpy_to_img(img))

    ws.send(b"2")

    ws.close()
    print("Done")


if __name__ == "__main__":
    start()
