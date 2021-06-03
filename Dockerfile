FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install python3-dev python3-pip

COPY . .

RUN python3 -m pip install -r requirements.txt

RUN CMD["python3", "main.py"]