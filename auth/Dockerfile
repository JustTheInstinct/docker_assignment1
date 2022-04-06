FROM python:latest

WORKDIR /home

COPY requirements.txt /home
RUN apt-get update
RUN apt-get install -y python3-pip 
RUN pip install -r requirements.txt

COPY *.py /home
EXPOSE 5000
CMD ["python", "auth.py"]
