
FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1


COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /code
WORKDIR /code
COPY ./mysite /code


RUN cd /code 
RUN python manage.py runserver 0.0.0.0:8000


