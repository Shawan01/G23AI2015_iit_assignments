# syntax=docker/dockerfile:1

FROM python:3.11

WORKDIR /python-docker

COPY . .

RUN pip install -r requirement.txt
EXPOSE 5000
CMD [ "python", "./run.py"] 