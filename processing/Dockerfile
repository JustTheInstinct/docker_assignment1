FROM python:latest

EXPOSE 8100
WORKDIR /app

COPY requirements.txt /app
COPY . /app
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install -r requirements.txt
CMD python app.py