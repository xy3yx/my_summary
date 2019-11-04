FROM ubuntu:18.04
RUN apt-get update
RUN apt install firefox -y
RUN apt install matchbox -y
RUN apt-get install python3 -y
RUN apt install python3-django -y
RUN mkdir -p /usr/src/app
COPY ./Summary/ ./
RUN firefox &