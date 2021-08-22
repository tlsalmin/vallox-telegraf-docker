FROM python:3.6-alpine

RUN apk add --update-cache telegraf py3-pip
RUN pip install vallox-websocket-api

RUN mkdir /app || echo "/app exists"
COPY metrics.py /app/metrics.py
COPY telegraf.conf /app/telegraf.conf

RUN chmod +x /app/metrics.py

CMD telegraf --config /app/telegraf.conf
