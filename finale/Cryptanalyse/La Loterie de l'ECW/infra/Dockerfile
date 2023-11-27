FROM ghcr.io/downunderctf/docker-vendor/nsjail:ubuntu-22.04

ENV JAIL_CWD=/chal
COPY ./src/secret.py /home/ctf/chal/
COPY ./src/challenge.py /home/ctf/chal/pwn
RUN chmod +x /home/ctf/chal/pwn
