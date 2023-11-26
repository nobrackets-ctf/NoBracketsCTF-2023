FROM debian:bookworm

ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /maze/

RUN apt update
RUN apt install -y socat
RUN apt install -y python3

COPY ./maze /maze/mazeGenerator
COPY ./entry.sh /maze/entry.sh
COPY ./maze.py /maze/maze.py
COPY ./flag.txt /maze/flag.txt

RUN useradd --home=/maze user
RUN chmod -R 4755 /maze/ && chown -R user:user /maze/

EXPOSE 7331
ENTRYPOINT ["/maze/entry.sh"]