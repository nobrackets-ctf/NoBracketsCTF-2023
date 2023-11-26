FROM python:3.10-slim-buster

WORKDIR /news

COPY requirements.txt /news/requirements.txt
RUN pip3 install -r requirements.txt

COPY ./src/static /news/static/
COPY ./src/templates /news/templates/
COPY ./app.py /news/app.py

CMD [ "python3.10", "-m" , "flask", "run", "--host=0.0.0.0"]