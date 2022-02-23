FROM python:latest

EXPOSE 5000
WORKDIR /

COPY requirements.txt /
RUN apt install pip3
RUN pip install -r requirements.txt

COPY *.py /
CMD python auth.py
