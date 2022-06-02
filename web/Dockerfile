FROM python:latest

RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY requirements.txt /opt/app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chown -R www-data:www-data /opt/app
