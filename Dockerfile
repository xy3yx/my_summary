FROM python:3.7
WORKDIR /usr/scr/app
RUN pip install Django
EXPOSE 3100
RUN mkdir -p /usr/src/app
COPY ./Summary/ ./
CMD ["python3", "manage.py", "runserver", "localhost:3100"]