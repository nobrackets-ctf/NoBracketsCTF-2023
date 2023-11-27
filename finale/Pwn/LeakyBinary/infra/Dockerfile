FROM ghcr.io/downunderctf/docker-vendor/nsjail:ubuntu-22.04

ENV JAIL_CWD=/chal
ENV TIME_LIMIT=180
#Copiez les fichiers sources dans le conteneur
COPY ./src/ /home/ctf/chal/
RUN mv /home/ctf/chal/chall /home/ctf/chal/pwn

#Installation des tools nécessaires
RUN chmod 744 /home/ctf/chal/flag
RUN chmod 755 /home/ctf/chal/ld-linux-x86-64.so.2
RUN chmod 755 /home/ctf/chal/libc.so.6
RUN chmod 755 /home/ctf/chal/pwn
