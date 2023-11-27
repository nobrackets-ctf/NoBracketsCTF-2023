FROM ghcr.io/downunderctf/docker-vendor/nsjail:ubuntu-22.04

ENV HOSTNAME zubaltron

ENV JAIL_CWD=/chal
COPY ./src/zubaltron.py /home/ctf/chal/pwn

RUN pip install inputimeout
RUN chmod +x /home/ctf/chal/pwn
