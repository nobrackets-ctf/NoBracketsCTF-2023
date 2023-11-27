FROM ghcr.io/downunderctf/docker-vendor/nsjail:ubuntu-22.04

ENV HOSTNAME galacticdigger

ENV JAIL_CWD=/chal
RUN pip install inputimeout

COPY ./src/galactic_digger.py /home/ctf/chal/pwn

RUN chmod +x /home/ctf/chal/pwn
