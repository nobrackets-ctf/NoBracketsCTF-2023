FROM ghcr.io/downunderctf/docker-vendor/nsjail:ubuntu-22.04

ENV JAIL_CWD=/chal
COPY ./src/secret.py /home/ctf/chal/
COPY ./src/lettre_amour_secret_partage.py /home/ctf/chal/pwn
COPY requirements.txt /home/ctf/chal/
RUN chmod +x /home/ctf/chal/pwn
RUN python3 -m pip install -r /home/ctf/chal/requirements.txt
