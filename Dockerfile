FROM python:3.10.1
ENV PYTHONUNBUFFERED 1
RUN mkdir /QRMenu
WORKDIR /QRMenu
ADD . /QRMenu/
RUN pip install -r requirements.txt