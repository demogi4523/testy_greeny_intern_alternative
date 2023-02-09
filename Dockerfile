# pull the official docker image
FROM python:3.10

# set work directory
WORKDIR /tasks

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY /tasks/ /tasks/
