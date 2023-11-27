FROM ghcr.io/downunderctf/docker-vendor/nsjail:ubuntu-22.04

ENV JAIL_CWD=/chal
COPY ./src/server.py /home/ctf/chal/pwn
RUN chmod +x /home/ctf/chal/pwn
RUN python3 -m pip install pycryptodome
