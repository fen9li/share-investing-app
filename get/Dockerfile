FROM python:3.8.2-slim

COPY requirements.txt /
RUN pip install -r /requirements.txt

VOLUME /app
WORKDIR /app

CMD ["sh","-c","sleep infinity"]