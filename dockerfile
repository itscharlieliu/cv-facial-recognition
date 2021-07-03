FROM ubuntu:18.04

RUN apt-get update -y
RUN apt-get install -y python3.7 python3-pip
RUN pip3 install --upgrade pip
RUN pip install opencv-contrib-python

COPY ./src /app
