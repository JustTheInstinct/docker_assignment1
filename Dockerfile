# Change image to valid image
FROM python:latest
# Startup
RUN apt get update
RUN git clone https://github.com/JustTheInstinct/docker_assignment1.git
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Installations
RUN apt install python3
RUN apt install pip3
RUN pip install -r requirements.txt

# idk what else
EXPOSE 5000
CMD ["flask", "run"]
