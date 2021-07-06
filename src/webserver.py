from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
    # https://blog.miguelgrinberg.com/post/video-streaming-with-flask
    # Use this to create a static webpage that can stream a video
    return "<p>Hello, World!</p>"