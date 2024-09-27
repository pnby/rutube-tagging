FROM python:3.12.5-bullseye

WORKDIR /

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app app

ENV PYTHONPATH=/app

