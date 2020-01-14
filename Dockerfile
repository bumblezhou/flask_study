FROM python:3

WORKDIR ~/flask_study/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]

#References:
#https://hub.docker.com/_/python

#1.build docker image
# docker build -t flask_study .
#2.run it in docker
# docker run -it --rm --name flask_study -p 0.0.0.0:80:8080/tcp flask_study
