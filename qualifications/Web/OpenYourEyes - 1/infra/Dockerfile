FROM python:3.10-slim-buster

WORKDIR /openyoureyes

COPY requirements.txt /openyoureyes/requirements.txt
RUN pip3 install -r requirements.txt

COPY ./src/static /openyoureyes/static/
COPY ./src/templates /openyoureyes/templates/
COPY ./app.py /openyoureyes/app.py

CMD [ "python3.10", "-m" , "flask", "run", "--host=0.0.0.0"]