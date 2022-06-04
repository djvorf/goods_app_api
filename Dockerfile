FROM python:3.9

WORKDIR /usr/src/api_goods

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements .
RUN pip install -r prod.txt

COPY . .