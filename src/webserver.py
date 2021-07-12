import os
from flask import Flask, render_template, Response
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def generate_frame():
    while True:
        # Testing
        print(os.listdir())

        with open("src/test.jpeg", "rb") as image:
            f = image.read()
            frame = bytearray(f)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        time.sleep(1);


@app.route('/video_feed')
def video_feed():
    return Response(generate_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0',  debug=True)