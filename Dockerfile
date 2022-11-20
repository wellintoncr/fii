FROM python:3.10.5-bullseye

RUN useradd -ms /bin/bash dev

USER dev

WORKDIR /home/dev
