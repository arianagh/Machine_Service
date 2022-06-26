FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /djangomachine

COPY ./requirements.txt ./requirements.txt

#RUN #apt update
RUN apt -y install gcc mono-mcs

RUN pip install -r requirements.txt

COPY . /djangomachine/

EXPOSE 8000
