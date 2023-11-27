FROM ghcr.io/downunderctf/docker-vendor/nsjail:ubuntu-18.04

ENV JAIL_CWD=/chal
ENV TIME_LIMIT=180
# Copiez les fichiers sources dans le conteneur
COPY ./src/AAAAA /home/ctf/chal/pwn
COPY ./src/passwd.txt /home/ctf/chal/passwd.txt

RUN chmod 755 /home/ctf/chal/pwn
RUN chmod 744 /home/ctf/chal/passwd.txt
