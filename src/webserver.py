import os
import threading
from flask import Flask, render_template, Response
import time

# TODO this doesn't work, so refactor this
# Note: Don't use app.run()
class webserver(threading.Thread):
    app = Flask(__name__)

    def __init__(self) -> None:
        threading.Thread.__init__(self)
        self._img = bytearray()

    def set_img(self, img):
        self._img = img

    def generate_frame(self):
        while True:
            # Testing

            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + self._img + b'\r\n')

            # TODO remove this delay
            time.sleep(1);


    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/video_feed')
    def video_feed(self):
        return Response(self.generate_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

    def run(self):
        self.app.run(host='0.0.0.0',  debug=True)



