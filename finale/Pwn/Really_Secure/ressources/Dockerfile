FROM ubuntu:22.04

# docker build -t chall . && docker run --rm -v $(pwd):/shared chall

RUN apt update && apt-get -y install gcc patchelf
WORKDIR /shared
CMD ["/bin/bash", "./compile.sh"]
