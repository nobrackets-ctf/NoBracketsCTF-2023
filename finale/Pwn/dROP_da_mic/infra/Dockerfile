FROM ghcr.io/downunderctf/docker-vendor/nsjail:ubuntu-22.04

ENV JAIL_CWD=/chal
ENV TIME_LIMIT=180
#Copiez les fichiers sources dans le conteneur
COPY ./src/dROP_da_mic /home/ctf/chal/pwn
COPY ./src/flag.txt /home/ctf/chal/flag.txt

#Installation des tools nécessaires
RUN chmod 755 /home/ctf/chal/pwn
RUN chmod 744 /home/ctf/chal/flag.txt
