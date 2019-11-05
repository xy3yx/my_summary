FROM python:3.7
RUN mkdir -p /usr/src/app
WORKDIR /usr/scr/app
RUN pip install Django
EXPOSE 3100
COPY ./Summary/ ./
CMD ["python3", "manage.py", "runserver", "localhost:3100"]