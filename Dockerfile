FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu20.04

RUN apt-get update && \
    apt-get install -y build-essential libssl-dev zlib1g-dev \
                       libncurses5-dev libgdbm-dev libnss3-dev \
                       libsqlite3-dev libreadline-dev libffi-dev \
                       curl libbz2-dev && \
    rm -rf /var/lib/apt/lists/*

RUN curl -O https://www.python.org/ftp/python/3.12.5/Python-3.12.5.tgz && \
    tar -xzf Python-3.12.5.tgz && \
    cd Python-3.12.5 && \
    ./configure --enable-optimizations && \
    make altinstall && \
    cd .. && \
    rm -rf Python-3.12.5.tgz Python-3.12.5

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /

COPY requirements.txt requirements.txt
RUN python3.12 -m pip install --no-cache-dir --upgrade -r requirements.txt

COPY app app
COPY prompts prompts

EXPOSE 8000

ENV PYTHONPATH=/app
