FROM debian:bookworm

ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /marchand/

RUN apt update
RUN apt install -y socat
RUN apt install -y python3 python3-pip
RUN pip3 install networkx --break-system-packages

COPY ./entry.sh /marchand/entry.sh
COPY ./Marchand.py /marchand/Marchand.py
COPY ./flag.txt /marchand/flag.txt

RUN useradd --home=/marchand user
RUN chmod -R 4755 /marchand/ && chown -R user:user /marchand/

EXPOSE 7331
ENTRYPOINT ["/marchand/entry.sh"]
