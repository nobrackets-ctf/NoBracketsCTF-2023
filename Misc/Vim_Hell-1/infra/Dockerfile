FROM disconnect3d/nsjail

# Install necessary packages
RUN apt-get -qq update
RUN apt-get install openssh-server vim -y

ENV HOSTNAME vim-hell

# Add prisoner user
RUN useradd prisoner --shell=/bin/rbash
RUN echo "prisoner:prisoner"|chpasswd

# Set up environment
RUN mkdir /rbin
RUN mkdir /home/prisoner

COPY ./src/flag.txt /home/prisoner/flag.txt
COPY ./src/unicorn /home/prisoner/unicorn
COPY ./src/vim /rbin/vim

RUN cp /bin/ls /rbin/ls
RUN chmod -R 555 /rbin

RUN echo "PATH=/rbin" >> /home/prisoner/.profile
RUN echo "alias echo=ls" >> /home/prisoner/.profile

WORKDIR /home/prisoner

# Start SSH service
RUN service ssh restart
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]
