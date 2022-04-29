FROM python:3.10.1
ENV PYTHONUNBUFFERED 1
RUN mkdir /qr_menu
WORKDIR /qr_menu
ADD . /qr_menu/
RUN pip install -r requirements.txt