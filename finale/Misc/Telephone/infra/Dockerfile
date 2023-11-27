FROM ubuntu:16.04
WORKDIR /telephone/

RUN apt-get update
RUN apt-get install -y socat
RUN apt-get install -y python2.7

COPY ./entrypoint.sh /telephone/entry.sh
COPY ./src/challenge.py /telephone/challenge.py
COPY ./src/phone_number.txt /telephone/phone_number.txt
COPY ./src/flag.txt /telephone/flag.txt

RUN useradd --home=/telephone user
RUN chmod -R 4755 /telephone/ && chown -R user:user /telephone/

EXPOSE 7331
ENTRYPOINT ["/telephone/entry.sh"]
