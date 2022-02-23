FROM python:latest

EXPOSE 8100
WORKDIR /app

COPY requirements.txt /app
COPY . /app
RUN pip install -r requirements.txt
CMD python app.py