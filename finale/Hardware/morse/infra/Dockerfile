FROM alpine:latest

# Installation de socat
RUN apk add --no-cache socat
# RUN apk add --no-cache pv

# Création du répertoire de travail
WORKDIR /app

COPY final.iq /app/signal.iq

# samp rate: 2048000 Hz
# 8 bytes per sample
# -> 16384000 bytes per second
# CMD socat TCP-LISTEN:1234,fork,reuseaddr EXEC:"pv -qL 16384000 /app/signal.iq"
CMD socat TCP-LISTEN:1234,fork,reuseaddr FILE:/app/signal.iq

EXPOSE 1234