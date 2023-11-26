FROM ghcr.io/downunderctf/docker-vendor/nsjail:ubuntu-22.04

ENV JAIL_CWD=/chal
ENV TIME_LIMIT=180
#Copiez les fichiers sources dans le conteneur
COPY ./src/TheBigBertha /home/ctf/chal/pwn
COPY ./src/password.txt /home/ctf/chal/password.txt

#Installation des tools nécessaires
RUN apt-get update && apt-get install -y python3
RUN chmod 755 /home/ctf/chal/pwn
RUN chmod 744 /home/ctf/chal/password.txt
