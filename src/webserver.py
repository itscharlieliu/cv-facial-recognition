from flask import Flask, render_template, Response
from flask_sock import Sock
import time


class _Streamer:
    _img = bytearray()

    def set_img(self, img):
        self._img = img

    def generate_frame(self):
        while True:
            # Testing
            frame = (
                b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + self._img + b"\r\n"
            )
            yield (frame)

            # TODO remove this delay
            time.sleep(1)


streamer = _Streamer()

app = Flask(__name__)
sock = Sock(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    return Response(
        streamer.generate_frame(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


# Send jpeg image via websocket
@sock.route("/video_in")
def echo(ws):
    while True:
        data = ws.receive()
        streamer.set_img(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, use_reloader=False)
