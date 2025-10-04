FROM python:3.10-slim

WORKDIR /app

COPY app.py /app/

RUN pip install flask

COPY requirements.txt /app/

EXPOSE 5000

ENV APP_VERSION=v1

CMD["python","app.py"]