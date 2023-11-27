FROM debian:latest

ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone;

RUN apt-get update && apt-get install -y cron \
    vim \
    python3 \
    python3-pip \
    python3-venv \
    gosu \
    nano && \
    apt clean && \
    rm -rf /var/lib/apt/lists/

# Setup backup
RUN mkdir /backups/
#RUN crontab -l | { cat; echo "* * * * * cd /data/ && tar -cf /backups/backup.tar *"; } | crontab -
RUN echo "* * * * * cd /data/ && tar -cf /backups/backup.tar *" > /etc/crontab
#RUN service cron start

# Put flag
RUN echo "NBCTF{You've_Really_Becomed_Th3_R3d_Panda_And_Red_Team_Master!}" > /root/final_flag.txt
RUN chmod 700 /root/final_flag.txt

# Setup application
RUN useradd nbctfuser
RUN mkdir /data/
RUN chown -R nbctfuser:nbctfuser /data
COPY --chown=nbctfuser:nbctfuser ./src /data/
USER nbctfuser
WORKDIR /data
RUN python3 -m venv venv
RUN /data/venv/bin/pip install -r requirements.txt


USER root
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Run application
EXPOSE 1337

ENTRYPOINT ["/entrypoint.sh"]

# ENTRYPOINT ["/data/venv/bin/flask","run","--host","0.0.0.0","-p","1337"]

