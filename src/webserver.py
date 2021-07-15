import os
from flask import Flask, render_template, Response
import time

class _Streamer:
    _img = bytearray()

    def __init__(self) -> None:
        with open("test.jpeg", "rb") as image:
            f = image.read()
            self._img = bytearray(f)

    def set_img(self, img):
        self._img = img

    def generate_frame(self):
        while True:
            # Testing

            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + self._img + b'\r\n')

            # TODO remove this delay
            time.sleep(1);

streamer = _Streamer()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(streamer.generate_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

