FROM ubuntu:18.04
CMD ["/bin/bash"]
RUN apt-get update
RUN apt install firefox -y
RUN apt install matchbox -y
RUN apt-get install python3 -y
RUN apt install python3-django -y
RUN apt install python3-pip -y
RUN apt-get install xauth -y
RUN mkdir -p /usr/src/app
COPY ./Summary/ ./
CMD ["python3 Summary/manage.py runserver 3100"]
CMD export DISPLAY="127.0.0.1:0.0"; firefox