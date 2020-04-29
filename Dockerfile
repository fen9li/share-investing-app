FROM python:3.8.2-slim

COPY requirements.txt /
RUN pip install -r /requirements.txt

VOLUME /app
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["get.py"]