FROM ubuntu:18.04

RUN apt-get update -y
RUN apt-get install -y python3-pip ffmpeg libsm6 libxext6
RUN pip3 install --upgrade pip
RUN pip install opencv-contrib-python flask flask-sock websocket-client

COPY ./src /app
