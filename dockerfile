FROM python:latest

WORKDIR /app 

COPY ./app/requirements.txt .
COPY ./app/MediaNation .

RUN pip install -r requirements.txt

EXPOSE 8080
