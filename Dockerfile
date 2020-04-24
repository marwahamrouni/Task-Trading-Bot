FROM python:3.7

WORKDIR /usr/src/app

COPY ./Task.py ./TSLA.csv /usr/src/app/

RUN pip3 install pandas