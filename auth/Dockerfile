FROM python:latest

EXPOSE 5000
WORKDIR /

COPY requirements.txt /
RUN apt-get update
RUN apt-get install -y python3-pip 
RUN pip install -r requirements.txt

COPY *.py /
CMD python auth.py
